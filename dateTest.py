from time import localtime, time, strftime
from datetime import datetime, timedelta


now_date = strftime('%Y-%m-%d', localtime(time()))
print(now_date)





today = datetime.now()
yesterday = today - timedelta(days=1)
formatted_yesterday = yesterday.strftime('%Y-%m-%d')

print(formatted_yesterday)