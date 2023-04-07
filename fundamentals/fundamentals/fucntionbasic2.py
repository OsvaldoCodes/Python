#countdown
def countdown(x):
    list = []
    for i in range(x,-1,-1):
        list.append(i)
    return list

print(countdown(5))


#Print and return
def print_and_return (list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))


#First Plus Length
def op(my_list):
    return len(my_list) + my_list[0]

print(op([1,2,3,4,5]))


#Values Greater Than Second
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))


#This length, that value

def fun(size,value):
    output=[]
    for i in range(0,size):
        output.append(value)
    return output
print(fun(4,7))
print(fun(6,2))