
class Student:
    name="Usman Khalil"
s1=Student()
print(s1.name)

class Student:
    name="umar khalil"
s1=Student()
print("Name :",s1.name)

class Bank:
    bank_name = "Meezan Bank"
b1=Bank()
print("Bank Name :",b1.bank_name)

class Car:
    color = "white"
    brand="mercedies"
car1=Car()
print("Car color :",car1.color)
print("Brand :",car1.brand)

class College:
    College_name="isl sci college"
    name="Muhammad Usman Khalil"
c1=College()
print("College_Name :",c1.College_name)
print("Name :",c1.name)

class Bank:
    bank_name="Microfinance Bank"
    Emp_Name="Hamza Jamal"
    Salary=35000
    Bonus="Six Months"
b1=Bank()
print("Bank Name :",b1.bank_name)
print("Employee Name :",b1.Emp_Name)
print("Salary :",b1.Salary)
print("Bonus :",b1.Bonus)

class Student:
    name="Muhammad Usman Khalil"
    def __init__(self):
        print("adding new student in database...")
s1=Student()

class Car:
    brand="Mercedies"
    def __init__(self):
        print("adding new model in new database...")
c1=Car()

class College:
    College_name="isl science college"
    def __init__(self):
        print("adding new data of student information :")
c1=College()

class University:
    uni_name="karachi university"
    def __init__(self):
        print("adding new information in new data :")
u1=University()

class Student:
    name="Usman Khalil"
    def __init__(self):
        print(self)
s1=Student()

class Student:
    def __init__(self,name):
        self.name=name
s1=Student("Usman")
print("Full Name :",s1.name)        

class Student:
    def __init__(self,name):
        self.name=name
s1=Student("aYESHA mALIK")
s2=Student("Ahsan Shamim")
print(s1.name)
print(s2.name)

class College:
    College_name="Isl sci college"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
c1=College("Usman Khalil",85)
c2=College("Umar Khalil",76)
print(c1.name)
print(c1.marks)
print(c2.name)
print(c2.marks)

class Car:
    def __init__(self,name,type):
        self.name=name
        self.type=type
c1=Car("cultus","Mercedies")
print("Name :",c1.name, "Type :",c1.type)        

class Student:
    def __init__(self,name,roll_no,marks,grade,result):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        self.grade=grade
        self.result=result
s1=Student("Usman Khalil",123,87,"A","Pass")
print("Full Name :",s1.name)
print("Roll No :",s1.roll_no)
print("Marks :",s1.marks)
print("Grade :",s1.grade)
print("Result :",s1.result)
s2=Student("Umar Khalil",234,76,"B","Promoted")
print("Full Name :",s2.name)
print("Roll No :",s2.roll_no)
print("Marks :",s2.marks)
print("Grade :",s2.grade)
print("Result :",s2.result)

#Class and Instance Attributes
class Student:
    College_name = "Islamia science college"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
s1=Student("Usman Khalil",123)
print(s1.name, s1.roll_no)
s2=Student("Umar Khalil",345)
print(s2.name,s2.roll_no)
print(s1.College_name)
print(s2.College_name)
print(Student.College_name)


class University:
    name="ku"
    def __init__(self,roll_no,result):
        self.roll_no=roll_no
        self.result=result
u1=University(123,"pass")
print(u1.roll_no,u1.result)
print(u1.name)
print(University.name)

class Student:
    name="Bob"
    def __init__(self,name):
        self.name=name
s1=Student("Usman")
print("Name :",s1.name)
print(Student.name)

#Methods
class Student:
    def __init__(self,name):
        self.name=name
    def welcome(self):
        print("welcome student :",self.name)    
s1=Student("kiran malik")        
s1.welcome()

class Student:
    def welcome(self):
        print("welcome student :")
s1.welcome()      

class Student:
    College_name="sir syed college"
    def __init__(self,name,result):
        self.name=name
        self.result=result
    def welcome(self):
        print("welcome student :",self.name, "Result :",self.result)    
s1=Student("karan sharma","pass")
print("Name :",s1.name, "Result :",s1.result)
print("Name of college :",s1.College_name, "Name of college :", Student.College_name)    
s1.welcome()


