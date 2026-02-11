#  data is stored in key-value pairs


info={
    "key":"value",
    "name":"Charlie",
    "topics":("dict","set"),
    1:23,
    1.2:14
}
print(info)

print(type(info))
# dict are unorder
# dict are mutable
# cant create duplicate key


# print value
print(info["name"])

# KeyError
# print(info['surname'])


# mutable
info["name"]="Bob"
print(info)

# adding new key value pair
info["surname"]="smith"
print(info)


# null dict
null_dict={}
print(null_dict)
# o/p--> {}


# nested dictionary
student={
    "name":"Charlie",
    "subject":{
        "chem":23,
        "phy":25,
        "math":29
    }
}
print(student["subject"])

# accessing the value of dict inside dict
print(student["subject"]["chem"])


# Dictionary Methods

print(student.keys())


# type cast to list
print(list(student.keys()))


# total number of keys
print(len(student))


# values-->returns a collection of all the values
print(student.values())

# items--> key value pairs ko return karta hai as tupples
print(student.items())
pairs=list(student.items())
print(pairs[0])
# o/p-->('name', 'Charlie')


# get method-->returns the value of the key
print(student["name"])  #return keyError if key not found so the code below it will not run at all
print(student.get("name1")) #return none if key not found


# update method
student.update({"city":"Delhi"})
print(student)

