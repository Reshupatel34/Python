# calculate the sum of 2 numbers using function

# function definition
def calc_sum(a,b): #parameters
    sum=a+b
    print(sum)
    return sum

calc_sum(2,3)
calc_sum(1.2,23.4)


def print_hello():
    print("Heelloo")

print_hello()


# average of three numbers
def calc_average(a,b,c):
    return a+b+c/3
avg=calc_average(100,100,100)
print(avg)


# WAP to print the length of the list (list is the parameter)
def len_list(list):
    return len(list)

list=[1,2,3]
print(len_list(list))





# WAP to print the ele of a list in a single line
def print_list(list):
    for i in list:
        print(i,end=" ")
    return

list=[1,2,3]
print_list(list)


# WAF to find the factorial of n(n is parameter)
def fact(n):
    mult=1
    for i in range(1,n+1):
        mult*=i
        print(mult,end=" ")
    return

n=5
fact(n)



# Convert USD to INR
def convert(USD):
    ruppee=90.71*USD
    print(ruppee)
    return

convert(25)