class Car:
    brand="suzuki"
    def __init__(self,name):
        self.name=name
    def start(self):
        print("car started,","car name :",self.name) 
    def stop(self):
        print("car stopped.")       
c1=Car("Cultus")
print("Car Name :",c1.name)
print("Brand :",c1.brand, "brand :",Car.brand)    
c1.start()    
c1.stop()


class Student:
    College_name="sir syed college"
    def __init__(self,roll_no,name):
        self.roll_no=roll_no
        self.name=name
    def welcome(self):
        print("welcome student :",self.name)
    def result(self):
        print("result : pass","roll no :",self.roll_no,self.name)        
s1=Student(123,"usman khalil")
print("roll no :",s1.roll_no, "Name :",s1.name)
print("Name of college :",s1.College_name, "name of college :",Student.College_name)        
s1.welcome()
s1.result()

class Computer:
    name="laptop"
    def __init__(self,id,password):
        self.id=id
        self.password=password
    def keyboard(self):
        print("keyboard typing :","Password :",self.password)
    def mouse(self):
        print("Mouse draging :","ID :",self.id)        
c1=Computer("abc",2468)
print("Name :",c1.name, "name :",Computer.name)
print("ID :",c1.id, "Password :",c1.password)        
c1.keyboard()
c1.mouse()

class Student:
    College_name="sir syed"
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def welcome(self):
        print("welcome student :","Name :",self.name)
    def get_marks(self):
        return self.marks        
s1=Student("usman khalil",2345,89)
print("Name :",s1.name, "Roll No :",s1.roll_no, "Marks :",s1.marks)        
print("Marks :",s1.get_marks())

class Student:
    College_name="city college morning"
    def __init__(self,roll_no,name):
        self.roll_no=roll_no
        self.name=name
    def get_name(self):
        return self.get_name
s1=Student(2456,"usman khalil")        
print("college name :",s1.College_name, "college name :",Student.College_name)
print("roll no :",s1.roll_no, "Name :",s1.name)
print(s1.get_name())

class Student:
    College_name="dj sindh college"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def welcome(self):
        print("welcome student",self.name)
    def get_marks(self):
        return self.get_marks     
s1=Student("usman khalil",87)
s1.welcome()
print(s1.name, s1.marks)       
s1.get_marks()

#Create student class that takes name & marks of 3 subjects as arguments in constructor.
#Then create a method to print the average?

class Student:
    def __init__(self,name, marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name, "your avg score is :", sum/3)        
s1=Student("Usman Khalil",[87,97,54])  
s1.get_avg()      
print(s1.get_avg())

s1.name="asma khalil"
s1.get_avg()

#Create student class that takes name & marks of 4  subjects as arguments in constructor.
#Then create a method to print the average?
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Name :",self.name, "Your avg score is :", sum/4)        
s1=Student("Usman Khalil",[34,56,78,87])
print("Name :",s1.name)
print("Marks :",s1.marks)        
s1.get_avg()

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Name :",self.name, "your average score is =",sum/4)    
s1=Student("Usman Khalil",[45,34,76,98])
print("Name :",s1.name, "Marks :",s1.marks) 
s1.get_avg()       

class Car:
    def __init__(self,name,brand,price):
        self.name=name
        self.brand=brand
        self.price=price
    def get_avg(self):
        sum = 0
        for val in self.price:
            sum+=val
        print("Name of Car :",c1.name, "Avg price of car =",round(sum/3),2)   
c1=Car("cultus","mercedies",[1000000,15000000,25000000])
print("Name of Car :",c1.name, "Car Brand :",c1.brand)
print("Car Avg Price :",c1.price)    
c1.get_avg()    

class Furniture:
    def __init__(self,name,brand,price):
        self.name=name
        self.brand=brand
        self.price=price
    def get_mean(self):
        sum = 0
        for val in self.price:
            sum+=val
        print("Names :",f1.name, "avg price is =",round(sum/4),0)        
f1=Furniture(["sofa","bed","table","chair"],"Uniform",[23000,12000,45000,55000])
print("Names :",f1.name) 
print("Brand :",f1.brand)
print("Price :",f1.price)       
f1.get_mean()

#Abtraction
class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.clutch=True
        self.acc=True
        print("car startedd...")
