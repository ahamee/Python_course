#from datetime import datetime, timedelta
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
#x = 42
#y = 0
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

## List
#names = ['chudi ba', 'abdul', 'jaffer', 'waseem']

# append will add object to the end of the list
#names.append('nadeem')
#names.append(99)

## insert will add object at a particular index position
#names.insert(0, 'javeed')

## Replace
#names[1] = 'aaquib'

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

## Looping through dictionary
#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',
#    }
#favorite_languages['Tam'] = 'C#'
#print(favorite_languages)

#for name, language in favorite_languages.items():
#    print(name.title() + "'s favorite language is " + language.title() + ".")

## Looping through all keys in dictionary
#for name in favorite_languages.keys():
#    print(name.title())

## while Loops
## Removing Instances from a list
#pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
#print(pets)
#while 'cat' in pets:
#    pets.remove('cat')
#    print(pets)

#responses = {}
#polling_active = True
#while polling_active:
#    name = input('Enter ur Name \n')
#    party = input('whon do you want to vote \n')

#    responses[name] = party    

#    poll = input('Do you want to continue ? (y/n)')    
#    if poll == 'n':
#        polling_active = False

#for name, party in responses.items():
#    print (name + ' want to vote for ' + party)

##Functions
# Positional arguments
#def describe_pet(animal_type, pet_name):
#    """Display information about a pet."""
#    print("\nI have a " + animal_type + ".")
#    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#describe_pet('cat','Meow')
#describe_pet('cow','ganga')

# keyword based Arguments
#def describe_pet(animal_type, pet_name):
#    """Display information about a pet."""
#    print("\nI have a " + animal_type + ".")
#    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#describe_pet(animal_type = 'cat', pet_name = 'Meow')
#describe_pet('cow','ganga')

# Returning a value from a function
#def ood_even(num):
#    if (num%2) == 0:
#        return 'Even'
#    else:
#        return 'Odd' 

#print(ood_even(4))

## Arbitary Number of aurguments
#toppi = []
#def Pizza_topings(*toppings):
#    print(toppings)

#Pizza_topings('chillies')    

#for items in toppi:
#    print(items)

## Arbitary keyword Arguments
#def user_info(first_name, Last_name, **personal_info):
#    profile = {}
#    profile['first_name'] = first_name.title()
#    profile['last_name'] = Last_name.title()
#    # use for loop for storing personal info items 
#    for key, value in personal_info.items():
#        profile[key] = value
#    return profile

##profil = user_info('abdul', 'hameed', age=25, email = 'hameed@gmail.com')
##print(profil)

#import python_train

#pro = python_train.user_info('abdul','hameed',age=26,email='hameedm@gmail.com')
#print(pro)

#print("CHudi Ba")\

## OOPS
#class Example:
#    'this is an sample class for adding two numbers'
#    def __init__(self, a, b):
#        self.a = a
#        self.b = b

#    def add(self):
#        return self.a + self.b

#e = Example(8, 6)
#print(e.add())
#print(Example.__doc__)

#class Employee:
#    def __init__(self, first, Last, age, pay):
#        self.first = first
#        self.Last = Last
#        self.age = age
#        self.pay = pay
    
#Emp1 = Employee('abdul','Hameed',25,60000)
#Emp2 = Employee('abdul','Waheed',25,70000)
#print(Emp1.first)
#print(Emp2.Last)

#class Student:
#    age = 26             # |
#    USN = '1gv12ec001'   # |------Instance vriables or class variable
#    name = 'Abdul'       # |

#    def student_details(self):
#        clg = 'ttit' # Local Variables
#        print('clg = ', clg)
#        print('age = ', self.age)
#        print('USN = ', self.USN)
#        print('name = ', self.name)
#        print('The student details')
#    def reading(self):
#        print('reading....')


#s1 = Student()
#s1.student_details()

#class Employee:
#    empl_count = 0

#    def __init__(self, name, salary):
#        self.name = name
#        self.salary = salary
#        self.empl_count += 1

#    def displayCount(self):
#        print("Total Employees are %d" % Employee.empl_count)
    
#    def diplayEmploye(self):
#        print("Name: ", self.name, ", Salary: ", self.salary)


#emp1 = Employee('Test1',50000)
#emp2 = Employee('Test2',60000)

#emp1.diplayEmploye()
#emp2.diplayEmploye()
#print(Employee.displayCount)

#class Employee:
#    'Common base class for all employees'
#    empCount = 0
#    def __init__(self, name, salary):
#        self.name = name
#        self.salary = salary
#        Employee.empCount += 1

#    def displayCount(self):
#        print ("Total Employee %d" % Employee.empCount)
    
#    def displayEmployee(self):
#        print ("Name : ", self.name, ", Salary: ", self.salary)


