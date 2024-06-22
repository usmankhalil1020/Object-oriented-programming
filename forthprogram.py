collection=set()
collection.add(1)
collection.add(2)
collection.add(2)

print(collection)

collection=set()
collection.add(2)
collection.add(3)
collection.add(4)
collection.add(1)
collection.remove(3)
collection.add("usman")
collection.add((1,2,3))

print(collection)

collection=set()
collection.add(1)
collection.add(2)
collection.add("usman")
collection.clear()

print(len(collection))

collection={"usman","umar","ibrahim","asma","samra"}
print(collection.pop())
print(collection.pop())
print(collection.pop())

#union and intersection
set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

dict={
    "cat":"a small animal",
    "table":["a piece of furniture","list of fact and figures"]
}

print(dict)

subjects={
    "python","java","c++","python","javascript","java","python","java","c++","c"
}
print(subjects)

print(len(subjects))

marks={}

x=int(input("enter phy: "))
marks.update({"phy":x})

y=int(input("enter math: "))
marks.update({"math":y})

z=int(input("enter che: "))
marks.update({"che":z})

print(marks)

marks={}

x=int(input("enter Eng: "))
marks.update({"Eng":x})

y=int(input("enter phy: "))
marks.update({"phy":y})

z=int(input("enter che: "))
marks.update({"che":z})

t=int(input("enter math: "))
marks.update({"math":t})

print(marks)

val={9,9.0}
print(val)

val={9,9.25}
print(val)

val={9,9.25,8,8.0}
print(val)

val={9,"9.0"}
print(val)

val={
    ("float",9.0),
    ("int",9)
}
print(val)

val={
    ("float",9.0),
    ("int",9),
    ("str","usman")
}
print(val)

#loops, for loops and while loop

count=1
while count<=5:
    print("usman")
    count=count+1

count=1
while count<=6:
    print("ibrahim") 
    count+=1

i=1
while i<=5:
    print("khalil")
    i+=1  

i=1
while i<=8:
    print("usman khalil")
    i=i+1        

i=1
while i<=5:
    print(5,i)
    i+=1  

count=1
while count<=10:
    print("Asma")
    count=count+1 

i=1
while i<5:
    print("U")
    i+=1

i=1
while i<=11:
    print("usman",i)
    i+=1   

i=1
while i<=10:
    print(i,"usman")
    i+=1    

i=1
while i<=7:
    print(i,"A","B","C","D","E","F","G") 
    i+=1  

i=1
while i<=5:
    print(i)
    i+=1
print("end loop")  

i=5
while i>=1:
    print(i)
    i-=1
print(i) 
print("end loop")  

i=10
while i>=1:
    print(i)
    i-=1
print("end") 

i=5
while i>=5:
    print(i,"usman")
    i-=1
print("end")    

#print numbers from 1 to 100

i=1
while i<=100:
    print(i)
    i+=1

#print numbers from 100 to 1

i=100
while i>=1: #stopping condition
    print(i)
    i-=1

#print the multiplication table

i=1
while i<=10:
    print(3*i)
    i+=1

i=1
while i<=10:
    print(4*i)
    i+=1 

i=10
while i>=1:
    print(3*i)
    i-=1 

n=int(input("enter number: "))
i=1
while i<=10:
    print(n*i)
    i+=1 

n=int(input("enter number: "))
i=10
while i>=1:
    print(n*i)
    i-=1  

n=int(input("enter number: "))
i=1
while i<=10:
    print(n*i)
    i+=1

n=int(input("enter number: "))
i=10
while i>=1:
    print(n*i)
    i-=1 

#

num=[1,4,9,16,25,36,49,64,81,100] 

index=0
while index < len(num):
    print(index)
    index+=1

num=[1,4,9,16,25,36,49,64,81,100]

index=0
while index < len(num):
    print(num[index])
    index+=1

num=[1,2,3,4,5,6]

index=0
while index < len(num):
    print(num[index])
    index+=1  

list=[1,2,3,4,5,6,7,8,9]
index=0
while index < len(list):
    print(list[index])
    index+=1  

str=["usman","hamza","jamal"]
index=0
while index < len(str):
    print(str[index])
    index+=1 

tuple=(1,4,9,16,25,36,49,64,81,100)
x=49
i=0
while i < len(tuple):
    if(tuple[i]==x):
        print("found at index: ",i)
    i+=1 

#break & continue

i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print("end of loop")  

num=(1,2,3,4,5,6,7,8,9,10)

x=6
i=0
while i < len(num):
    if(num[i]==x):
        print("found at i: ",i)
        break
    else:
        print("finding: ")
    i+=1

    print("end of loop")    


#continue

i=0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1

i=0
while i<=5:
    if(i==4):
        i+=1
        continue
    print(i)
    i+=1
    
i=1
while i<=5:
    if(i==2):
        i+=1
        continue
    print(i)
    i+=1

i=1
while i<=5:
    if(i==4):
        i+=1
        continue
    print(i)
    i+=1

