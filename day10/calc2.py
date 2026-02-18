def calculator(func):
    def inner(a, b):
        return func(a, b) # calls the function as per user choice
    return inner

#defining functions for different operations

@calculator
def add(x, y):
    return x + y

@calculator
def sub(x, y):
    return x - y    

@calculator
def multiply(x, y):
    return x * y

@calculator
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"


print("Select operation:")
print("1. add")
print("2. sub")
print("3. multiply")
print("4. divide")
choice = input("Enter choice of operation: ")


# Convert inputs to floats to handle decimals
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 'add' or choice == '1':
    print(f"Result: {add(num1, num2)}")
elif choice == 'sub' or choice == '2':
    print(f"Result: {sub(num1, num2)}")
elif choice == 'multiply' or choice == '3':
    print(f"Result: {multiply(num1, num2)}")
elif choice == 'divide' or choice == '4':
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid Input")