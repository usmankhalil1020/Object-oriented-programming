class Student:
    name = "usman"

s1=Student()
print(s1.name) 

class Student:
    name = "üsman khalil"

s1=Student()
print(s1.name)

class Student:
    name="usman khalil"
    college="govt isl sci college"

s1=Student()
print(s1.name)
print(s1.college) 

class Student:
    name="usman khalil"
    school="azeem school"
    college="govt isl sci college"
    university="university of karachi"

s1=Student()
print(s1.name)
print(s1.school)
print(s1.college)
print(s1.university)

class Student:
    name="usman"

s1=Student()
print(s1.name)

s2=Student()
print(s2.name)

class Car:
    color="blue"

car1=Car()
car2=Car()
car3=Car()

print(car1.color)
print(car2.color)
print(car3.color)

class Car:
    color="white"
    brand="corolla"

car1=Car()
print(car1.color)
print(car1.brand)

#Constructor __init__ function

class Student:
    name="usman"
    def __init__(self):
        print("adding new student in database:")

s1=Student()

class Student:
    name="usman"
    def __init__(self):
        print(self)
        print("adding new student in database: ")

s1=Student()

class Student:
    name="usman"
    def __init__(self):
        print(self)
        print("introduce your self: ")

s1=Student()

class Student:
    name="usman"
    def __init__(self):
        print(self)
        print("Introduction")

s1=Student()  

class Student:
    def __init__(self,fullname):
        self.name=fullname
        print("introduction")

s1=Student("usman")
print(s1.name)

class Student:
    def __init__(self,fullname):
        self.name=fullname

s1=Student("asif raza khan")
print(s1.name)

class Student:
    def __init__(self,fullname):
        self.name=fullname

s1=Student("Muhammad Usman Khalil")
print(s1.name)

class Student:
    def __init__(abcd,fullname):
        abcd.name=fullname

s1=Student("Usman Khalil")
print(s1.name) 

class Student:
    def __init__(self,fullname):
        self.name=fullname
        print("adding new student in database: ")

s1=Student("Usman Khalil")
print(s1.name)

s2=Student("Ibrahim Khalil")
print(s2.name)

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("adding new student in database: ")

s1=Student("Usman Khalil",78)
print(s1.name, s1.marks)

s2=Student("Ibrahim Khalil",89)
print(s2.name, s2.marks)

class Student:
    college_name="isl sci college"
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks 

s1=Student("Usman Khalil",306356,85)
print("Name:",s1.name,"Roll No:",s1.roll_no,"Total Marks:",s1.marks)

s2=Student("Ibrahim Khalil",306357,88)
print("Name:",s2.name,"Roll No:",s2.roll_no,"Total Marks:",s2.marks)

print(s1.college_name)
print(s2.college_name)

class Student:
    college_name="Isl sci college"
    name="Alaska" #class attribute

    def __init__(self,name,marks):
        self.name=name #object attribute > class attribute
        self.marks=marks
        print("adding new student in database")

s1=Student("usman",67) 
print(s1.name,s1.marks)

#Methods

class Student:
    college_name="ABC college"
    def __init__(self,names,marks):
        self.name=names
        self.marks=marks

    def welcome(self):
        print("welcome student: ",self.name)

    def get_marks(self):
        return self.marks

s1=Student("usman",78)
s1.welcome()
print(s1.get_marks())


class Student:
    def __init__(self,names,roll_no,marks):
        self.names=names
        self.roll_no=roll_no
        self.marks=marks

    def welcome(self):
        print("welcome student: ",self.names)

    def get_marks(self):
        return self.marks
    
    def get_roll_no(self):
        return self.roll_no

s1=Student("Usman",306356,74)
s1.welcome()
print(s1.get_roll_no())
print(s1.get_marks()) 