car1=Car()
car1.start()

class Student:
    def __init__(self):
        self.roll_no=False
        self.name=False
        self.marks=False
    def result(self):
        self.roll_no=True
        self.result=True
        print("result announced...")
s1=Student()
s1.result()

class Bank:
    def __init__(self):
        self.acc_no=False
        self.pas=False
        self.user=False
    def privacy(self):
        self.user=True
        self.pas=True
        print("user acc_no private...")
b1=Bank()
b1.privacy()            

class Furniture:
    def __init__(self):
        self.chair=False
        self.table=False
        self.bed=False
    def decorate(self):
        self.chair=True
        self.table=True
        print("Home delivered...")
f1=Furniture()
f1.decorate()

class Laptop:
    def __init__(self):
        self.mouse=False
        self.keyboard=False
        self.user=False
    def work(self):
        self.mouse=True
        self.user=True
        print("ability to work")
l1=Laptop()
l1.work()    

class Saylani:
    def __init__(self):
        self.course=False
        self.test=False
        self.online=False
    def job(self):
        self.course=True
        self.online=True
        print("Job achieved...")
say1=Saylani()
say1.job()

class Account:
    def __init__(self,acc_no,acc_bal):
        self.acc_no=acc_no
        self.acc_bal=acc_bal
    def debit(self, amount):
        self.acc_bal -= amount
        print("Rs-",amount,"was debited")
        print("total balance =",self.get_balance())
    def credit(self, amount):
        self.acc_bal += amount
        print("Rs-",amount, "was credited")
        print("total balance =",self.get_balance())
    def get_balance(self):
        return self.acc_bal          
acc1=Account(123,25000)  
print("Account no =",acc1.acc_no)
print("Balance =",acc1.acc_bal)   
acc1.debit(1000)

class Account:
    def __init__(self, acc_no, acc_bal):
        self.acc_no = acc_no
        self.acc_bal = acc_bal
    def debit(self, amount):
        self.acc_bal -= amount
        print("Rs-", amount, "was debited.")
        print("total balance =", self.get_balance())
    def credit(self, amount):
        self.acc_bal += amount
        print("Rs-", amount, "was credited.")
        print("total balance =",self.get_balance())
    def get_balance(self):
        return self.acc_bal            
acc1=Account(3456,25000) 
print(acc1.acc_no)
print(acc1.acc_bal)
acc1.debit(2000)
acc1.credit(3000)
acc1.credit(55000)

class Student:
    def __init__(self, name):
        self.name=name
s1=Student("Usman")
print(s1.name)

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass
    def reset_pass(self):
        print(self.__acc_pass)    
acc1=Account(12345,"abcde")
print(acc1.acc_no)
print(acc1.reset_pass())           

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass
    def reset_pass(self):
        print(self.__acc_pass)    
acc1=Account(1234, "jdhfg")
print(acc1.acc_no)
print(acc1.reset_pass())

class Fruits:
    def __init__(self, name, price):
        self.name=name
        self.__price=price
    def remove(self):
        print(self.__price)    
fru1=Fruits("banana",100)
print(fru1.name)
print(fru1.remove())

class Laptop:
    def __init__(self,brand,quality):
        self.brand=brand
        self.__quality=quality
    def delete(self):
        print(self.__quality)    
l1=Laptop("dell","25%")
print(l1.brand)
print(l1.delete())

class Student:
    def __init__(self, roll_no, marks, grade, result):
        self.roll_no=roll_no
        self.__marks=marks
        self.__grade=grade
        self.result=result
    def reset_marks(self):
        print(self.__marks)
    def reset_grade(self):
        print(self.__grade)    
s1=Student(2345,65,"B","pass")
print(s1.roll_no)
print(s1.reset_marks())
print(s1.reset_grade())
print(s1.result)        

class Car:
    def __init__(self, name, brand, price):
        self.name=name
        self.__brand=brand
        self.__price=price
    def reset_brand(self):
        print(self.__brand)
    def reset_price(self):
        print(self.__price)      
car1=Car("cultus","mercedies",25000)   
print(car1.name)
car1.reset_brand()
car1.reset_price()    

