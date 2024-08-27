#!/usr/bin/python
# -*- coding: utf-8 -*-

import lbcore


EMAIL_TEMPLATE_ID__PAYMENT = 'email.payment'
SMS_TEMPLATE_ID__PAYMENT = 'sms.payment'

EMAIL_TEMPLATE_ID__CANCEL_PAYMENT = 'email.cancel_payment'
SMS_TEMPLATE_ID__CANCEL_PAYMENT = 'sms.cancel_payment'

PAYMENT_NOTICE_TYPE = 4


module = lbcore.Module()
module.SetName("NotifyPayment", 1)
module.SetTitle("LANBilling Python module notification")


def notify_payment(msg, arg, con):

    class SkipNotice(Exception):
        pass

    try:
        con.log_debug('Payment received. Check notify payment %s' % arg)
        lbsettings = lbcore.Settings()
        if lbsettings.GetSettingValue(lbsettings.notifications_enabled, "1") == "0":
            raise SkipNotice('Skipping due to config settings')

        agreements = con.call('getAgreements', {'agrm_id': arg['agrmid']})

        if not agreements:
            raise Exception('Agreement not exists for agrm_id %s' % arg['agrm_id'])

        agreement = agreements[0]
        account = con.call('getAccount', {'uid': agreement['uid']})

        if not account:
            raise Exception('Account not exists for uid %s' % agreement['uid'])

        # check user notice
        notices = con.call('getAccountNotices', {'uid': agreement['uid'], 'notice_type': PAYMENT_NOTICE_TYPE})
        if not notices:
            con.log_debug('Notice of type 4 is off for account, uid %s' % agreement['uid'])
            return

        currencies = con.call('getCurrencies', {'cur_id': agreement['cur_id']})

        if not currencies:
            raise Exception('Currency not exists for cur_id %s' % agreement['cur_id'])

        currency = currencies[0]

        params = {}
        params['username'] = account['name']
        params['amount'] = round(arg['amount'], 2)
        params['currency'] = currency['symbol']

        is_cancelled = arg.get('is_cancelled', False)

        if not is_cancelled:
            params['agrm_number'] = agreement['agrm_num']
            params['balance'] = round(agreement['balance'], 2)
            if params['balance'] == 0:
                params['balance'] = 0.00

        def check_recipient(recipient_category, user_type, sole_proprietor):
            if recipient_category == 0:
                return True
            elif recipient_category == 1:
                return user_type == 2 and not sole_proprietor
            elif recipient_category == 2:
                return user_type == 1 or sole_proprietor

            return False

        sms_template_id = SMS_TEMPLATE_ID__CANCEL_PAYMENT if is_cancelled else SMS_TEMPLATE_ID__PAYMENT
        email_template_id = EMAIL_TEMPLATE_ID__CANCEL_PAYMENT if is_cancelled else EMAIL_TEMPLATE_ID__PAYMENT
        recipient_category_sms = con.call('getSbssSettingsNotices', {'id': sms_template_id})[0]['recipient_category']
        recipient_category_email = con.call(
            'getSbssSettingsNotices', {'id': email_template_id})[0]['recipient_category']
        can_send_sms = check_recipient(recipient_category_sms, account['type'], account['sole_proprietor'])
        can_send_email = check_recipient(recipient_category_email, account['type'], account['sole_proprietor'])

        if not can_send_sms:
            con.log_debug(
                'Notifications with id = %s are disabled for this user category.' % sms_template_id
            )

        if not can_send_email:
            con.log_debug(
                'Notifications with id = %s are disabled for this user category.' % email_template_id
            )

        if notices[0]['notices'][0]['is_email'] is True and can_send_email:
            if not account['email']:
                con.log_warning('Empty user email for uid %d.' % agreement['uid'])
            else:
                msg = {
                    'template_id': email_template_id,
                    'params': params,
                    'email_to': account['email'],
                    'uid': agreement['uid']
                }
                con.call('sendMail', msg)

        if notices[0]['notices'][0]['is_sms'] is True and can_send_sms:
            if not account['mobile']:
                con.log_warning('Empty user mobile phone for uid %d.' % agreement['uid'])
            elif not account['mobile_is_confirmed']:
                con.log_warning('Mobile is not confirmed for uid %d.' % agreement['uid'])
            else:
                send_params = {
                    'numbers': [account['mobile']],
                    'template_id': sms_template_id,
                    'params': params,
                    'sync': True,
                    'uid': account['uid']
                }
                con.call('sendSms', send_params)

    except SkipNotice as e:
        con.log_debug('Skip notify payment: %s' % str(e))

    except Exception as e:
        con.log_error('Cant notify payment: %s' % str(e))


m = lbcore.Messenger(notify_payment, 'notify_payment')
