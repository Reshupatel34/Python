# tup=(1,2,3,4,5)
# for i in tup:
#     print(i)



# str="hello"
# for char in str:
#     print(char)
# else:
#     print("End")



# nums=[1,4,9,16,25]
# for i in nums:
#     print(i)


# # range function
# for i in range(10):
#     print(i)


# # range(start,stop,jump)
# for i in range(1,10,2):
#     print(i)

# # from 1 to 100
# for i in range(101):
#     print(i)


# # from 100 to 1
# for i in range(100,0,-1):
#     print(i)


# # table of n
# n=2
# for i in range(1,11):
#     print(n*i)



# pass in for loop-->used to make/save space for some future code
# it is empty, the whole for loop and when we write pass it skips the loop completely

for i in range(100):
    pass

print("Hola")



# WAP to find the sum of first n numbers
n=5
i=1
sum=0
for i in range(n+1):
    sum+=i
print(sum)



# WAP to find the factorial of first n numbers
n=5
mult=1
i=1
for i in range(1,n+1):
    mult*=i
print(mult)