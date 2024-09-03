#Loops are used to repeat instructions.
#While loop

count = 1 #start
while count <= 5: #condition
    print("Hello")
    count+=1  #Increment
print("last value =",count)    

i=1
while i<=6:
    print("islamabad")
    i+=1
print(i)    

i=3
while i<=8:
    print("Lahore")
    i+=1
print(i)    

i=1
while i<=10:
    print(i,"Usman")
    i+=1
print(i)

i=1
while i<=10:
    print(i,"Apple")
    i+=1

i=1
while i<=5:
    print(i)
    i+=1
print("End")  

i=1
while i<=10:
    print(i)
    i+=2
print("end")    

i=2
while i<=10:
    print(i)
    i+=2
print("END")

i=5
while i>=1:
    print(i,"hello")
    i-=1
print("end")  
print(i)  

i=10
while i>=2:
    print(i,"Even Numbers")
    i-=2
print(i)   

i=9
while i>=1:
    print(i,"Odd Numbers")
    i-=2
print(i)

#Print numbers from 1 to 100.
i=1
while i<=100:
    print(i)
    i+=1

#Print numbers from 100 to 1.
i=100
while i>=1:
    print(i)
    i-=1

#Print the multiplication table of a number n.

n=3
i=1
while i<=10:
    print(n*i)
    i+=1

n=5
i=1
while i<=10:
    print("5 *",i, "=", n*i)    
    i+=1

n=4
i=10
while i>=1:
    print("4 *", i, "=", n*i)
    i-=1

#Print the elements of the following list using a loop.

list=[1,4,9,16,25,36,49,64,81,100]
index = 0
while index < len(list):
    print(index)
    index+=1

list=[1,4,9,16,25,36,49,64,81,100]
index = 0
while index < len(list):
    print(list[index])
    index+=1

nums=[3,6,9,12,15,18,21,24,27,30]
index = 0
while index < len(nums):
    print(nums[index])
    index+=1

tuple=(2,4,6,8,10,12,14,16,18,20)
index = 0
while index < len(tuple):
    print(tuple[index])
    index+=1

list=[1,4,9,16,25,36,49,64,81,100]
index=0
while index < len(list):
    print(list[index])
    index+=1

names=["ayesha","abid","aslam","atif","hasan"]
i=0
while i < len(names):
    print(names[i])
    i+=1

#Search for a number x in this tuple using loop.
tuple=(2,4,6,8,10,12,14,16,18,20)
x=12
i=0
while i<len(tuple):
    if(tuple[i] == x):
        print("found at index i =", i)
    i+=1    

list=[2,4,5,6,3,2,5,6,7,8,4,6,5,3]
x=4
i=0
while i < len(list):
    if(list[i] == x):
        print("found =", i)
    i+=1

tuple=(3,5,1,2,5,6,6,4,6,7,88,3,4,5,6,7,9,5,5)
x=5
i=0
while i < len(tuple):
    if(tuple[i] == x):
        print("found =", i)
    i+=1

list=[2,3,5,4,6,3,4,6,7,4]
x=4
i=0
while i < len(list):
    if(list[i] == x):
        print("found at index", i)
    else:
        print("finding...")
    i+=1

list=[2,4,6,8,10,4,12,14,16,18,20]
x=4
i=0
while i < len(list):
    if(list[i] == x):
        print("found...")
    else:
        print("finding...")
    i+=1

names=["aslam","aqib","bashir","manza","aslam","adil"]
x="aslam"
i=0
while i < len(names):
    if(names[i] == x):
        print("STOP")
    else:
        print("RUN...")
    i+=1

#Break: used to terminate the loop when encountered.
#terminate means atop
#BREAK

i=1
while i<=5:
    print(i)
    if(i == 3):
        break
    i+=1
print("end of loop")

i=2
while i<=10:
    print(i)
    if(i == 5):
        break
    i+=1
print("stop")

i=10
while i >= 1:
    print(i)
    if(i == 4):
        break
    i-=1
print("END")

