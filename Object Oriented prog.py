class Student:
    name="usman"

s1=Student()
print(s1)

class Student:
    name="Khalil"

s1=Student()
print(s1.name)

s2=Student()
print(s2.name)

class Car:
    color="green"
    brand="corolla"

car1=Car()
print("Car color:",car1.color)
print("Car brand:",car1.brand)

class Flag:
    color="green"

flag1=Flag()
print("Pakistan flag color:",flag1.color)

class Fruit:
    apple="red"
    banana="yellow"

fruit1=Fruit()
print("Apple color:",fruit1.apple)    
print("Banana color:",fruit1.banana)

#Constructor __init_-(self)

class Student:
    def __init__(self):
        print(self)
        print("add new student in database:")
        print("Muhammad Usman Khalil")

s1=Student()

class Student:
    def __init__(self,full_name):
        self.name=full_name

s1=Student("Usman")
print("Name:",s1.name)

class Student:
    def __init__(self,full_name,roll_no,marks):
        self.name=full_name
        self.roll_no=roll_no
        self.marks=marks

s1=Student("Muhammad Usman Khalil",306356,74)
print("Full Name:",s1.name,"Roll No:",s1.roll_no,"Total Marks:",s1.marks)  

s2=Student("Muhammad Ibrahim Khalil",306357,79)
print("Full Name:",s2.name,"Roll No:",s2.roll_no,"Total Marks:",s2.marks)

class Fruit:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        print("New fruit name:")

fruit1=Fruit("Apple","red")
print("Fruit Name",fruit1.name)
print("Fruit color:",fruit1.color)  

fruit2=Fruit("Banana","Yellow")
print("Fruit Name:",fruit2.name)
print("Fruit color:",fruit2.color)

class Student:
    def __init__(self,GR_no,name,father_name,roll_No,marks):
        self.GR_No=GR_no
        self.name=name
        self.Father_name=father_name
        self.roll_No=roll_No
        self.marks=marks

s1=Student(2301,"Usman Khalil","Khalil ur Rehman",306356,75)
print("GR No",s1.GR_No,"Name:",s1.name,"Father Name:",s1.Father_name,"Roll No:",s1.roll_No,"Marks:",s1.marks)

#Class & Instance Attributes

class Student:
    college_Name="Govt Isl sci college"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("enter new student in database: ")

s1=Student("usman","84")
print("Name:",s1.name)
print("Marks:",s1.marks) 

print("College Name:",Student.college_Name)

class Student:
    name="Shayan" #Class attribute

    def __init__(self,name,marks):
        self.name=name #Object attribute > Class attribute
        self.marks=marks

s1=Student("Usman",78)
print(s1.name)
print(s1.marks)   

#Methods

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def welcome(self):  #Methods
        print("Welcome Student:", self.name)

    def get_marks(self):  #Methods
        return self.marks    

s1=Student("usman khalil",76)
print(s1.name,s1.marks) 
print(s1.welcome) 

print(s1.get_marks)

#create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print Average

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self): #Method
        sum = 0
        for i in self.marks:
            sum+=i
        print("Name:",self.name,"your avg score is:",sum/3 )        

s1=Student("Usman",[65,87,74])        
s1.get_avg()

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum+=val
        print("Name:",self.name,"Your avg score is:",sum/3)        

s1=Student("Usman",[54,65,87]) 
s1.get_avg()       

#create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print Average

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def avg_marks(self):
        sum = 0
        for i in self.marks:
            sum+=i
        print("Name:",self.name,"your avg score is:",sum/4)        

s1=Student("Usman",[50,50,50,50])
s1.avg_marks()
        
#create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print Average

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def avg(self):
        sum = 0
        for i in self.marks:
            sum+=i
        print("Name:",self.name,"Avg:",sum/3)        

s1=Student("Usman",[10,20,30])  
print(s1.avg)
s1.avg()

s1.name = "Ibrahim"
s1.avg()

#Static Method

class Student:
    def __init__(self,name):
        self.name=name

    @staticmethod    
    def hello():
        print("hello")    

s1=Student("Usman")
print(s1.name)

s2=Student("hello")
print(s2.hello)
s2.hello()

#Abstraction

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("car started: ")

car1=Car()
car1.start()

class Car:
    def __init__(self):
        self.acc=True
        self.brk=True
        self.clutch=True

    def stop(self):
        self.clutch=False
        self.acc=False
        print("Car stopped:") 