##This would create first object of Employee class"
#emp1 = Employee("Zara", 2000)
##This would create second object of Employee class"
#emp2 = Employee("Manni", 5000)
#emp1.displayEmployee()
#emp2.displayEmployee()
#print ("Total Employee %d" % Employee.empCount)
#print ("Employee.__doc__:", Employee.__doc__)
#print ("Employee.__name__:", Employee.__name__)
#print ("Employee.__module__:", Employee.__module__)
#print ("Employee.__bases__:", Employee.__bases__)
#print ("Employee.__dict__:", Employee.__dict__ )

#class Presenter():
#    def __init__(self,name):
#        self.name = name

#    @property
#    def name(self):
#        print ('In Getter')
#        return self.__name

#    @name.setter
#    def name(self,value):
#        print('In setter')
#        self.__name = value

#presenter = Presenter('chris')
##presenter.name  = 'Chrostopher'
##presenter.say_hello()
#print(presenter.name)

# Inheritance
# Accessing One Class from another as SubClass
#class Parents:
#    'this is a parent class or Super Class'
#    def __init__(self, name):
#        self.name = name

#    def say_hello(self):
#        print('Hello, ' + self.name)

#class Student(Parents):
#    'This is a Child class or a Subclass'
#    def __init__(self, name, school):
#        # in Order to access arguments from super class into the constructer of child class use super().__init__(argument) 
#        super().__init__(name)
#        self.school = school
#    def sing_school_song(self):
#        print("long Live " + self.school)

#student = Student('Harry', 'Howgart')
#student.say_hello()
#student.sing_school_song()

# Inheritance
#class Vehicle:

#    def __init__(self, veh_type):
#        self.veh_type = veh_type
#    def car_name (self, name):
#        return "The "+ self.veh_type +" Name is " + name

#class Vehicle_specification(Vehicle):

#    def des(self):
#        return "Completed"

#vehi = Vehicle_specification('HatchBack')
#car = vehi.car_name('Swift')
#print(car)

#class BankAccount:
#    # initializr the class
#    def __init__(self):
#        self.balance = 0
    
#    # This function takes the amount you deposit into the bank account
#    def deposit(self, amount):
#        self.balance = self.balance + amount

#    def withdraw(self, amount):
#        if self.balance >= amount:
#            self.balance -= amount
#        else:
#            print("Insufficient Funds")
    
#    def print_balance(self):
#        return self.balance

#account = BankAccount()
#for i in range (1,5):
#    account.deposit(int(input("Enter the amount to be deposited \n")))

#account.withdraw(6000000)
#money = account.print_balance()

#print(money)

#class Person:
#    def __init__(self, Name, age):
#        self.Name = Name
#        self.age = age
    
#    def myfunc(self):
#        print("Hello {} age is {}".format(self.Name, self.age))

#p1 = Person("Name", 26)
#p1.age = 55
#del p1.age
#p1.myfunc()

## Advance Python

## there are 3 types of Methods
## 1. Instance Methods 
## 2. Class Methods
## 3. Static Methods

#class Student:

#    # Class Varaible
#    school = "BEML"

#    def __init__(self, m1, m2, m3):
#        self.m1 = m1
#        self.m2 = m2
#        self.m3 = m3

#    # instance method as it works with Object
#    # 2 types of instances Accesors(to fetch) and Mutators (to Update)
#    def avg(self):
#      return (self.m1 + self.m2 + self.m3)/3

#    # get method (getter) accessors
#    def get_m1(self):
#        return self.m1

#    # Set Method (Setter) Mutators
#    def set_m1(self, value):
#        self.m1 = value

#    # Class Methods to access Class Variables
#    @classmethod
#    def school_Name(cls):
#        return cls.school

#    # Static Methods Nothing to do with class variable or Instance variable
#    @staticmethod
#    def Info():
#        print("This is student class.. in this module")


#s1 = Student(32,46,67)
#s1 = Student(39,45,65)

#print(s1.avg())
#print(Student.school_Name())
#Student.Info()

## Class within a Class

#class Student:

#    def __init__(self, Name, Roll):
#        self.Name = Name
#        self.Roll = Roll
#        self.Lap = self.Laptop()

#    def show(self):
#        print(self.Name, self.Roll)
#        self.Lap.show()

#    class Laptop:
        
#        def __init__(self):
#            self.brand = 'HP'
#            self.Processor = 'AMD Ryzen'
#            self.Ram = "HyperX 8GB"
#        def show(self):
#            print('This is an ' + self.brand + ' Laptop it is powered with ' + self.Processor + 'and Ram ' + self.Ram)

#s1 = Student('Chudi Baa', '13')
#s2 = Student('Abdul', '01')
#s1.show()
#s1.Laptop.show

# inheritance 
class A:

    def __init__(self):
        print('in init of A')
    def feature1(self):
        print('Feature1 working')
    def feature2(self):
        print('Feature2 working')

class B(A):

    def __init__(self):
        #super represents the super class
        super().__init__()
        print('in init of B')

    def feature3(self):
        print('Feature3 working')
    def feature4(self):
        print('Feature4 working')
#TO call both the __init__ for A and B we have to use super
a1 = B()