class College:
    def __init__(self, roll_noo, attandance, marks, result):
        self.roll_no=roll_noo
        self.__attandance=attandance
        self.marks=marks
        self.__result=result
    def reset_attandance(self):
        print(self.__attandance)
    def reset_result(self):
        print(self.__result)        
col1=College(123,"70%",78,"pass")
print(col1.roll_no)
col1.reset_attandance()
print(col1.marks)
col1.reset_result()       

#Inheritance
class Car:
    @staticmethod
    def start():
        print("car started.")
    @staticmethod
    def stop():
        print("car stopped.")
class ToyotaCar(Car):
    def __init__(self, name, brand):
        self.name=name
        self.brand=brand
car1=ToyotaCar("cultus","diesel")
print(car1.name)
print(car1.brand)
car1.start()
car1.stop()                   

class Car:
    def start(self):
        print("car started.")
    def stop(self):
        print("car stopped.")
class Toyotacar(Car):
    def __init__(self, name, brand):
        self.name=name
        self.brand=brand
car1=ToyotaCar("civic","prios")
print(car1.name)
print(car1.brand) 
car1.start()
car1.stop()

class Student:
    @staticmethod
    def roll_no():
        print("give rollno.")
    def give_name(self):
        print("Name given.")
class Junior(Student):
    def __init__(self, marks, grade):
        self.marks=marks
        self.grade=grade
class Senior(Junior):
    def __init__(self, result, gpa):
        self.result=result
        self.gpa=gpa
j1=Junior(87,"A+")           
s1=Senior("pass",3.24)             
print(j1.marks)
print(j1.grade)
print(s1.result)
print(s1.gpa)
j1.roll_no()
j1.give_name()
s1.roll_no()
s1.give_name()

class School:
    def roll_no(self):
        print("give rollno")
    def name(self):
        print("name given")
    def classes(self):
        print("class given.")
class College(School):
    def __init__(self, books, exams):
        self.books=books
        self.exams=exams
c1=College("maths", "final year")
class University(College):
    def __init__(self, Notes, result):
        self.Notes=Notes
        self.result=result
u1=University("practical centre","promote")
class Job(University):
    def __init__(self, salary, bonus):
        self.salary=salary
        self.bonus=bonus
j1=Job(23000,2000) 
print(c1.books)
print(c1.exams)
print(u1.Notes)
print(u1.result)
print(j1.salary)
print(j1.bonus)   
c1.roll_no()
c1.name()
c1.classes()
u1.roll_no()                           
u1.name()
u1.classes()
j1.roll_no()
j1.name()
j1.classes()

class Car:
    def start(self):
        print("car started.")
    def stop(self):
        print("car stopped.")
class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name=name
        self.type=type
class Fortuner(ToyotaCar):
    def __init__(self, brand, price):
        self.brand=brand
        self.price=price
car1=Fortuner("mercedies", 100000)
car1=ToyotaCar("cultus", "diesel")
car1.start()
car1.stop()
print(car1.name)
print(car1.type)

#Super Method
class Car:
    def __init__(self, type):
        self.type = type        
    @staticmethod
    def start():
        print("car started.")
    @staticmethod
    def stop():
        print("car stopped")
class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
car1=ToyotaCar("cultus", "Electric")
print(car1.type)                                
c1=Car("suzuki")
print(c1.type)   

#Class Method
class Person:
    name = "Anoynemous"
    @classmethod
    def changeName(cls, name):
        cls.name=name
p1=Person()
p1.changeName("Usman Khalil")
print(p1.name)
print(Person.name)

class Person:
    name = "Usman Khalil"
    @classmethod
    def changeName(cls, name):
        cls.name = name
p1=Person()
p1.changeName("Ibrahim khalil")
print(p1.name)
print(Person.name)

class Car:
    name = "civic"
    @classmethod
    def changeName(cls, name):
        cls.name=name
p1=Person()
p1.changeName("Electric")
print(p1.name)
print(Person.name)

class Person:
    name = "Usman Khalil"
    def changeName(self, name):
        self.name=name
p1=Person()
p1.changeName("Ayesha Malik")
print(p1.name)
print(Person.name)

class Person:
    name = "usman Khalil"
    def changeName(self, name):
        self.name=name