car1=Car()
car1.stop()

class Book:
    def __init__(self):
        self.understand=False
        self.write=False

    def start(self):
        self.understand=True
        self.write=True
        print("Succeed")

book1=Book()
book1.start()

#Create account class with 2 attributes balance & account no.
#Create method for debit, credit & printing the balance


class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no

    def debit(self,amount):
        self.balance-=amount
        print('Rs:',amount,"was debited")
        print("Total balance =",self.get_balance())

    def credit(self,amount):
        self.balance+=amount 
        print("Rs:",amount,"was credited")
        print("Total balance =",self.get_balance()) 

    def get_balance(self):
        return self.balance          

acc1=Account(20000,12345)
acc1.debit(1000)
acc1.credit(40000)

class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no

    def debit(self,amount):
        self.balance-=amount
        print("Rs:",amount, "was debited")
        print("Total balance:",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs:",amount,"was credit")
        print("Total balance=",self.get_balance())

    def get_balance(self):
        return self.balance    

acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(4000)

class Account:
    def __init__(self,account_no,amount):
        self.account_no=account_no
        self.amount=amount

    def debit(self,amount):
        self.amount-=amount
        print("Rs=",amount,"was debited")
        print("Total amount",self.get_amount())

    def credit(self,amount):
        self.amount+=amount
        print("Rs=",amount,"was credited")
        print("Total amount=",self.get_amount())  

    def get_amount(self):
        return self.amount          

acc1=Account(20000,12345) 
acc1.debit(1000)        

acc1=Account(12345,50000)  

class Account:
    def __init__(self,acc_no,amount):
        self.acc_no=acc_no
        self.amount=amount

    def debit(self,amount):
        self.amount-=amount
        print("Rs=",amount,"amount was debited")
        print("Total balance=",self.get_balance()) 

    def credit(self,amount):
        self.amount+=amount
        print("Rs=",amount,"amount was credited")
        print("Total balance=",self.get_balance())    

    def get_balance(self):
        return self.get_balance    

acc1=Account(12345,50000) 
acc1.debit(1000)
acc1.credit(2000)

#Delete Keyword

class Student:
    def __init__(self,name):
        self.name=name

s1=Student("usman")
print(s1.name * 5) 

#Private(like) attributes & Methods

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def reset_pass(self):
        print(self.__acc_pass)    

acc1=Account(12345,"asdf")
print(acc1.acc_no)
print(acc1.reset_pass())

class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.__roll_no=roll_no

    def hide_roll_no(self):
        print(self.__roll_no)    

s1=Student("usman",306356) 
print(s1.name)
print(s1.hide_roll_no())

class Fruit:
    def __init__(self,apple,mango):
        self.apple=apple
        self.__mango=mango

    def hide_mango(self):
        print(self.__mango)    

fruit1=Fruit('A',"M")
print(fruit1.apple)
print(fruit1.hide_mango())

#Inheritance

class Car:
    @staticmethod   
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")


class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name 

car1=ToyotaCar("fortune")
car2=ToyotaCar("Carry")
print(car1.name)
print(car2.name)

print(car1.start())
print(car1.stop())

class Student:
    @staticmethod
    def first_name():
        print("First name")
    @staticmethod
    def last_name():
        print("Last name")

class JuniorsStudent(Student):
    def __init__(self,roll_no):
        self.roll_no=roll_no

stu1=JuniorsStudent(306356)
stu2=JuniorsStudent(306357)

print(stu1.roll_no)
print(stu2.roll_no)

print(JuniorsStudent.first_name())
print(JuniorsStudent.last_name())


class Car:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

    class ToyotaCar(Car):
        def __init__(self,brand):
            self.brand=brand

car1=ToyotaCar("Cultus")
car2=ToyotaCar("Civic")

print(car1.start())
print(car1.stop())

print(ToyotaCar.start())
print(ToyotaCar.stop())

#Multi Level Inheritance

class Car:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def run():
        print("car runned")
    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortumer(ToyotaCar):
    def __init__(self,type):
        self.type=type

car1=Fortumer("electric")
car1.start()
car1.run()
car1.stop()
print(Fortumer.run())
print(ToyotaCar.start())

class Student:
    @staticmethod
    def First_name():
        print("first name:")
    @staticmethod
    def Last_name():
        print("Last name:")

class JuniorStudents(Student):
    def __init__(self,roll_no,marks):
        self.roll_no=roll_no
        self.marks=marks

class SeniorStudents(JuniorStudents):
    def __init__(self,college,university):
        self.college=college
        self.university=university

junior1=JuniorStudents(306356,85)
senior1=SeniorStudents("Govt Isl Sci college","Sir Syed university")

print(junior1.First_name())
print(junior1.Last_name())
print(junior1.roll_no,junior1.marks)
print(senior1.First_name())
print(senior1.Last_name())
print(senior1.college)
print(senior1.university)

#Multiple Inheritance

class A:
    varA="welcome to class A"

class B:
    varB="welcome to class B"

class C(A,B):
    varC="welcome to class C"

c1=C()

a1=A()

b1=B()

print(c1.varA)
print(c1.varB)
print(c1.varC)

print(a1.varA)
print(b1.varB)

class Student:
    stu1="welcome to first student"

class JuniorStudent:
    stu2="welcome to second student"

class SeniorStudent(Student,JuniorsStudent):
    stu3="welcome to third student"

senior1=SeniorStudent(306356)
print(senior1.stu1) 
print(senior1.stu3)  

#Super Method

class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name

car1=ToyotaCar("Corolla","Electric")
print(car1.type) 

class Car:
    def __init__(self,name):
        self.name=name

    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self, name,type,brand):
        super().__init__(name)
        self.type=type
        self.brand=brand

