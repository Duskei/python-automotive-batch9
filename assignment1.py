# Employee Salary Management System (Single Employee)

employees = {}

emp_id = input("Employee ID: ")
name = input("Employee Name: ")
department = input("Department: ")

base_salary = float(input("Base Salary: "))
bonus = float(input("Bonus: "))

# Salary calculation
# 10% tax deduction
#addition operation used for adding base_salary and bonus
total_salary = base_salary + bonus

#multiplication operation used to calculate tax
tax = 0.1 * total_salary  

#substraction operation used to calculate net_salary      
net_salary = total_salary - tax

# Store data in dictionary
employees[emp_id] = {
    "name": name,
    "department": department,
    "base_salary": base_salary,
    "bonus": bonus,
    "total_salary": total_salary,
    "tax": tax,
    "net_salary": net_salary
}

# Print salary slip
print("\n========== SALARY SLIP ==========")
print(f"Employee ID   : {emp_id}")
print(f"Name          : {employees[emp_id]['name']}")
print(f"Department    : {employees[emp_id]['department']}")
print("--------------------------------")
print(f"Base Salary   : {employees[emp_id]['base_salary']}")
print(f"Bonus         : {employees[emp_id]['bonus']}")
print(f"Total Salary  : {employees[emp_id]['total_salary']}")
print(f"Tax (10%)     : {employees[emp_id]['tax']}")
print("--------------------------------")
print(f"Net Salary    : {employees[emp_id]['net_salary']}")
print("--------------------------------")