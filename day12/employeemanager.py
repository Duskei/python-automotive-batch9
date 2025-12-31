# as a manager you have to evaluate the performance of your reportees. there are 3 managers
# and total 12 reportees. for example: a,b,c are managers and there are 12 reportees
# using the concept of filter, lambda and comprehensions try to implement the concept of
# manager-employee relationship. 
# #one employee can have only one manager but one manager can have multiple employees.

from functools import reduce

# -----------------------------------
# Step 1: Input Managers
# -----------------------------------
num_managers = int(input("Enter number of managers: "))
managers = []

for i in range(num_managers):
    manager = input(f"Enter manager {i+1} name: ")
    managers.append(manager)

# -----------------------------------
# Step 2: Input Employees
# -----------------------------------
num_employees = int(input("\nEnter number of employees: "))
employees = []

for i in range(num_employees):
    print(f"\nEnter details for Employee {i+1}")
    name = input("Employee Name: ")
    manager = input("Manager Name: ")
    performance = int(input("Performance Score (0-100): "))

    employees.append({
        "name": name,
        "manager": manager,
        "performance": performance
    })

# -----------------------------------
# Step 3: Manager → Employees Mapping
# (Dictionary Comprehension)
# -----------------------------------
manager_employee_map = {
    manager: [emp["name"] for emp in employees if emp["manager"] == manager]
    for manager in managers
}

print("\nManager - Employee Mapping:")
for m, e in manager_employee_map.items():
    print(m, "->", e)

# -----------------------------------
# Step 4: High Performers (filter + lambda)
# -----------------------------------
high_performers = list(
    filter(lambda e: e["performance"] >= 80, employees)
)

print("\nHigh Performing Employees (>=80):")
for emp in high_performers:
    print(emp["name"], "-", emp["performance"])

# -----------------------------------
# Step 5: Average Performance Per Manager
# (filter + map + reduce)
# -----------------------------------
manager_avg_performance = {}

for manager in managers:
    manager_emps = list(filter(lambda e: e["manager"] == manager, employees))

    if manager_emps:  # avoid division by zero
        scores = list(map(lambda e: e["performance"], manager_emps))
        avg = reduce(lambda x, y: x + y, scores) / len(scores)
        manager_avg_performance[manager] = avg
    else:
        manager_avg_performance[manager] = 0

print("\nAverage Performance Per Manager:")
for m, avg in manager_avg_performance.items():
    print(m, ":", round(avg, 2))

# -----------------------------------
# Step 6: Best Manager Based on Performance
# -----------------------------------
best_manager = max(
    manager_avg_performance.items(),
    key=lambda x: x[1]
)

print("\n🏆 Best Manager Based on Team Performance:")
print("Manager:", best_manager[0])
print("Average Score:", round(best_manager[1], 2))