p1=Person()
p1.changeName("Ibrahim Khalil")
print(p1.name)
print(Person.name)

class Car:
    name = "cultus"
    def changeName(self, name):
        self.name=name
c1=Car()
c1.changeName("civic corolla")
print(c1.name)
print(Car.name)

class Computer:
    name = "HP"
    def changeName(self, name):
        self.name=name
co1=Computer()
co1.changeName("DEL")
print(co1.name)
print(Computer.name)

class Person:
    name = "Usman Khalil"
    def changeName(self, name):
        self.name=name
p1=Person()
p1.changeName("Ibrahim Khalil")
print(p1.name)
print(Person.name)

class Person:
    name = "Usman Khalil"
    def changeName(self, name):
        self.__class__.name="Ibrahim Khalil"
p1=Person()
print(p1.name)
print(Person.name)

class Person:
    name = "asma"
    def changeName(self, name):
        self.__class__.name="Usman"
p1=Person()
print(p1.name)
print(Person.name)

class Car:
    name = "corolla"
    def changeName(self, name):
        self.name=name
c1=Car()
c1.changeName("civic")
print(c1.name)
print(Car.name)        

class Car:
    name = "corolla"
    def changeName(self, name):
        self.__class__.name="civic"
c1=Car()
print(c1.name)
print(Car.name)        

class Person:
    name = "Usman Khalil"
    def changeName(self, name):
        self.name=name
p1=Person()
p1.changeName("Ibrahim Khalil")
print(p1.name)
print(Person.name)

class Person:
    name = "Usman Khalil"
    def changeName(self, name):
        self.__class__.name = "ibrahim khalil"
p1=Person()
print(p1.name)
print(Person.name)        

class Fruits:
    name="mango"
    def changeName(self, name):
        self.__class__.name = "orange"
f1=Fruits()
print(f1.name)
print(Fruits.name)

class Computer:
    name =  "lenovo"
    company = "PC"
    def changeName(self, name, company):
        self.__class__.name = "dell"
        self.__class__.company = "HP"
c1=Computer()
print(c1.name)
print(Computer.name)
print(c1.company)
print(Computer.company)

class Student:
    name = "roll no"
    marks = "Numbers"
    def changeName(self, name, marks):
        self.__class__.name = "Gr No"
        self.__class__.marks = "alphabets"
s1=Student()
print(s1.name)
print(Student.name)
print(s1.marks)
print(Student.marks)    

class House:
    name = "table"
    name1 = "chair"
    def changeName(self, name, name1):
        self.__class__.name="anc"
        self.__class__.name1="parcal"
h1=House()
print(h1.name)
print(House.name)
print(h1.name1)
print(House.name1)

class Laptop:
    name = "HP"
    def changeName(self, name):
        self.name=name
l1=Laptop()
l1.changeName("DEL")
print(l1.name)
print(Laptop.name)

class Laptop:
    name = "HP"
    def changeName(self, name):
        self.__class__.name="DEL"
l1=Laptop()
print(l1.name)
print(Laptop.name)

class Student:
    name = "Usman Khalil"
    roll_no = 12345
    marks = 67
    grade = "B"
    def changeName(self, name, roll_no, marks, grade):
        self.__class__.name="Umar Khalil"
        self.__class__.roll_no=6789
        self.__class__.marks=78
        self.__class__.grade="A"
s1=Student()
print(s1.name)
print(Student.name)
print(s1.roll_no)
print(Student.roll_no)
print(s1.marks)
print(Student.marks)
print(s1.grade)
print(Student.grade)

