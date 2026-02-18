from functools import reduce

# -----------------------------------
# Step 1: Input EXACTLY 3 Managers
# -----------------------------------
managers = []

print("Enter details for 3 Managers:")
for i in range(3):
    manager = input(f"Enter manager {i+1} name: ")
    managers.append(manager)

# -----------------------------------
# Step 2: Input EXACTLY 12 Employees
# -----------------------------------
employees = []

print("\nEnter details for 12 Employees:")
for i in range(12):
    print(f"\nEmployee {i+1}")
    name = input("Employee Name: ")

    # Ensure employee reports to only one valid manager
    while True:
        manager = input(f"Manager Name {managers}: ")
        if manager in managers:
            break
        print("Invalid manager! Choose from:", managers)

    performance = int(input("Performance Score (0-100): "))

    employees.append({
        "name": name,
        "manager": manager,
        "performance": performance
    })

# -----------------------------------
# Step 3: Manager → Employees Mapping
# Dictionary Comprehension
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
# filter + map + reduce
# -----------------------------------
manager_avg_performance = {}

for manager in managers:
    manager_emps = list(filter(lambda e: e["manager"] == manager, employees))

    scores = list(map(lambda e: e["performance"], manager_emps))
    avg = reduce(lambda x, y: x + y, scores) / len(scores)

    manager_avg_performance[manager] = avg

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