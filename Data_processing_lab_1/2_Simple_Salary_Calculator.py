name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance: "))

gross_salary = basic_salary + allowance

if gross_salary <= 30000:
    tax_rate = 0
elif gross_salary <= 50000:
    tax_rate = 0.05
elif gross_salary <= 80000:
    tax_rate = 0.10
else:
    tax_rate = 0.15

tax = gross_salary * tax_rate
net_salary = gross_salary - tax

print("Employee Name:", name)
print("Gross Salary:", gross_salary)
print("Tax:", tax)
print("Net Salary:", net_salary)