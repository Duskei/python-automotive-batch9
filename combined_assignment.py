# =========================================================
# Introduction to Scripting
# This script demonstrates Python scripting using
# a Student Course Enrollment example
# =========================================================

print("Welcome to Student Course Enrollment System")

# =========================================================
# Python Variables, Datatypes, Keywords, Comments
# =========================================================

# Taking student name (string)
student_name = input("Enter student name: ")

# Taking student age (integer)
student_age = int(input("Enter student age: "))

# Taking course fee (float)
course_fee = float(input("Enter course fee: "))

# Taking yes/no input and converting it into boolean
is_enrolled = input("Is the student enrolled? (yes/no): ").lower() == "yes"

# Displaying basic datatypes
print("\n--- Basic Datatypes ---")
print("Student Name:", student_name, "| Type:", type(student_name))
print("Student Age:", student_age, "| Type:", type(student_age))
print("Course Fee:", course_fee, "| Type:", type(course_fee))
print("Enrollment Status:", is_enrolled, "| Type:", type(is_enrolled))
#------------------1------------------------------
# =========================================================
# Type Conversion (Casting)
# =========================================================

print("\n--- Type Conversion ---")

# Integer to float
age_float = float(student_age)

# Float to integer
fee_int = int(course_fee)

print("Age as float:", age_float)
print("Course fee as int:", fee_int)

# =========================================================
# Python Operators
# =========================================================

print("\n--- Operators ---")

# Taking marks as input
marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))

# Arithmetic operators
total_marks = marks1 + marks2
print("Total Marks:", total_marks)

# Comparison operators
print("Marks1 > Marks2:", marks1 > marks2)
print("Marks1 == Marks2:", marks1 == marks2)

# Logical operator
print("Both marks are positive:", marks1 > 0 and marks2 > 0)

# Bitwise operator
print("Bitwise AND of marks:", marks1 & marks2)
#-----------------2----------------------
# =========================================================
# Python Control Statements (if, elif, else)

print("\n--- Conditional Statements ---")

# Grade classification
if total_marks >= 180:
    print("Grade: A")
elif total_marks >= 120:
    print("Grade: B")
else:
    print("Grade: C")

# Nested if
if is_enrolled:
    if course_fee > 50000:
        print("Premium Course Student")
    else:
        print("Regular Course Student")

# =========================================================
# Python Loop Control Statements
# =========================================================

print("\n--- For Loop ---")

# Printing subjects list
subjects = ["Maths", "Python", "Data Science", "AI"]

for subject in subjects:
    print(subject)

print("\n--- While Loop ---")

# Countdown example
count = 5
while count > 0:
    print("Countdown:", count)
    count -= 1

# =========================================================
# break, continue, pass
# =========================================================

print("\n--- break, continue, pass ---")

for i in range(1, 6):
    if i == 2:
        continue
    if i == 5:
        break
    print("Value:", i)

# pass example
for _ in range(3):
    pass
#---------------------3---------------------
# =========================================================
# Data Structures (List, Tuple, Dictionary, Set)
# =========================================================

print("\n--- Data Structures ---")

# List
student_scores = [marks1, marks2, 85, 90] #mutable

# Tuple
course_details = ("Python", "6 Months", "Online") #immutable

# Dictionary
student_info = { #key:value pair
    "name": student_name,
    "age": student_age,
    "enrolled": is_enrolled
}

# Set
unique_courses = {"Python", "AI", "ML"} #no duplicate values and unordered

print("Scores List:", student_scores)
print("Course Tuple:", course_details)
print("Student Dictionary:", student_info)
print("Courses Set:", unique_courses)

# Accessing and updating
student_scores.append(95)
student_info["grade"] = "A"
unique_courses.add("Data Science")

print("\nUpdated Scores:", student_scores)
print("Updated Student Info:", student_info)
print("Updated Courses:", unique_courses)

# Slicing list
print("Score Slice:", student_scores[1:4])
#---------------------4---------------------
# =========================================================
# Membership Operator (in)
# =========================================================

print("\n--- Membership Operator ---")
print("Python in courses:", "Python" in unique_courses)
print("Age key exists:", "age" in student_info)

# =========================================================
# String Operations
# =========================================================

print("\n--- String Operations ---")

course_name = "python programming"

print(course_name.upper())
print(course_name.lower())
print(course_name.split())
print("_".join(["Data", "Science", "Course"]))
print("String Slice:", course_name[0:6])
#---------------------5---------------------
# =========================================================
# Functions
# =========================================================

print("\n--- Functions ---")

# Built-in functions
print("Length of course name:", len(course_name))
print("Type of marks:", type(marks1))

# User-defined function
def calculate_average(m1, m2):
    return (m1 + m2) / 2

average = calculate_average(marks1, marks2)
print("Average Marks:", average)

def welcome_student(name):
    return f"Welcome {name} to the course!"

print(welcome_student(student_name))

# =========================================================
# End of Script
# =========================================================

print("\nStudent Course Enrollment Script Executed Successfully ")