num1 = 42 #variable declaration number
num2 = 2.3 #variable declaration float
boolean = True #initialize boolean
string = 'Hello World' #initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #initialize tuple
print(type(fruit)) #log statement tuple type check
print(pizza_toppings[1]) # log statement list access value
pizza_toppings.append('Mushrooms') # add value
print(person['name']) #log statement dictionary
person['name'] = 'George' #change value
person['eye_color'] = 'blue' #change value typeError
print(fruit[2]) #log statement tuple access value

if num1 > 45: #conditional
    print("It's greater")#log statement
else:
    print("It's lower")#log statement

if len(string) < 5:#conditional
    print("It's a short word!")#log statement
elif len(string) > 15:#conditional
    print("It's a long word!")#log statement
else:#conditional
    print("Just right!")#log statement

for x in range(5):#for loop
    print(x)#log statement
for x in range(2,5):#for loop
    print(x)#log statement
for x in range(2,10,3):#for loop
    print(x)#log statement
x = 0 # variable declaration
while(x < 5):#while loop
    print(x)#log statement
    x += 1 #variable declaration, numbers

pizza_toppings.pop() #delete value
pizza_toppings.pop(1)#delete value

print(person) #log statement
person.pop('eye_color') #delete value
print(person) #log statement

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #conditional
        continue #continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #conditional
        break #break

def print_hello_ten_times(): #initialize function
    for num in range(10): #for loop
        print('Hello') #log statement

print_hello_ten_times() #return function

def print_hello_x_times(x):#initialize function
    for num in range(x): #for loop
        print('Hello') #log statement

print_hello_x_times(4) #return function

def print_hello_x_or_ten_times(x = 10):#initialize function
    for num in range(x): #for loop
        print('Hello') #log statement

print_hello_x_or_ten_times() #return function
print_hello_x_or_ten_times(4) #return function


"""
Bonus section
"""

# print(num3) NameError
# num3 = 72 
# fruit[0] = 'cranberry' TypeError
# print(person['favorite_team']) TypeError KeyError
# print(pizza_toppings[7]) TypeError
#   print(boolean) IndentationError
# fruit.append('raspberry') add value
# fruit.pop(1) delete value