i=20
while i >= 10:
    print(i)
    if(i == 14):
        break
    i-=1
print("end...")    

list=[1,4,5,6,6,3,4,5]
x=6
i=0
while i < len(list):
    if(list[i] == x):
        print("found at index =", i)
        break
    else:
        print("finding..")
    i+=1
print("end of loop")        

names=["aqib","jawed","hasham","zain","kinza","kiren"]
x="zain"
i=0
while i < len(names):
    if(names[i] == x):
        print("found =", i)
        break
    else:
        print("finding...")
    i+=1
print("END")

list=["Army","Navy","Fazaiya","Air force","Politician"]
x="Fazaiya"
i=0
while i < len(list):
    if(list[i] == x):
        print("found =", i)
        break
    else:
        print("finding...")
    i+=1
print("END")   

tuple=(1,5,3,4,5,4,5,6,6)
x=4
i=0
while i < len(tuple):
    if(tuple[i] == x):
        print("found =", i)
        break
    else:
        print("finding...")
    i+=1
print("end of loop...")            

#Continue
#continue: terminates execution in the current iteration & continues execution of the loop
#with the next iteration

i=0
while i<=5:
    if(i == 3):
        i+=1
        continue #skip
    print(i)
    i+=1
print("END")    

i=1
while i<=6:
    if(i == 4):
        i+=1
        continue
    print(i)
    i+=1
print("end")

i=5
while i>=1:
    if(i == 2):
        i-=1
        continue
    print(i)
    i-=1
print("END")    

i=20
while i>=1:
    if(i == 10):
        i-=1
        continue
    print(i)
    i-=1
print("end of loop...")

#Print odd numbers

i=1
while i<=10:
    if(i % 2 == 0):
        i+=1
        continue
    print(i)
    i+=1

i=10
while i>=1:
    if(i % 2 == 0):
        i-=1
        continue
    print(i)
    i-=1

#Print even numbers

i=0
while i<=20:
    if(i % 2 != 0):
        i+=1
        continue
    print(i)
    i+=1

i=20
while i>=1:
    if(i % 2 != 0):
        i-=1
        continue
    print(i)
    i-=1

i=1
while i<=10:
    if(i % 2 == 0):
        i+=1
        continue
    print(i)
    i+=1

i=5
while i<=20:
    if(i % 2 == 0):
        i+=1
        continue
    print(i)
    i+=1

i=1
while i<=10:
    if(i % 2 != 0):
        i+=1
        continue
    print(i)
    i+=1

i=20
while i>=1:
    if(i % 2 == 1):
        i-=1
        continue
    print(i)
    i-=1

i=20
while i>=1:
    if(i % 2 != 1):
        i-=1
        continue
    print(i)
    i-=1

#For loop in Python
#Looops are used for sequential traversal. For traversing list, string, tuple etc.

list=[1,2,3,4,5,6]
for ele in list:
    print(ele)

list=[3,2,1,5,4,6,4,7]
for val in list:
    print(val)

names=["ayesha","ahmed","umair","hasan","aqib"]
for char in names:
    print(char)

password=(1,"a","&","*","^","%")
for ele in password:
    print(ele)

str="pakistan"
for char in str:
    print(char)

str="Mango"
for char in str:
    print(char)

str="Pakistan"
for char in str:
    if(char == "t"):
        print("t found")
        break
    print(char)
else:
    print("end")

str="India"
for char in str:
    if(char == "d"):
        print("d found")
        break
    print(char)
else:
    print("END")

list=[2,1,4,3,2,4,5,6,5,6]
for val in list:
    if(val == 4):
        print("4 found")
        break
    print(val)
else:
    print("end")

str="computer"
for char in str:
    if(char == "e"):
        print("e found")
        break
    print(char)
else:
    print("stop")    

nums=[2,3,2,5,6,4,5,4,4]
for ele in nums:
    if(ele == 6):
        print("6 found")
        break
    print(ele)
else:
    print("end")

#Print the elements of the following list using a loop.

