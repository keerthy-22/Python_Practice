# Write employee names to the file
with open("Employees.txt", "w") as file:
    file.writelines([
        "Ramesh\n",
        "Sita\n",
        "Karthik\n",
        "Divya\n"
    ])

# Read and display the employee names
with open("Employees.txt", "r") as file:
    employees = file.readlines()
    print("Employee List:")
    print(employees)

# Append new employee names
with open("Employees.txt", "a") as file:
    file.writelines([
        "Harsha\n",
        "Nikhil\n",
        "Pooja\n",
        "Varun\n"
    ])

# Read the updated file
with open("Employees.txt", "r") as file:
    print("\nUpdated Employee List:")
    print(file.read())
