from decimal import Decimal, getcontext
from datetime import datetime, date, timedelta

from typing import Union

# getcontext().prec = 1
DATE_FORMAT = '%Y-%m-%d'


def add(items: dict, title: str, amount: Decimal, expiration_date: str=None) -> None:
    if not items.get(title):
        items[title] = list()

    if expiration_date:
        expiration_date = datetime.strptime(expiration_date, DATE_FORMAT).date()

    items[title].append({'amount': amount, 'expiration_date': expiration_date})


def add_by_note(items: dict, note: str) -> None:
    note_list = note.split()

    try:
        test_date = datetime.strptime(note_list[-1], DATE_FORMAT).date()
        expiration_date = note_list.pop()
    except ValueError:
        expiration_date = None

    print(note_list)
    amount = Decimal(note_list.pop())
    print(note_list)
    title = ' '.join(note_list)
    add(items, title, amount, expiration_date)


def find(items: dict, needle: str) -> list:
    search_result = []
    needle = needle.lower()

    return [product for product in items.keys() if product.lower().find(needle) >= 0]


def amount(items: dict, needle: str) -> Decimal:
    products_list = find(items, needle)

    if not products_list:
        return Decimal(0)

    total_amount = 0
    for product in products_list:
        for pack in items[product]:
            total_amount += pack['amount']

    return total_amount

def expire(items: dict, in_advance_days: int=0) -> Union[list, None]:
    check_time = date.today() + timedelta(days=in_advance_days)
    verdue_products = []
    for product_name, features_list in items.items():
        amount_verdue = 0
        is_verdue = False

        for pack in features_list:
            if not pack['expiration_date']:
                continue

            if check_time >= pack['expiration_date']:
                is_verdue = True
                amount_verdue += pack['amount']

        if is_verdue:
            verdue_products.append((product_name, amount_verdue))

    return verdue_products






