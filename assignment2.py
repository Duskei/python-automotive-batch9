# =========================================================
# Introduction to Scripting
# =========================================================
# This Python script demonstrates scripting concepts,
# data types, operators, I/O, control statements, and loops.

# =========================================================
# Python Variables, Datatypes, Keywords, Comments
# =========================================================

# Taking user input (I/O Expressions)
name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
is_employee = input("Are you an employee? (yes/no): ").lower() == "yes"

# Displaying basic datatypes
print("\n--- Basic Datatypes ---")
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Salary:", salary, "| Type:", type(salary))
print("Is Employee:", is_employee, "| Type:", type(is_employee))

# =========================================================
# Type Conversion (Casting)
# =========================================================
print("\n--- Type Conversion ---")
age_float = float(age)
salary_int = int(salary)
print("Age converted to float:", age_float)
print("Salary converted to int:", salary_int)

# =========================================================
# Python Operators
# =========================================================
print("\n--- Operators ---")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Arithmetic operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Comparison operators
print("a > b:", a > b)
print("a == b:", a == b)

# Logical operators
print("a > 0 and b > 0:", a > 0 and b > 0)

# Bitwise operators
print("Bitwise AND:", a & b)

# =========================================================
# Python Control Statements (if, elif, else)
# =========================================================
print("\n--- Conditional Statements ---")
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Nested if
if is_employee:
    if salary > 50000:
        print("High salary employee")
    else:
        print("Regular salary employee")

# =========================================================
# Python Loop Control Statements
# =========================================================

# For loop
print("\n--- For Loop ---")
n = int(input("Enter a number to print numbers from 1 to n: "))
for i in range(1, n + 1):
    print(i, end=" ")
print()

# While loop
print("\n--- While Loop ---")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# =========================================================
# break, continue, pass
# =========================================================
print("\n--- break, continue, pass ---")
for i in range(1, 6):
    if i == 3:
        continue   # skips 3
    if i == 5:
        break      # stops loop
    print(i)

for _ in range(2):
    pass  # placeholder statement


# =========================================================
# 2D List (List of Lists)
# =========================================================
print("\n--- 2D List ---")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter element [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)

print("2D List (Matrix):")
for row in matrix:
    print(row)

# =========================================================
# Formatting Output
# =========================================================
print("\n--- Formatted Output ---")
print("Hello {}, you are {} years old and earn {:.2f}".format(name, age, salary))
print(f"Name: {name}, Age: {age}, Salary: {salary}")

# =========================================================
# End of Script
# =========================================================
print("\nScript executed successfully.")

