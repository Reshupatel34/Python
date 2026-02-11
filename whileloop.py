# loops in python

# while loop

# infinite loop

# while True:
#     print("Hello")


count=1
while(count<=5):
    print("Hello")
    count+=1


# reverse while loop
i=5
while i>=1:
    print(i)
    i-=1

# print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1


# print numbers from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1


# print the multiplication table of number n
n=int(input("Enter a number: "))
i=1
while i<=10:
    print(n*i)
    i+=1


# print the eles of the following list using loop: [1,4,9,16,25,36,49,81,100]
list=[1,4,9,16,25,36,49,81,100]
i=0
while i<len(list):
    print(list[i])
    i+=1

# search for a number x in this tuple using loop
tupple=(1,4,9,16,25,36,49,81,100)
x=9
i=0
while i<len(tupple):
    if(tupple[i]==x):
        print("Found",i)
        break
    i+=1