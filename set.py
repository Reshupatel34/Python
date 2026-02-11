# no order , unique,immutable

# since dict and list are mutable then they wont be in sets

collection={1,2,3,4}

print(collection)
print(type(collection))

duplicate={1,2,2,3,3,4}
print(duplicate)
# o/p-->{1, 2, 3, 4}  
print(len(duplicate))
# o/p-->4



# empty set
# a={}-->it is a dict and not a set
set=set()
print(set)
# o/p-->set()

# set is mutalbe but the element in set are immutable that is why we can store tuples in sets as they are immutable
set={1,2}
set.add(3)
set.add(4)
set.remove(2)
print(set)
#set.remove(7)#-->KeyError if elem dosnot exists



# unhashble type
# hashing-->changing original value into encrypted value or smth

set.add((1,2,3))
print(set)

# empties the set
# set.clear()
print(set)



print(set.pop())


# union method in Sets

set1={1,2,3}
set2={4,5,6,1}
print(set1.union(set2))
print(set1.intersection(set2))