class Student:
    def __init__(self, phy, chem, math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage = (self.phy + self.chem + self.math) / 3
    def calcpercentage(self):
        self.percentage = (self.phy + self.chem + self.math) / 3    
s1=Student(56, 67, 87)
print(s1.phy)
print(s1.chem)
print(s1.math)
print(s1.percentage)        
s1.phy = 98
print(s1.phy)
print(s1.calcpercentage())
print(s1.percentage)

class Student:
    def __init__(self, phy, urdu, isl, chem):
        self.phy=phy
        self.urdu=urdu
        self.isl=isl
        self.chem=chem
        self.percentage = str((self.phy + self.urdu + self.isl + self.chem) / 4) + "%"
    def calcpercentage(self):
        self.percentage = str((self.phy + self.urdu + self.isl + self.chem) / 4) + "%"    
stu1=Student(67,65,78,89)
print(stu1.percentage)
stu1.chem = 76
print(stu1.calcpercentage())
print(stu1.percentage)

class Student:
    def __init__(self, phy, chem, math, eng, pst):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.eng=eng
        self.pst=pst
        self.percentage = str((self.phy + self.chem + self.math + self.eng + self.pst) / 5) + "%"
    def calcpercentage(self):
        self.percentage = str((self.phy + self.chem + self.math + self.eng + self.pst) / 5) + "%"    
stu1=Student(45,67,78,88,65)
print(stu1.percentage) 
stu1.phy = 99
stu1.eng = 70
print(stu1.eng)
print(stu1.phy)
print(stu1.calcpercentage())
print(stu1.percentage)       

#Second Method
#Property Decorator

class Student:
    def __init__(self, phy, chem, math):
        self.phy=phy
        self.chem=chem
        self.math=math
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"    
s1=Student(67,78,88)  
print(s1.percentage)
s1.math = 56
print(s1.percentage)      

class Car:
    def __init__(self, cultus, civic, corolla):
        self.cultus=cultus
        self.civic=civic
        self.corolla=corolla
    @property
    def percentage(self):
        return str((self.cultus + self.civic + self.corolla) / 3) + "%"    
c1=Car(250000, 1000000, 4560000)
print(c1.percentage)
c1.civic = 340000
print(c1.percentage)

class Student:
    def __init__(self, phy, chem, math, eng, pst, isl):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.eng=eng
        self.pst=pst
        self.isl=isl
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math + self.eng + self.pst + self.isl) / 6) + "%"    
s1=Student(25,35,40,45,50,60)
print(s1.percentage)
s1.phy=56
s1.chem = 45
print(s1.percentage)
s1.isl = 87
print(s1.percentage)
s1.math = 70
print(s1.percentage)
s1.eng = 90
s1.phy = 78
print(s1.percentage)

#Polymorphism
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def shownumber(self):
        print(self.real, "i +", self.imag, "j")
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImag = self.imag + num2.imag
        return Complex(newReal, newImag)      
num1 = Complex(4,7)
num1.shownumber()
num2 = Complex(6,8)
num2.shownumber()

num3 = num1 + num2
num3.shownumber()

class Complex:
    def __init__(self, real, imag):
        self.real=real
        self.imag=imag
    def showNumber(self):
        print(self.real,"I +",self.imag,"j")
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImag = self.imag + num2.imag
        return Complex(newReal, newImag)    
num1=Complex(4,8)
num1.showNumber()
num2=Complex(12,9)
num2.showNumber()            
num3=num1 + num2
num3.showNumber()

class Complex:
    def __init__(self, real, imag):
        self.real=real
        self.imag=imag
    def showNumber(self):
        print(self.real,"i +",self.imag,"j")
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImag = self.imag - num2.imag
        return Complex(newReal, newImag)    
num1=Complex(5,7)
num1.showNumber()
num2=Complex(2,3)
num2.showNumber()
num3 = num1 - num2
num3.showNumber()

class Complex:
    def __init__(self, real, imag):
        self.real=real
        self.imag=imag
    def showNumber(self):
        print(self.real,"i *",self.imag,"j")
    def __mul__(self, num2):
        newReal= self.real * num2.real
        newImag=self.imag * num2.imag  
        return Complex(newReal, newImag)
num1=Complex(3,5)
num1.showNumber()
num2=Complex(4,7)
num2.showNumber()  
num3=num1 * num2
num3.showNumber()

class Complex:
    def __init__(self, real, imag):
        self.real=real
        self.imag=imag
    def showNumber(self):
        print(self.real,"i +",self.imag,"j")
    def __truediv__(self, num2):
        newReal=self.real / num2.real
        newImag=self.imag / num2.imag
        return Complex(newReal, newImag)    
num1=Complex(15,25)
num1.showNumber()
num2=Complex(3,5)
num2.showNumber()  
num3=num1 / num2
num3.showNumber()          












































































































































































































































































































































































































