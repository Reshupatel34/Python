#  a build in dataype -->immutable unlike lists in python

tup=(1,2,3,4)
print(tup)
print(tup[0])


# emtpy tuple
emp=()
print(type(emp))


# if we have single value in tupple than we have to include a , so 
# it is being treated like a tupple and not an int,flost,string
tup=(1)
print(type(tup))
# o/p--> <class 'int'>

tup=("hello")
print(type(tup))
# <class 'str'>

tup=(1.2)
print(type(tup))
# <class 'float'>

# that is why we have to have a comma for single values for it to be a tupple
tup=(1,)
print(type(tup))
# <class 'tuple'>


# slicing in tupples
tup=[1,2,3,4,5]
print(tup[:3])

# index -->returns first occurence of an ele
print(tup.index(1))


# count -->returns total count occurence
tup=(1,2,3,4,3,2,1)
print(tup.count(1))