i=5
while i>=1:
    if(i==3):
        i-=1
        continue
    print(i)
    i-=1 

i=5
while i>=1:
    if(i==4):
        i-=1
        continue
    print(i)
    i-=1

i=0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1 

i=6
while i>=1:
    if(i==5):
        i-=1
        continue #skip
    print(i)
    i-=1 

i=1
while i<=10:
    if(i % 2==0):
        i+=1
        continue
    print(i)
    i+=1  

i=1
while i<=10:
    if(i % 2 !=0):
        i+=1
        continue
    print(i)
    i+=1 

#for loop

numbers=[1,2,3,4,5]
for val in numbers:
    print(val)

names=["usman","umar","ibrahim","asma","samra"]
for i in names:
    print(i)

tuple=(1,2,3,4,5,6,7,8,9)
for i in tuple:
    print(i) 

str="UsmanKhalil"
for char in str:
    print(char) 

str="UsmanKhalil"
for char in str:
    if(char==n):
        print("n found")
        break
    print(char)
else:
    print("END")

str="usmanKhalil"
for char in str:
    if(char=="n"):
        print("n found")
        break
    print(char)

str="UsmanKhalil"
for char in str:
    if(char=="a"):
        print("a found")
        break
    print(char) 

str="MuhammadUsmanKhalil"
for char in str:
    if(char=="d"):
        print("d found")
        break
    print(char)      
else:
    print("END")

num=[1,4,9,16,25,36,49,64,81,100]

for ele in num:
    print(ele)

num=[1,4,9,16,25,36,49,64,81,100,49]
x=49

index=0 
for ele in num:
    if(ele==x):
        print("number found at index",index)
    index+=1

num=[1,2,2,3,3,4,5,6]
x=3

index=0
for ele in num:
    if(ele==x):
        print("number found at index: ",index)
    index+=1 

num=(2,3,4,4,5,4,4,6,7)
x=4

index=0
for ele in num:
    if(ele==x):
        print("enter found at index: ",index)
    index+=1

num=["usman","ibrahim","salman","usman","usman"]
x="usman"
index=0
for ele in num:
    if(ele==x):
        print("enter found at index: ",index)
    index+=1 

num=(1,2,2,3,4,2,5,6,7) 
x=2
index=0
for ele in num:
    if(ele==x):
        print("index found at no: ",index) 
        break
    index+=1

print(range(5))

seq=range(5)
print(seq[1])
print(seq[0])
print(seq[2])
print(seq[3])
print(seq[4])

seq=range(5)
for i in seq:
    print(i)

for i in range(10):
    print(i)

for i in range(11):
    print(i)

for i in range(10): #range(stop)
    print(i) 


for i in range(2,10): #range(start,stop)
    print(i)

for i in range(2,10,2): #range(start,stop,step)
    print(i)

for i in range(1,101,2):
    print(i)
for i in range(1,100,2):
    print(i) 

for i in range(1,101):
    print(i)

for i in range(100,0,-1):
    print(i)  

for i in range(100,0,-2):
    print(i)  

for i in range(1,401,4):
    print(i) 

for i in range(400,0,-4):
    print(i) 

n=int(input("Enter number: "))
for i in range(1,11):
    print(n*i)

n=int(input("enter number: "))
for i in range(1,21):
    print(n*i)

n=int(input("Enter number: "))
for i in range(100,0,-1):
    print(n*i) 

n=int(input("Enter number: "))
for i in range(201,0,-4):
    print(n*i)

for i in range(5):
    pass
print("usman") 

n=5
for i in range(n+1):
    print(i)

n=5
for i in range(1,n+1):
    print(i)

n=5
sum = 0
for i in range(1,n+1):
    sum+=i
print("total sum=",sum)  

n=6
sum = 0
for i in range(1,n+1):
    sum+=i
print("total sum = ",sum)  

n=7
sum = 0
for i in range(1,n+1):
    sum+=i
print("total sum = ",sum) 

n=4
sum = 0
for i in range(1,n+1):
    sum+=i
print("total sum=",sum)

n=7
sum = 0
for i in range(1,n+1):
    sum+=i
print("total sum=",sum)

n=9
sum = 0
for i in range(1,n+1):
    sum+=i
print("total sum is:",sum)    

n=8
sum = 0
for i in range(1,n+1):
    sum+=i
print("total sum is=",sum)

n=7
sum = 0
i=1
while i<=n:
    sum+=i
    i+=1
print("total no=",sum) 

n=8
sum = 0
i=1
while i<=n:
    sum+=i
    i+=1
print("total sum: ",sum)

n=5
fact = 1
i=1
while i<=n:
    fact*=i
    i+=1
print("factorial =",fact)  

n=6
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("factorial: ",fact)

n=7
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("factorial= ",fact)

n=8
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("factorial=",fact)

n=3
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("factorial=",fact)

n=4
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("factorial=",fact)  

n=5
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("factorial=",fact)

n=6
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("factorial=",fact) 

#for loop
n=5
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial=",fact)    
















































































































    



















































