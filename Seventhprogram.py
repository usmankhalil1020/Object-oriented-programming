class Student:
    def __init__(self,name):
        self.name=name

s1=Student("usman")
print(s1.name)

class Account:
    def __init__(self,account_no,account_pass):
        self.account_no=account_no
        self.account_pass=account_pass

acc1=Account(12345,"asdf")
print(acc1.account_no)
print(acc1.account_pass) 

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1=Account(1234,"asdf")

print(acc1.acc_no)
print(acc1.reset_pass())

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1=Account(2325,"lkik")

print(acc1.acc_no)
print(acc1.reset_pass())

class Student:
    def __init__(self,acc_name,pass_no):
        self.acc_name=acc_name
        self.__pass_no=pass_no

    def reset_pass(self):
        print(self.__pass_no)

acc1=Account("usman",3654)
print(acc1.reset_pass()) 

###

class Person:
    __name="usman"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1=Person()
print(p1.welcome())

#Inheritance single inheritance

class Car:
    @staticmethod
    def start():
        print("car started:")
    @staticmethod    
    def stop():
        print("car stopped:")

class ToyotaCar(Car): #Inheritance
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("Cultus")
car2=ToyotaCar("Civic")

print(car1.start())

class Car:
    color="white"
    @staticmethod
    def start():
        print("Car Started:")
    @staticmethod    
    def stop():
        print("Car stopped:")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("Cultus")
car1=ToyotaCar("Corolla")                    

print(car1.color)
print(car1.start())
print(car1.stop())

class Car:
    color="black"
    @staticmethod
    def start():
        print("Car started:")
    @staticmethod
    def stop():
        print("Car stopped:")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("Civic")
car1=ToyotaCar("Corolla")

print(car1.color)
print(car1.start())
print(car1.stop())

class Student:
    @staticmethod
    def name():
        print("name given:")
    @staticmethod
    def marks():
        print("marks given:")

class seniorStudent(Student):
    def __init__(self,name):
        self.name=name

stu1=seniorStudent("usman")
stu1=seniorStudent("ibrahim")

print(stu1.name)
print(stu1.marks())

class Student:
    @staticmethod
    def name():
        print("name given:")
    @staticmethod
    def marks():
        print("marks given:")

class juniorStudent(Student):
    def __init__(self,name):
        self.name=name

Stu1=juniorStudent("ibrahim")
stu1=juniorStudent("khalil")

print(stu1.name)
print(stu1.marks())

class Car:
    @staticmethod
    def start():
        print("car started:")

    @staticmethod
    def stop():
        print("car stopped:")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("Civic")
car1=ToyotaCar("Corolla")

print(car1.start())
print(car1.stop())

class Car:
    @staticmethod
    def start():
        print("car started:")
    @staticmethod
    def stop():
        print("car stopped:")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("Civic")
car1=ToyotaCar("Corolla")

print(car1.start())
print(car1.stop())

#Multi_Level Inheritance

class Car():
    @staticmethod
    def start():
        print("car started:")
    @staticmethod
    def stop():
        print("car stopped:")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand

class Furniture(ToyotaCar):
    def __init__(self,type):
        self.type=type  

car1=Furniture("Electric")
car1.stop
car1.start

class Student:
    @staticmethod
    def name():
        print("given name:")
    @staticmethod
    def marks():
        print("Total marks:")

class JuniorStudent(Student):
    def __init__(self,roll_no):
        self.roll_no=roll_no

class SeniorStudent(JuniorStudent):
    def __init__(self,CNIC_no):
        self.CNIC_no=CNIC_no

stu1=SeniorStudent("Expert")
stu1.marks()
stu1.name()

#Multiple Inheritance

class A:
    varA="welcome to class A:"
    
class B:
    varB="welcome to class B:"

class C(A,B):
    varC="welcome to class C:"

C1=C()

print(C1.varC)
print(C1.varB)
print(C1.varA)

class A:
    varA="welcome to class A:"

class B:
    varB="welcome to class B:"

class C:
    varC="welcome to class C:"

class D(A,B,C):
    varD="welcome to class D:"

D1=D()

print(D1.varA)
print(D1.varB)
print(D1.varC)
print(D1.varD)

#Super Method

class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started:")

    @staticmethod
    def stop():
        print("car stopped:")

class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name=name 
        super().__init__(type)
        super().start()

car1=ToyotaCar("Cultus","electric")
print(car1.type)

class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started:")
    @staticmethod
    def stop():
        print("car stopped:")

class Toyota(Car):
    def __init__(self,type,name):
        super().__init__(type)
        self.name=name
        super().start()

car1=Toyota("Cultus","electric")
print(car1.type)

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
    def __init__(self, type,name):
        super().__init__(type)
        self.name=name
        super().start()
        super().stop()

car1=ToyotaCar("Civic","electric")
print(car1.type)

class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class Toyota(Car):
    def __init__(self,type,name):
        super().__init__(type)
        self.name=name
        super().start()
        super().stop()

car1=ToyotaCar("Corolla","electric")  
print(car1.type)      

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
        self.name=name
        super().__init__(type)  
        

car1=ToyotaCar("corolla","electric")
print(car1.type) 

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
    def __init__(self,name, type):
        super().__init__(type)
        self.name=name
        super().start()

car1=ToyotaCar("corolla car","electric")
print(car1.type) 

















      


















        













car1=Toyota("Corolla","electric car")
print(car1.type)        



        
                        









































































































            
        













































































    





