car1=ToyotaCar("Civic","Electric car","fortuner")
print(car1.name)

class Car:
    def __init__(self,name,type):
        self.name=name
        self.type=type

    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self, name, type,brand):
        super().__init__(name,type)
        self.brand=brand
        super().start()
        super().stop()

car1=ToyotaCar("Cultus","Electric","Yamaha")
print(car1.name)
print(car1.type) 
print(car1.start())

class Student:
    def __init__(self,name,type):
        self.type=type
        self.name=name

    @staticmethod
    def start():
        print("class started")
    @staticmethod
    def stop():
        print("class stopped")

class ToyotaCar(Car):
    def __init__(self, name, type,brand):
        super().__init__(name, type)
        self.brand=brand  

car1=ToyotaCar("Cultus","Honda","Electric")
print(car1.start())
print(car1.stop())
print(car1.brand)
print(car1.type) 

class Student:
    def __init__(self,name):
        self.name=name

    @staticmethod
    def start():
        print("class started")
    @staticmethod
    def stop():
        print("class stopped")

class JuniorStudent(Student):
    def __init__(self, name,type):
        super().__init__(name)
        self.type=type  

stu1=JuniorStudent("Usman","Intermediate")
print(stu1.start())
print(stu1.stop()) 
print(stu1.name,stu1.type)

class Car:
    def __init__(self,type,brand):
        self.type=type
        self.brand=brand

    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def run():
        print("car runned")
    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self, type, brand,name):
        super().__init__(type,brand)
        self.name=name

car1=ToyotaCar("Electric","Yamaha","Cultus")
print(car1.start()) 
print(car1.stop())
print(car1.run())
print("Car name:",car1.name, "Car brand:", car1.brand, "Car Type:", car1.type) 

#Class Method

class Person:
    name="Ibrahim"

    def changeName(self,name):
        self.name=name

p1=Person()
p1.changeName("Usman")
print(p1.name) 

class Car:
    name="Civic"

    def changeName(self,name):
        self.name=name

car1=Car()
car1.changeName("Corolla")
print(car1.name) 

class Fruit:
    name="Banana"

    def changeName(self,name):
        self.name=name

fruit1=Fruit()
fruit1.changeName("Mango")
print(fruit1.name)

class Student:
    def __init__(self,math,phy,chem):
        self.math=math
        self.phy=phy
        self.chem=chem
        self.percentage=str((self.math + self.phy + self.chem) / 3)

    def calcPercentage(self):
        self.percentage=str((self.math + self.phy + self.chem) / 3)    

stu1=Student(94,75,66) 
print(stu1.percentage) 

stu1.math=80
print(stu1.math)
stu1.calcPercentage()
print(stu1.percentage)

class Student:
    def __init__(self,eng,math,phy,chem):
        self.eng=eng
        self.math=math
        self.phy=phy
        self.chem=chem
        self.per=((self.eng + self.math + self.phy + self.chem) / 4)

    def calcper(self):
        self.per=str((self.eng + self.math +self.phy + self.chem) / 4)   

stu1=Student(74,65,85,59)
print(stu1.per)

