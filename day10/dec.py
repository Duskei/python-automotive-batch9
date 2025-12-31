#create a decorator named as calculator that will perform addition of two numbers
#by using the decorator @calculator.
def calculator(func): #taking function(add) as argument
    def mycalc(a, b):
        result1 = func(a, b) #calling the add function
        result2 = sub(a, b) #calling the sub function
        return result1*result2 #returns the product of addition and subtraction
    return mycalc

@calculator
def add(x, y):
    return x + y

#outer function
def sub(x, y):
    return x - y

print("final result is: ", add(10, 20))