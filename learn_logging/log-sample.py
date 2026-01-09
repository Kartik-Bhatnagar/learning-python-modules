import logging

def adding(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

num1 = 15
num2 = 20

add_result = adding(num1,num2)
print(f"Add : {num1} + {num2} = {add_result}")

sub_result = subtract(num1,num2)
print("Sub: {} - {} = {}".format(num1,num2,sub_result))

mul_result = multiply(num1,num2)
print(f"Add : {num1} + {num2} = {add_result}")

div_result =  divide(num1,num2)
print(f"Add : {num1} + {num2} = {add_result}")
