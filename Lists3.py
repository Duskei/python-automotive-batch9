students=[100, 66, 70, 88, 90,30, 44, 50, 0]

students_passed=[i if i>=60 else "Failed" for i in students]
print(students_passed)