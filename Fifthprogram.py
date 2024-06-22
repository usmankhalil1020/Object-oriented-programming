def cal_sum(a,b):
    sum = a+b
    print(sum)
    return sum
cal_sum(5,6)
cal_sum(10,15)
cal_sum(12,34)

def sum(a,b):
    sum=a+b
    print(sum)
    return sum 
sum(10,20)
sum(20,10)
sum(5,10)

def difference(a,b):
    difference=a-b
    print(difference)
    return difference 
difference(20,10)
difference(8,4)

def diff(a,b):
    diff=a-b
    print(diff)
    return diff
diff(4,2)
diff(5,3)
diff(6,4)

def mul(a,b):
    mul=a*b
    print(mul)
    return mul
mul(6,5)
mul(4,5)
mul(8,4)

def div(a,b):
    div=a/b
    print(div)
    return div
div(5,2)
div(6,3)
div(4,7)

def sum(a,b):
    sum=a+b
    print(sum)
    return sum
sum(4,3)
sum(4,5)
sum(6,6)

def sum(a,b):
    return a+b
sum=sum(3,4)
print(sum)

def diff(a,b):
    return a-b
diff=diff(5,4)
print(diff)

def mul(a,b):
    return a*b
mul=mul(4,3)
print(mul)

def print_hello():
    print("hello")
print_hello()   

def print_usmankhalil():
    print("usmankhalil")
print_usmankhalil()  

def print_muhammadusmankhaalil():
    print("muhammadusmankhalil")
print_muhammadusmankhaalil()

def print_ibrahimkhalil():
    print("ibrahimkhalil")
print_ibrahimkhalil()

def print_AsmaKhalil():
    print("AsmaKhalil")
print_AsmaKhalil()    

output=print_hello()
print(output)     

#average of 3 numbers
def avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg 

avg(1,2,3)
avg(2,4,6)

def avg(a,b,c,d):
    sum=a+b+c+d
    avg=sum/4
    print(avg)
    return avg 
avg(3,4,5,6)
avg(2,4,6,8)

def avg(a,b,c,d,e):
    sum=a+b+c+d
    avg=sum/5
    print(avg)
    return avg
avg(1,2,3,4,5)
avg(6,7,8,9,10)

print("usman","khalil")
print("usman", end=" ") #sep=" "
print("ibrahim") #end = "\n"

print("Asma",end="&")
print("Khalil")

print("Samra",end="@")
print("Imran")

print("ibrahim",end="@&")
print("khalil")

#default fuctions
def mul(a=3,b=5):
    print(a*b)
    return a*b
mul()

def mul(a=4,b=5):
    print(a*b)
    return a*b
mul()


def add(a=6,b=5):
    print(a+b)
    return a+b
add()

def sub(a=7,b=4):
    print(a-b)
    return a-b
sub()

names=["usman","umar","salman","hafsa","fatima","hadia"]
numbers=[33,45,77,65,98,76,55]

def print_len(list):
    print(len(list))

print(len(names))
print(len(numbers)) 

n=5
fact=1
for i in range(1,n+1):
    fact*=i
print(fact) 

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(5)

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
fact(6)     

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
fact(10)  

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
fact(4) 

def convertor(usd_val):
    pak_value=usd_val*285
    print(usd_val,"USD=",pak_value,"PAK")

convertor(6)  

def convertor(usd_val):
    pak_value=usd_val*285
    print(usd_val,"USD=",pak_value,"PAK")
convertor(3)

def convertor(usd_val):
    pak_value=usd_val*290
    print(usd_val,"USD =",pak_value,"PAK")
convertor(5)

def convert(usd_value):
    pak_value=usd_value*286
    print(usd_value,"USD =",pak_value,"PAK")
convert(5)

def convert(usd_value):
    ind_value=usd_value*83
    print(usd_value,"USD =",ind_value,"IND")
convert(5) 

def convert(usd_value):
    chi_value=usd_value*7
    print(usd_value,"USD =",chi_value,"CHI")
convert(5)

def convert(pak_value):
    usd_value=pak_value*285
    print(pak_value,"PAK =",usd_value,"USD")

convert(285)

def convert(ind_value):
    pak_value=ind_value*3.33
    print(ind_value,"IND =",pak_value,"PAK")
convert(1)

def convert(saudi_riyal):
    pak_value=saudi_riyal*74.03
    print(saudi_riyal,"SAUDI RIYAL =",pak_value,"PAK RUPEE")
convert(1)

#recursive fuction

def show(n):
    print(n)
show(12)

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(10)

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5) 

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)  

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(4)

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    print("End")
show(3)

def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(5))

def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(4))

def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(6))

def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(7))

def fact(n):
    if(n==0 or n==1):
        return 1
    return fact(n-1)*n
print(fact(8))

def sum(n):
    if(n==0):
        return 0
    return sum(n-1)+n
sum=sum(10)
print(sum)

def sum(n):
    if(n == 0):
        return 0
    return sum(n-1)+n
sum=sum(9)
print(sum)

def sum(n):
    if(n == 0):
        return 0
    return sum(n-1)+n
sum=sum(10)
print(sum)



































































































































 































































































































    
