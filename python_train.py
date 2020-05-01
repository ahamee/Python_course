from datetime import datetime, timedelta
#today = datetime.now()
#print('todays date is: '+ str(today))

## timedelta is used to deine a period of time
#one_day = timedelta(days=2)
#yesterday = (today - one_day)
#print('Date before two days was: ' + str(yesterday))

## getting only exact days and months and year
#print('todays date is: '+ str(today.day))
#print('todays date is: '+ str(today.month))
#print('todays date is: '+ str(today.year))

# when date is taken a input
#birthday = input('when is your birthday (dd/mm/yyyy) ?')
#DOB = datetime.strptime(birthday, '%m/%d/%Y')
#print('Birthday ' + str(DOB))

# Error Handeling
x = 42
y = 0
#try:
#    print(x/y)
#except ZeroDivisionError as e:
#    print('Not allowed to divide by zero')
#else:
#    print('Somehing else is wrong')
#finally:
#    print('This happens sometimes')

## Conditions
#if x == y:
#    print('y')
#elif x > y:
#    print('G')
#else:
#    print("N")

# List
names = ['chudi ba', 'abdul', 'jaffer', 'waseem']

# append will add object to the end of the list
names.append('nadeem')
#names.append(99)

# insert will add object at a particular index position
names.insert(0, 'javeed')

# Replace
names[1] = 'aaquib'

# pop method remves the object based on the vaue passed into the pop method
#poped_name = names.pop()

# deleting elements from a list
#del names[0]

# removing and element from list
#names.remove('aaquib')

# Sort List in order basically it will consider in asc
#names.sort(reverse=True)

# sortig List temporary
#sorted(names)

# reversing a list
#names.reverse()

# length of List
#print(len(names))

#Looping through List
#count = len(names)
#for i in range (0,count):
#    print(names[i])
# OR
#for NAME in names:
#    print(NAME)

#getting a numerical list
#ODD = list(range(10,1,-1))
#print(ODD)

## generating square numbers and adding it to a list
#squaroot = []
#for i in range(1,10):
#    sqr = i**2
#    squaroot.append(sqr)
#print(squaroot)
#squares = [value**2 for value in range(1,11)]
#print(squares)


## slicing a list
#print(names[3:-2])
## ooping through sliing list
#for name in names[2:6]:
#    print(name)

## Tuple Values cannot be changed once assigne hence they are called immutable
#dimensions = (100,20)
#print(dimensions[0])

#num = int(input("enter number: \t"))
#print(type(num))

## Dictionaries
#car = {}
#car['Roma'] = 'ferrari'
#car['Civic'] = 'Honda'
#car['Hell cat'] = 'Dodge'
#print(car)

user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)