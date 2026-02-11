
# prinint reverse in  recursion

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)


# factorial

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))



# WAP to recursively calc the sum of first n natural numbers
def natural_num(n):
    if(n==1):
        return 1
    return n+natural_num(n-1)

print(natural_num(5))



# WAP to recursively print all the ele in a list
list=["hola","amigo","!","Kaise","ho","theek","ho"]

def print_list(list,idx):
    if(idx==len(list)):
        return 
    print(list[idx])
    print_list(list,idx+1)

print_list(list,0)

    