stu1.chem=90
print(stu1.chem)
stu1.calcper()
print("Student New Percentage=",stu1.calcper())

#Property Method

class Student:
    def __init__(self,math,chem,phy):
        self.math=math
        self.chem=chem
        self.phy=phy

    @property
    def per(self):
        return str((self.math + self.chem + self.phy) / 3)

stu1=Student(65,89,59)
print("Student Percentage=",stu1.per)  

stu1.chem=59
print("Chemistry Number change=",stu1.chem)
print("Student new Percentage=",stu1.per)

class Fruit:
    def __init__(self,apple,orange):
        self.apple=apple
        self.orange=orange

    @property
    def add(self):
        return str(self.apple + self.orange)  

fruit1=Fruit(65,85)
print(fruit1.add)

fruit1.apple=90
print(fruit1.apple)
print(fruit1.add)

class Student:
    def __init__(self,math,chem,phy):
        self.math=math
        self.chem=chem
        self.phy=phy

    @property
    def per(self):
        return str((self.math + self.chem + self.phy) / 3) 

stu1=Student(75,85,69)
print("Percentage=",stu1.per) 

stu1.math=45
print("Math marks=",stu1.math)
print("new percentage=",stu1.per)

#Polymorphism

class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def showNumber(self):
        print(self.real,"i +",self.imag,"j")

num1=Complex(5,4)
num1.showNumber()   

class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def showNumber(self):
        print(self.real,"i +",self.imag,"j")

    def add(self,num2):
        newReal=self.real + num2.real
        newImaginary=self.imag + num2.imag
        return Complex(newReal,newImaginary)    

num1=Complex(6,9)
num1.showNumber()  

num2=Complex(2,7)
num2.showNumber()

num3=num1.add(num2)
num3.showNumber()

class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def showNumber(self):
        print(self.real,"i+",self.imag,"j") 

    def add(self,num2):
        newReal=self.real + num2.real
        newImag=self.imag + num2.imag
        return Complex(newReal,newImag)    

num1=Complex(5,9)
num1.showNumber()

num2=Complex(3,8)
num2.showNumber()

num3=num1.add(num2)
num3.showNumber()

class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def showNumber(self):
        print(self.real,"i+",self.imag,"j")

    def subtract(self,num2):
        newReal=self.real - num2.real
        newImag=self.imag - num2.imag
        return Complex(newReal,newImag)    

num1=Complex(7,12)
num1.showNumber()

num2=Complex(8,15)
num2.showNumber()

num3=num1.subtract(num2)
num3.showNumber()

class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def showNumber(self):
        print(self.real,"i +",self.imag,"j")

    def Multiply(self,num2):
        newReal=self.real * num2.real
        newImag=self.imag * num2.imag
        return Complex(newReal,newImag)    

num1=Complex(2,4)
num1.showNumber()

num2=Complex(6,8)
num2.showNumber()

num3=num1.Multiply(num2)
num3.showNumber()

class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def showNumber(self):
        print(self.real,"i *",self.imag,"j")

    def Multiply(self,num2):
        newReal=self.real * num2.real
        newImag=self.imag * num2.imag
        return Complex(newReal,newImag)

com1=Complex(5,7)
com1.showNumber()

com2=Complex(10,14)
com2.showNumber()

com3=num1.Multiply(num2)
com3.showNumber()

class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def showNumber(self):
        print(self.real,"i+",self.imag,"j") 

    def __add__(self,num2):
        newReal=self.real + num2.real
        newImag=self.imag + num2.imag
        return Complex(newReal,newImag)    

num1=Complex(5,9)
num1.showNumber()

num2=Complex(3,8)
num2.showNumber()

num3=num1 + num2
num3.showNumber()

class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def showNumber(self):
        print(self.real,"i+",self.imag,"j")

    def  subtract(self,num2):
        newReal=self.real - num2.real
        newImag=self.imag - num2.imag
        return Complex(newReal,newImag)    

num1=Complex(7,12)
num1.showNumber()

num2=Complex(8,15)
num2.showNumber()

num3=num1.subtract(num2)
num3.showNumber()

#Define a circle class to create a circle with radius r using constructor.
#Define an area() method of the class which calculate the area of circle.
#Define an perimeter() method of the class which allows to calculate perimeter of circle

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return (22/7) * self.radius **2

    def perimeter(self):
        return 2 * (22/7) * self.radius

