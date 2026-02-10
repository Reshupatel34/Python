str1="This is a string"
print(str1)

str2=" this is another string, \n with another line "
print(str2)

# concatenation of strings
final_str=str1+str2
print(final_str)


# length of the string
print(len(str1))

print(len(final_str))


# indexing in strings
str="HelloWorld"
print(str[0])

# printing all the elements in the str
for i in range(len(str)):
    print(str[i])

# string is immutable as well


# slicing in str [starting idx:ending index] excluded
fruit="apple"
print(fruit[0:3])

print(fruit[0:])
print(fruit[:len(fruit)])


# negative index ---> from the backwards,sarts with -1,-2,-3
print(fruit[-5:-1])
# last element
print(fruit[-1])


# functions in string

# ensWith()-->True,False
print(fruit.endswith("pple"))

# capitalise the first letter-->the old string does not change and remains the same
print(fruit.capitalize())
print(fruit)
# if we want to change the real string
fruit=fruit.capitalize()
print(fruit)

# replace function -->replace something with something
str="replace the string"
print(str.replace(" ","str"))
print(str.replace("string","str"))


# find function-->checks whether a character exsit or not anf is so then prints the first occurence
print(fruit.find("p"))
print(fruit.find("z"))

# count-->counts the total number of words/characters in a string
str="us dumb bitch ko ye samjh nahi aa raha to ye extra slow hai , .......mere pass extra do hai"
print(str.count("extra"))




# WAP to input user's first name and print its length

# name=input("Enter your name : ")
# print(len(name))


# WAP to input user's first name ans print its length
str="$$$$$$$$$"
print(str.count("$"))