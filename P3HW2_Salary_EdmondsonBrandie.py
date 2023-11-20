# CTI-110
# P3HW2 - Salary
# Brandie Edmondson
# 11/02/2023
#

name = input("Enter employee's name:")
hours    = float(input("Enter number of hours worked:"))
pay_rate = float(input("Enter employee's pay rate:"))

overtime_hours = 0
if hours > 40:
    overtime_hours = hours - 40

overtime_pay = overtime_hours * pay_rate
regular_pay  = (hours - overtime_hours) * pay_rate
gross_pay    = regular_pay + overtime_pay

print("-" * 30)
print(f"Employee name: {name:20s}")
print()
print("Hours Worked   Pay Rate   Overtime   Overtime Pay   Regular Pay   Gross Pay")
print("-" * 75)

str_pay = f"{' ':8s}${overtime_pay:.2f}{' ':9s}${regular_pay:.2f}{' ':7s}${gross_pay:.2f}"

print(f"{hours}{pay_rate:15.1f}{overtime_hours:10.1f}{str_pay}")