class Student:
    def __init__(self,name,roll_no,marks,grade):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        self.grade=grade

    def welcome(self):
        print("welcome Student:",self.name)

    def get_roll_no(self):
        return self.roll_no

    def get_marks(self):
        return self.marks
    
    def get_grade(self):
        return self.grade
    
s1=Student("usman",306547,76,"B")
s1.welcome()
print(s1.get_roll_no())
print(s1.get_marks())    
print(s1.get_grade()) 

class Student:
    def __init__(self,name,father_name,university,roll_no,marks,grade):
        self.name=name
        self.father_name=father_name
        self.university=university
        self.roll_no=roll_no
        self.marks=marks
        self.grade=grade

    def welcome(self):
        print("welcome student:",self.name)

    def get_father_name(self):
        print("Father Name:",self.father_name)

    def get_university(self):
        return self.university    

    def get_roll_no(self):
        return self.roll_no

    def get_marks(self):
        return self.marks

    def get_grade(self):
        return self.grade

s1=Student("Usman Khalil","Khalil ur Rehman","Karachi University",306356,74,"A")
s1.welcome()
print(s1.get_father_name())
print(s1.get_university())
print(s1.get_roll_no())
print(s1.get_marks())
print(s1.get_grade())

class Student:
    def __init__(self,name,GR_No,father_name,roll_no,marks,grade):
        self.GR_No=GR_No
        self.name=name
        self.father_name=father_name
        self.roll_no=roll_no
        self.marks=marks
        self.grade=grade

    def get_GR_No(self):
        return self.GR_No    

    def welcome(self):
        print("welcome Student:",self.name)   

    def get_father_name(self):
        return self.father_name    

    def get_roll_n0(self):
        return self.roll_no

    def get_marks(self):
        return self.marks

    def get_grade(self):
        return self.grade
    

s1=Student("Usman Khalil",1105,"Khalil ur Rehman",306356,65,"B")
s1.welcome()
print("GR No:",s1.get_GR_No())
print("Father Name:",s1.get_father_name())
print("Roll No:",s1.get_roll_n0())
print("Marks:",s1.get_marks())
print("Grade:",s1.get_grade()) 

#static parameter

class Student:
    @staticmethod
    def college():
        print("ABC college")


class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("car started:") 

car1=Car()
car1.start()

#create account class with 2 attributes - balance & account no.
#create method for debit, credit & printing the balance

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

acc1=Account(1000,2345)
print("usman khalil")
print("Account Balance:",acc1.balance)
print("Account No:",acc1.account_no)

class Account:
    def __init__(self,balance,account):
        self.balance=balance
        self.account=account

acc1=Account(1000,3456)
print("Account balance:",acc1.balance)
print("Account No:",acc1.account)

class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no

acc1=Account(23000,9876)
print("Account Balance:",acc1.balance)
print("Account No:",acc1.account_no)

class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no

    def debit(self,amount):
        self.balance-=amount
        print("Rs-",amount,"was debited") 
        print("total balance=",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs-",amount,"was credited")
        print("total balance=",self.get_balance())

    def get_balance(self):
        return self.balance 

acc1=Account(50000,5858)
acc1.debit(1000)
acc1.credit(2000)

acc1.credit(50000)
acc1.debit(1000)      

class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no

    def debit(self,amount):
        self.balance-=amount
        print("Rs:",amount,"has debited")
        print("total balance=",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs:",amount,"has credited")
        print("total balance=",self.get_balance()) 

    def get_balance(self):
        return self.balance

acc1=Account(25000,6458)
acc1.debit(1000)
acc1.credit(20000) 

class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no

    def debit(self,amount):
        self.balance-=amount
        print("Rs-",amount,"has debited")
        print("total amount=",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs-",amount,"was credited")
        print("total amount=",self.get_balance()) 

    def get_balance(self):
        return self.balance

acc1=Account(60000,5698)
acc1.debit(2000)
acc1.credit(60000)               


                























































































      


































































 


















































































































































































