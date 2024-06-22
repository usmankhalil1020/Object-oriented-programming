#class Method   

class Person:
    name="ibrahim"

    def changeName(self,name):
        self.name=name

p1=Person()
p1.changeName("Usman Khalil")
print(p1.name)
print(Person.name)

class Person:
    name="ibrahim"

    def changeName(self,name):
        Person.name=name

p1=Person()
p1.changeName("Usman Khalil")
print(p1.name) 
print(Person.name) 

class Person:
    name="Ibrahim"

    def changeName(self,name):
        self.__class__.name="Usman Khalil"

p1=Person()
p1.changeName("Usman Khalil")
print(p1.name)
print(Person.name) 

class Person:
    name="currun"

    @classmethod
    def changeName(cls,name):
        cls.name=name

p1=Person()
p1.changeName("Rehan")
print(p1.name)
print(Person.name) 

class Person:
    name="Currun"

    @classmethod
    def changeName(cls,name):
        cls.name=name

p1=Person()
p1.changeName("qasmi")
print(p1.name) 
print(Person.name)

class Person:
    name="umar"

p1=Person()
print("Person name:",p1.name)  

class Person:
    name="Currun"

    @classmethod
    def changeName(cls,name):
        cls.name=name

p1=Person()
p1.changeName("Sam")
print(p1.name)  
print(Person.name) 

class Person:
    name="Umar"

    @classmethod
    def changeName(cls,name):
        cls.name=name

p1=Person()
p1.changeName("Usman")
print("Change Name:",p1.name)
print("Person Name:",Person.name) 

#PropertyMethod

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage=str((self.phy+self.chem+self.math) / 3)

    def calcpercentage(self):
        self.percentage=str((self.phy+self.chem+self.math) / 3)    

stu1=Student(98,90,85)
print(stu1.percentage) 

stu1.math=51
print("Math Marks",stu1.math)

stu1.calcpercentage()
print(stu1.percentage)

#PropertyeasyMethod

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math) / 3)

stu1=Student(98,97,96)
print(stu1.percentage)

stu1.math=60
print("Marks change:",stu1.math)
print(stu1.percentage)

class Student:
    def __init__(self,math,phy,chem):
        self.math=math
        self.phy=phy
        self.chem=chem

    @property
    def percentage(self):
        return str((self.math+self.phy+self.chem) / 3) 

stu1=Student(65,54,85)
print(stu1.percentage)

stu1.math=45
print("Math Change=",stu1.math)
print("New Percentage=",stu1.percentage)

class Student:
    def __init__(self,math,chem,phy):
        self.math=math
        self.chem=chem
        self.phy=phy

    @property
    def percentage(self):
        return str((self.math + self.chem + self.phy) / 3)

stu1=Student(65,89,67)
print("old percentage=",stu1.percentage)

stu1.math=85
print("Math change=",stu1.math)
print("New percentage=",stu1.percentage)

class Student:
    def __init__(self,eng,math,chem,phy):
        self.eng=eng
        self.math=math
        self.chem=chem
        self.phy=phy

    @property
    def percentage(self):
        return str((self.eng + self.math + self.chem + self.phy) / 4)

stu1=Student(65,87,91,69)
print("Percentage=",stu1.percentage)

stu1.eng=80
stu1.math=95
print("English change=",stu1.eng)
print("Math Change=",stu1.math)
print("New percentage=",stu1.percentage)

#Polymorphism

print(1+2)
print("usmsn"+" "+"khalil") #concatenate
print([1,2,3] + [4,5,6]) #merge

class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def showNumber(self):
        print(self.real,"R +",   self.imag,"I")

num1=Complex(6,4)
num1.showNumber() 

num2=Complex(10,8)
num2.showNumber()

#Functions

def Hello():
    print("hello world")

h1=Hello() 

def var():
    print("variables and constant")
var1=var() 

def add():
    x=25
    y=25
    print(x+y)
add1=add()   

def mul():
    a=5
    b=2
    print(a*b)
mul1=mul() 

#Parameters & Arguments

def add(x,y):
    print(x+y)

