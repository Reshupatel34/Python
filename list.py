# lists are like arrays in java

marks=[13,13,14,12,11]
print(marks)


print(type(marks))

print(marks[0])


# in lists we can store different type of data type

student=["Charlie",34]
print(student)


# lists ar mutable
student[0]="Bob"
print(student)


#  slicing in lists
print(marks[1:4])

# List methods
list=[5,2,7,1,9]

list.append(4)
print(list)

list.sort()
print(list)


# reverse sorting
list.sort(reverse=True)
print(list)


# applying soritng in list os strings
fruits=["apple","kiwi","banana"]
print(fruits.sort())
fruits.sort()
print(fruits)


# reverse-->reverses list
fruits.reverse()
print(fruits)

# insert element at index--->(idx,value)
list=[1,2,4]
list.insert(1,5)
print(list)
# [1, 5, 2, 4]



# remove the first occurence of ele
list=[1,2,3,4,1,1]
list.remove(1)
print(list)

# pop ---> idx ko pop kara deta hai
list=[1,2,3,4]
list.pop(1)
print(list)



# WAP to ask user to enter names of thier 3 favorite movies and store them in a list
list=[]
for i in range(3):
    names=input("Enter a name : ")
    list.append(names)
print(list)