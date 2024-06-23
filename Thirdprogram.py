marks=[32.5,52.5,66.5,55.5,21.2]
print(marks)
print(len(marks))
print(type(marks))
print(marks[0])
print(marks[1])

student=["usman",71.5,26,"karachi"]
print(student[0])
student[0]="ibrahim"
print(student)

candidate=["usman",56.45,24,"lahore"]
print(candidate)
print(candidate[0])
student[0]="ibrahim"
student[3]="karachi"
print(student)

marks=[23,54,66,85,85]
print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])

list=[2,3,6,1]
list.append(5)
print(list)

list=[2,3,6,1]
print(list.sort())
print(list)

list=[2,1,3,6]
print(list.append(4))
print(list.sort())
print(list)

list=[2,4,6,8]
print(list.sort(reverse=True))
print(list)

list=["apple","mango","grapes"]
print(list.sort(reverse=True))
print(list)

list=["c","b","a","e","d"]
print(list.sort())
print(list)

list=["a","b","c","d"]
list.reverse()
print(list)

list=[1,2,3,4,5]
list.insert(2,6)
print(list)

list=[1,2,3,4,5]
list.pop(3)
print(list)

#tuple

tuple=(2,5,6,8,9)
print(type(tuple))
print(tuple[0])
print(tuple[1])

tuple=()
print(tuple)
print(type(tuple))

tuple=(1,)
print(tuple)
print(type(tuple))

tuple=(1)
print(tuple)
print(type(tuple))

tuple=(1,2,3,4)
print(tuple[1:3])

tuple=(1,2,3,4,5,2)
print(tuple.index(2))
print(tuple.count(2))

movies=[]

mov1=input("enter 1st movie: ")
mov2=input("enter 2nd movie: ")
mov3=input("enter 3rd movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

list=[]

list1=input("enter 1st no: ")
list2=input("enter 2nd no: ")
list3=input("enter 3rd no: ")
list4=input("enter 4th no: ")

list.append(list1)
list.append(list2)
list.append(list3)
list.append(list4)

print(list)


fruit=[]

fruit1=input("enter 1st fruit: ")
fruit2=input("enter 2nd fruit: ")
fruit3=input("enter 3rd fruit: ")

fruit.append(fruit1)
fruit.append(fruit2)
fruit.append(fruit3)

print(fruit)

even=[]

even.append(int(input("enter 1st even no: ")))
even.append(int(input("enter 2nd even no: ")))
even.append(int(input("enter 3rd even no: ")))

print(even)

#pallintrome

list=[1,2,1]

copy_list=list.copy()
copy_list.reverse()

if(copy_list==list):
    print("pallintrome")
else:
    print("not pallintrome") 


list=[1,2,2]

copy_list=list.copy()
copy_list.reverse()

if(copy_list==list):
    print("pallintrome'")
else:
    print("not pallintrome")  

grade=("B","C","B","B")
print(grade.count("B"))

#Dictionary

info={
    "key":"value",
    "name": "usman",
    "university":"sir syed"

}

print(info)

info={
    "name":"usman",
    "college":"govt isl sci college",
    "school":"azeem school",
    "university":"sir syed university"
}
print(info)


info={
    "name":"usman",
    "subject":["python","java script"],
    "topics":("dict","sets"),
    "age":"26",
    "school name":"azeem school",
    "college name":"isl sci college",
    "profession":"teaching",
    "is adult":True,
    12.65:85
}
print(type(info))

info={
    "name":"usman",
    "subject":"python",
    "topics":"sets",
    "age":24
}

info["name"]="ibrahim"
info["surname"]="khalil"

print(info["name"])
print(info["topics"])

null_dict={}
null_dict["name"]="apna college"
print(null_dict)

#nested dictionary

student={
    "names":{
        "usman":65,
        "asma":95
    },
    "subjects":{
        "physics":65,
        "chemistry":91,
        "maths":75
    }
}

print(student)
print(student["subjects"]["chemistry"])
print(student["names"])

#method of Dictionary

student={
    "name":"usman",
    "subjects":{
        "phy":63,
        "maths":69
    }
    
    
}

print(student.keys())
print(student.values())
print(student.items())
print(student["name"])
print(student.get("name"))

student.update({"city":"karachi"})
print(student)
print(len(student.keys()))


student={
    "name":"usman",
    "subjects":{
        "phy":65,
        "che":71,
        "maths":45

    }
}

new_dict={"city":"karachi","age":26}
student.update(new_dict)
print(student)

#Set

set={1,2,3,4,"usman",4}
print(set)
print(type(set))
print(len(set))#total no of items













