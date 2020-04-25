################################################################
# Learning Python
###############################################################
from datetime import datetime, timedelta

# timedelta is used to define a period of time 
'''oneday = timedelta(days=1)
today = datetime.now()

# get ester days date and time using time delta
yesterday = today - oneday
print(yesterday.day)
print(yesterday.month)
print(yesterday.year)
print(yesterday.hour)
print(yesterday.minute)
print(yesterday.second)

# conversion of string to date
birthday = input('when is your birthday (dd/mm/yyyy)')
bd_day = datetime.strptime(birthday, '%d/%m/%Y')
oneday = timedelta(days=1)
print(bd_day - oneday)'''

# error handling
# 1 Syntax Errors
'''x=90
y=0

# try and except is used to catch run time errors
try:
    print(x/(y+6))
except ZeroDivisionError as e:
    print(str(e))
except:
    print("sorrry something really went wrong")
finally:
    print("excecution successfull")

test = 'Hello dude how are u'
test2 = test.split(' ')
temp = 1

for i in range (len(test2)):
    len1 = len(test2[i])
    if temp > len1:
        strr = test2[]
        continue
    temp = len1

print(strr)'''

for i in range(1, 7):
    print(i * '*')
