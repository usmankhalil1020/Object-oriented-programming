
#Functions

def cal_sum(a,b):
    sum = a+b
    print(sum)
    return cal_sum
cal_sum(6,6)

def sum(a,b,c):
    sum = a+b+c
    print(sum)
sum(4,9,8)    

def diff(a,b):
    diff =  a-b
    print(diff)
    return diff
diff(4,1)
diff(10,9)

def sum(a,b,c,d):
    sum = a+b+c+d
    print(sum)
    return sum
sum(2,4,6,8)
sum(1,2,3,4)

def diff(a,b,c,d):
    diff = a-b-c-d
    print(diff)
    return diff
diff(8,7,10,4)

def prod(a,b,c):
    prod = a*b*c
    print(prod)
    return prod
prod(2,4,6)
prod(1,2,3)

def div(a,b):
    div = a/b
    print(div)
    return div
div(10,2)
div(20,5)

#function definition
def sum(a,b):#parameters
    return a+b
sum=sum(3,5) #function call; arguments
print(sum)

def diff(a,b):
    return a-b
diff=diff(3,1)
print(diff)

def prod(a,b,c):
    return a*b*c
prod=prod(2,4,6)
print(prod)

def div(a,b):
    return a/b
div=div(5,2)
print(div)

def print_hello():
    print("hello")
print_hello()
print_hello()

def print_usman():
    print("usman")
print_usman()

def print_list():
    print(1,2,3,4,5)
print_list()

def print_list():
    print(2,4,6,8,10)
print_list()    

def print_university():
    print("university")
print_university()

output = print_usman()
print(output)#None

#Average of 3 numbers
def avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
avg(1,2,3)

#Avg of 4 numbers
def avg(a,b,c,d):
    sum = a+b+c+d
    avg = sum/4
    print(avg)
avg(1,2,3,4)
avg(2,4,6,8)   

print("Usman", end=" ")
print("Khalil")

print("Usman", end="@")
print("Khalil")

#Build_in_Function: already in python function
#User defined function: write programmer

def prod(a=5,b=3):
    print(a * b)
    return prod
prod()

def prod(a=2,b=4,c=4):
    print(a*b*c)
    return prod
prod()

#first non default argument then default argument
def prod(a,b=3):
    print(a * b)
    return prod
prod(5)

#Write a function to print the length of a list.(list is a parameter)

cities = ["lahore","karachi","islamabad","sukkur","pune"]
def print_len(list):
    print(len(list))
print_len( cities)    

list=[1,2,3,4,5,6,7,8,9]
def print_len(list):
    print(len(list))
print_len(list) 

army = ["soldier", "lance naik", "captain", "major", "army chief"]
def print_len(list):
    print(len(list))
print_len(army)    

#Write a function to print the elements of a list in a single line. (list is the parameter)
teams = ["pak","ind","aus","new","eng"]
def print_list(list):
    for i in list:
        print(i, end=" ")
print_list(teams)
print()

fruits=["mango","banana","orange","water melon", "apple"]
def print_list(list):
    for i in list:
        print(i, end=" ")
print_list(fruits)     
print()

animals = ["tiger", "lion", "goat", "cow", "sheep", "buffalo", "camel"]
def print_list(list):
    for i in list:
        print(i, end=" ")
print_list(animals)
print()

#Write a function to find the factorial of n. (n is the parameter)
#loop
n=5
fact = 1
for i in range(1, n+1):
    fact *= i
print("factorial of 5 =",fact)    

#Function
def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact*=i
    print("factorial of given n is",fact)
fact(5)        

def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact*=i
        print("factorial of given n is",fact)
fact(6)    

def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact*=i
        print("factorial of given n is",fact)
fact(7)

def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact*=i
        print("factorial of given n is", fact)
fact(4)

def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact*=i
        print("factorial of given n is", fact)
fact(3)

#Write a function to convert USD to PAK.
def convertor(usd_val):
    pak_val = usd_val * 276
    print(usd_val, "USD =", pak_val, "PAK")
convertor(30)

def convertor(ind_val):
    pak_val = ind_val * 3.25
    print(ind_val, "IND", pak_val, "PAK")
convertor(50)

def convertor(usd_val):
    chi_yaun = usd_val * 7.25
    print(usd_val, "USD", chi_yaun, "YAUN")
convertor(20)

def convertor(saudi_riyal):
    pak_val = saudi_riyal * 75
    print(saudi_riyal, "RIYAL", pak_val, "PAK")
convertor(75)    

def number(n):
    if(n % 2 == 0):
        print("even number")
    else:
        print("odd number")
number(12)
number(15)

#Recursion: when a function calls itself repeatedly.
#print n to 1 backwards

def show(n):
    print(n) #5
show(5)    

#Recursive function

def show(n):
    if(n == 0): #Base case
        return
    print(n)
    show(n-1)
show(5)    

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
show(5)    

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
show(6)    

def show(n):
    if(n == -1):
        return
    print(n)
    show(n-1)
show(5)    

def show(n):
    if(n == 5):
        return 
    print(n)
    show(n+2)
show(1)    

def show(n):
    if(n == 9):
        return
    print(n)
    show(n+2)
show(1)    

def show(n):
    if(n == -2):
        return 
    print(n)
    show(n-2)
show(6)    

def show(n):
    if(n == -3):
        return
    print(n)
    show(n-2)
show(9)    

def show(n):
    if(n == 10):
        return
    print(n)
    show(n+2)
show(0)    

def show(n):
    if(n == -1):
        return
    print(n)
    show(n-3)
show(8)    

def show(n):
    if(n == 20):
        return
    print(n)
    show(n+2)
show(0)    

def show(n):
    if(n == -1):
        return
    print(n)
    show(n-3)
show(20)    

#Recurrence relation: n! = (n-1)! * n

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1)*n
print("fact of 5 is ", fact(5))

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1)*n
print("fact of 4 is =", fact(4))

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1)*n
print("fact of 6 is =", fact(6))

#Write a recursion function to calculate the sum of first n natural numbers.

def sum(n):
    if(n == 0):
        return 0
    return sum(n-1) + n
print(sum(5))

def sum(n):
    if(n == 0):
        return 0
    return sum(n-1) + n
print("sum of 6 =", sum(6))

def sum(n):
    if(n == 0):
        return 0
    return sum(n-1) + n
print(sum(4))

def prod(n):
    if(n == 1):
        return 1
    return prod(n-1) * n
print("product of 3 number is =",prod(3))

#Write a recursive function to print all elements in a list.
#Hint : use list & index as parameters.

def print_list(list, index = 0):
    if(index == len(list)):
        return
    print(list[index])
    print_list(list, index + 1)

names=["aslam","usman","kinza","ibrar","hasan"]
print_list(names)    

def print_list(list, idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
fruits = ["mango", "banana", "apple", "orange"]
print_list(fruits)    

def print_list(list, index = 0):
    if(index == len(list)):
        return
    print(list[index])
    print_list(list, index+1)
teams = ["pakistan","india","newzealand","bangladesh"]    
print_list(teams)



























































































































































































































































