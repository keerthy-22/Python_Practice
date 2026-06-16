emp_no = int(input("Enter Employee No: "))
emp_name = input("Enter Employee Name: ")
salary = float(input("Enter Salary: "))
if salary <= 30000:
    ta = salary * 0.07
    da = salary * 0.09
    hra = salary * 0.11
    pf = salary * 0.15
elif salary <= 50000:
    ta = salary * 0.12
    da = salary * 0.13
    hra = salary * 0.17
    pf = salary * 0.22
else:
    ta = salary * 0.17
    da = salary * 0.19
    hra = salary * 0.21
    pf = salary * 0.25
gross_salary = salary + ta + da + hra
net_salary = gross_salary - pf
print("\nEmployee No :", emp_no)
print("Employee Name :", emp_name)
print("Salary :", salary)
print("TA :", ta)
print("DA :", da)
print("HRA :", hra)
print("PF :", pf)
print("Gross Salary :", gross_salary)
print("Net Salary :", net_salary)
