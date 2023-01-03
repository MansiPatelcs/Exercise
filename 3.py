import datetime

now=datetime.datetime.now()
print('Current date and time:')
print(now.strftime('%y-%m-%d %H:%M:%S'))
print(now.strftime('%y-%m-%d on %A, %B the %dth, %y'))
print(now)


from datetime import date

today=date.today()
print("Today's date:",today)