c1=Circle(25)
print("Area of Circle =",c1.area())
print("Perimeter of Circle =",c1.perimeter())     

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return (22/7)* self.radius**2

    def perimeter(self):
        return 2 * (22/7) * self.radius

c1=Circle(10)
print(c1.area())
print(c1.perimeter())  


#Define a Employee class with attributes role, department & salary. This class also a showDetail() Method.
#Create an Engineer class that inherits properties from Employee & has additional attributes: name & age

class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetails(self):
        print("role =",self.role)
        print("Dept =",self.dept)
        print("salary =",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","60000")

engg1=Engineer("Bilgates",56)
engg1.showDetails()

#Define a Employee class with attributes role, department & salary. This class also a showDetail() Method.
#Create an Engineer class that inherits properties from Employee & has additional attributes: name & age

class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetails(self):
        print("role =",self.role)
        print("dept =",self.dept)
        print("salary =",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","60000") 

engg1=Engineer("Bilgates",55)
engg1.showDetails()

class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetails(self):
        print("role =",self.role)
        print("dept =",self.dept)
        print("salary =",self.salary)  

class Engineer(Employee):
    def __init__(self, role, dept, salary,name,age):
        super().__init__(role, dept, salary)
        self.name=name
        self.age=age

engg1=Engineer("Finance","IT",50000,"Elon Musk",55)
print("Name:",engg1.name,"Age =",engg1.age,"Department:",engg1.dept,"Role:",engg1.role,"salary:",engg1.salary)  

#Define a Employee class with attributes role, department & salary. This class also a showDetail() Method.
#Create an Engineer class that inherits properties from Employee & has additional attributes: name & age


class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetails(self):
        print("role =",self.role)
        print("dept =",self.dept)
        print("salary =",self.salary)

class Engineer(Employee):
    def __init__(self, role, dept, salary,name,age):
        super().__init__(role, dept, salary)
        self.name=name
        self.age=age

engg1=Engineer("Powerbi","IT",50000,"Bilgates",50)
print(engg1.name,engg1.dept,engg1.role,engg1.age,engg1.salary)


#Create a class called order which stores item & its price.
#Use dunder function__gt__() to convey that:
#order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,odr2):
        return self.price > odr2.price    
    
odr1=Order("Juice",30)
odr2=Order("chips",20)

print("Order 1 item =",odr1.item,"order 1 price =",odr1.price)
print("Order 2 item =",odr2.item,"Order 2 price",odr2.price)

print(odr1 > odr2)

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,order1):
        return self.price > order1.price   

order1=Order("Choclates",25)
order2=Order("Ice cream",150)

print(order1 > order2)

#Miniproject

import random

randNum=random.randint(1,5)

print(randNum)

import random

randNum=random.randint(1,10)
print(randNum)

import random
randNum=random.randint(1,8)
print(randNum)


import string
print(string.ascii_letters)

import string
print(string.ascii_letters)

import string
print(type(string.ascii_letters))

import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)

import random
print(random.choice("Usman"))

import random
print(random.choice("Ibrahim"))

import random
print(random.choice("Samra Imran"))

import string
charValue = string.ascii_letters + string.digits + string.punctuation
print(charValue)

import string
charValue = string.ascii_letters + string.digits + string.punctuation
print(random.choice(charValue))

pass_len = 10
charValue = string.ascii_letters + string.digits + string.punctuation

password =""
for i in range(pass_len):
    print(random.choice(charValue))

pass_len = 10
charValue = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password+=random.choice(charValue)
print("your password is :",password)   

pass_len = 20
charvalue = string.ascii_letters + string.digits

password = ""
for i in range(pass_len):
    password+=random.choice(charValue)
print("your password is :",password)   

pass_len = 15
chavalue = string.ascii_lowercase + string.digits
password = ""
for i in range(pass_len):
    password+=random.choice(chavalue)
print("your password is :",password)

pass_len = 15
charvalue = string.ascii_uppercase + string.digits

password = [random.choice(charvalue) for i in range(pass_len)]
print(password)

#List comprehention [function for i in range()]

password_length = 20
charactervalue = string.ascii_letters + string.digits + string.punctuation

password = "".join([random.choice(charactervalue) for i in range(password_length)])
print(password)











    

    










































































































print(order1.item,order1.price)
print(order2.item,order2.price)
































































































































































 











































































































































































































































































    

















































        














































      
        















    

                  



























       


                  













































































































      



    



      














     














   
    











































































































































            










































