add1=add(25,35)  
add2=add(10,10)

def subtract(x,y):
    print(x-y)

subtract1=subtract(6,2)
subtract2=subtract(5,4) 

def perimeter(a,b):
    print("Perimeter is =",2*(a+b))

per1=perimeter(20,2)

def rectangle(length,breath):
    print("area of rectangle is:",length * breath)

rec1=rectangle(25,25)

#Arbitary Arguments

def hello(*name):
    print("Hello, my name is:", name[2])

hello1=hello("usman","umar","asma") 

#Return Statement and Recursion in python

def var():
    return("a is greater than b")

print(var())

def add(a,b):
    return ("the addition of two numbers is =",a+b)

print(add(20,5))

def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))
print("Factorial of 5 is =",fact(5))

def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))
print("Factorial of 6 is =",fact(6))  

#Lambda Functions in python

a=lambda b: b*5
print(a(4))

a=lambda b: b*6
print(a(7))

x = lambda a,b,c: (a+b)*c
print(x(3,7,2))

x = lambda a,b,c: (a*b)+c
print(x(2,5,7))

#Local and Global variables

x=24
print("first variable x =",x)

def var():
    x=25
    return x
print(var())

print(x)

x=56
print("first value is =",x)

def var():
    x=45
    return x
print(var())

print(x)

#global variable
x=67
print("first value is =",x)

def var():
    global x
    x=78
    return x
print(var())

print(x)

x=50

def var():
    global x
    x=100
    return x
print(var())

print(x)

x=35

def var():
    global x
    y=45
    return y
print(var())

print(x)

#Writen a function to find maximum of three numbers in python

def maximum_value(val1,val2,val3):
    if(val1 > val2 and val1 > val3):
        print(val1, "is the greatest number.")

    elif(val2 > val1 and val2 > val3):
        print(val2, "is the greatest number.")

    else:
        print(val3, "is the greatest number.")

maximum_value(12,28,63)

#Writen a function to find maximum of four numbers in python

def max_value(val1,val2,val3,val4):
    if(val1 > val2 and val1 > val3 and val1 > val4):
        print(val1,"is the greatest number.")

    elif(val2 > val1 and val2 > val3 and val2 > val4):
        print(val2, "is the greatest number.")

    elif(val3 > val1 and val3 > val2 and val3 > val4):
        print(val3, "is the greatest number.")

    else:
        print(val4, "is the greatest number.")

max_value(25,22,55,56)

#Write a python function to create and print a list where the values are squares of numbers between 1 to 30

def create_list():
    l=[]
    for i in range(1,31):
        l.append(i**2)
    return l
print(create_list())    

#Write a python function to create and print a list where the values are cubes of numbers between 1 to 25

def create_list():
    l=[]
    for i in range(1,26):
        l.append(i**3)
    return l
print(create_list())

# Write a python function that takes a number as a parameter and check if the number is prime or not

def check_prime(num):
    if(num == 1):
        print("it is not a prime number.")
    if(num == 2):
        print("it is a prime number.")    
    for i in range(2,num):
        if num % i == 0:
            print("it is not a prime number.")
            break
        else:
            print("it is a prime number.")
            break

check_prime(51)            

def check_prime(num):
    if(num == 1):
        print("it is not a prime number.")
    if(num == 2):
        print("it is a prime number.")    
    for i in range(2,num):
        if num % 1 == 0:
            print("it is not a prime number.")
            break
        else:
            print("it is a prime number")
            break
check_prime(50)  

# Write a python function to sum all the numbers in a list

def add(num):
    total = 0
    for i in num:
        total=total + i
    return(total)

print(add([1,2,3,4]))  

def add(num):
    total = 0
    for i in num:
        total=total + i
    return(total)

print(add([1,2,3,4,5]))  

#Solution 2 (Recursion)

def add(nums):
    if len(nums)==1:
        return (nums[0])

    else:
        return ((nums[0]) + add(nums[1:]))
    
print("The sum of all numbers in a list is =",add([1,2,3,4,5]))    
    
    
        

































































































































































  














































    










































































































