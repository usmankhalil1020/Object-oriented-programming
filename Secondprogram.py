str1="my name is usman.\ni am  good in python"
print(str1)

a="my name is usman. \ti am good in english"
print(a)

str1="karachi"
print(len(str1))

str2="university"
len2=len(str2)
print(len2)

final_str=str1+" "+str2
print(final_str)
print(len(final_str))

str="karachi university"
cha=str[5]
print(cha)

str="usman khalil"
print(str[8])

str="karachi university"
print(str[1:4])

str="usman khalil"
print(str[0:5])
print(str[0:7])

str="ibrahim khalil"
print(str[7:len(str)])
print(str[8:len(str)])
print(str[8:])

str="apna college"
print(str[:4])
print(str[5:])

str="apple"
print(str[-3:-1])
print(str[-5:-2])
print(str[-6:-1])

str="universities"
slicing=str[-7:-1]
print(slicing)

str="i am studying python from university of karachi"
print(str.endswith("chi"))
print(str.endswith("opo"))

str="usman"
print(str.endswith("an"))
print(str.endswith("on"))

str="i am studying python"
print(str.capitalize())

str="i am studying python"
print(str.capitalize())
print(str)

str="i am studying python"
str=str.capitalize()
print(str)

str="i am studying python from apna college"
print(str.replace('a',"e"))

str="i am studying python from ku"
print(str.replace("python","java"))

str="i am from studying pytho from ku"
print(str.find("from"))

str="i am"
print(str.find("o"))

str="i am from studying python from ku"
print(str.count("from"))
print(str.count("o"))

name=input("enter your name")
print("lenghth of your name: ",len(name))

name=input("enter your name: ")
print("length of your name: ",len(name))

name1=int(input("enter first number"))
name2=int(input("enter second number"))
print("Average of two number is: ",name1+name2/2)

str="$i am $ i $"
print(str.count("$"))

light=input("light")
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("run")
elif(light=="yellow"):
    print("start")

num=25
if(num>25):
    print("greater than 25")
elif(num<25):    
    print("less than 25") 

light="pink"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("run")
else:
    print("break")   

age=24
if(age>=18):
    print("can vote")
else:
    print("cannot vote") 

marks=int(input("enter student marks: "))

if marks>=90:
    print("A+")
elif marks>=80 and marks<90:
    print("A")
elif marks>=70 and marks<80:
    print("B")
elif marks>=60 and marks<70:
    print("C")
elif marks>=50 and marks<60:
    print("D")
else:
    print("F")  

#Nesting

age=34

if(age<18):
    if(age>=80):
        print("cannot drive")
else:
    print("drive") 


num=int(input("enter number: "))
rem=num % 2
if(rem==0):
    print("even")
else:
    print("odd")

num=int(input("enter number: "))
rem=num % 2
if(rem==0):
    print("even")
else:
    print("odd")  

a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))

if(a>=b and a>=c):
    print("first number is largest: ")
elif(b>=c):
    print("second number is largest: ")
else:
    print("third number is largest: ")

a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
d=int(input("enter forth number: "))

if(a>=b and a>=c and a>=d):
    print("first number is largest")
elif(b>=c and b>=d):
    print("second number is largest: ")
elif(c>d):
    print("third number is largest: ")
else:
    print("forrth number is largest: ")  

x=int(input("enter number: "))
if(x % 7==0):
    print("multiple of 7")
else:
    print("not multiples of 7")  

y=int(input("enter number: "))
if(y % 5==0):
    print("multiples of 5") 
else:
    print("not multiples of 5") 


z=int(input("enter number: "))
if(z % 4==0):
    print("multiples of 4")
else:
    print("not multiples of 4")    





    

            