list=[1,4,9,16,25,36,49,64,81,100]
for ele in list:
    print(ele)

#Search for a number x in this tuple using loop.

list=[1,4,9,16,25,36,49,64,81,100]
x=64
for ele in list:
    if(ele == x):
        print("value found")
        break
    print(ele)
else:
    print("end")    

tuple=(1,4,9,16,25,36,49,64,81,100,49)
x=49
index=0
for ele in tuple:
    if(ele == x):
        print("number found at index",index)
        break
    index+=1    

names=["ansar","javed","hussain","ifra","hussain"]
x="hussain"
index=0
for char in names:
    if(char == x):
        print("character found at index",index)
        break
    index+=1

#Range()
print(range(5))
print(range(10))

seq=range(3)
print(seq[0])
print(seq[1])
print(seq[2])

seq=range(5)
for ele in seq:
    print(ele)

nums=range(10)
for val in nums:
    print(val)

list=range(5)
for val in list:
    print(val)

for i in range(5):
    print(i)

for j in range(10):
    if(j == 5):
        print("value found")
        break
    j+=1
    print(j)    

for j in range(5):
    if(j == 3):
        print("val found")
        break
    print(j)
    j+=1

for k in range(10): #range(stop)
    print(k)

for k in range(2,10): #range(start, stop)
    print(k)

for k in range(2,10,2): #range(start, stop, step)
    print(k)

#Print even numbers
for e in range(2,101,2):
    print(e)

#Print odd numbers.
for o in range(1,100,2):
    print(o)

#Print numbers from 1 to 100.
for i in range(1,101):
    print(i)

#Print numbers from 100 to 1.
for j in range(100,0,-1):
    print(j)    

#Print the multiplication table of a number n.
n=int(input("Enter number: "))
for i in range(1,11):
    print(n,"*", i, "=", n*i)

n=int(input("enter number :"))
for j in range(1,11):
    print(n, "*", j, "=", n*j)

n=int(input("enter number: "))
for k in range(1,16):
    print(n,"*", k, "=", n*k)

n=int(input("enter number: "))
for l in range(1,21):
    print(n, "*", l, "=", n*l)

#Pass Statement
#Pass statement means null statement.
#Pass is a null statement that does nothing. It is used as a placeholder for future code.

for i in range(5):
    pass
print("king")

if(i>=5):
    pass
print("promote")

#Write a program to find the sum of first n numbers. (using while loop)
#for loop
n=5
sum = 0
for i in range(1,n+1):
    sum+=i
print("total sum =", sum)  

#while loop
n=5
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("total sum =", sum)   

n=6
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("total sum =", sum)    

n=5
prod=1
i=1
while i<=n:
    prod*=i
    i+=1
print("Total product of 5 numbers =", prod)    

n=6
sum=0
for j in range(1,n+1):
    sum+=j
print("total sum =", sum)    

n=7
sum=0
for k in range(1,n+1):
    sum+=k
print("total sum =", sum)    

n=5
prod=1
for i in range(1,n+1):
    prod*=i
print("total product =", prod)    

n=6
prod=1
for j in range(1,n+1):
    prod*=j
print("total product of 6 numbers =",prod)

n=7
prod=1
for k in range(1,n+1):
    prod*=k
print("total product of 7 numbers =", prod)    

#Write a program to find the factorial of first n numbers. (using for loop)

n=5
fact = 1
i=1
while i<=n:
    fact*=i
    i+=1
print("fact of 5 is =",fact)    

n=6
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("fact of 6 is =", fact)

#for loop

n=5
fact = 1
for i in range(1, n+1):
    fact*=i
print("fact of 5 is =", fact)    

n=6
fact = 1
for i in range(1, n+1):
    fact*=i
print("fact of 6 =", fact)  

n=7
fact = 1
for j in range(1, n+1):
    fact*=j
print("fact of 7 =", fact)    

n=4
fact = 1
for k in range(1, n+1):
    fact*=k
print("fact of 4 is =", fact)    
























































































































































    





































































































































    

























































































































































































































































































