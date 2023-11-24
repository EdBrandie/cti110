# CTI-110
# P4HW2 - Salary Calculator
# Brandie Edmondson
# 11/24/2023
#

#Pseudo code
#while name <> "done"
#  get name, hours, payrate
#  calculate regular, overtime and gross payments
#  append regular, overtime, gross pay to a list
#calculate cumulative payments
#display cumulative payments

data = []

while True:
   name     = input("Enter employee's name or \"Done\" to terminate:")
   if name == "Done":
       break
   hours    = float(input(f"How many hours did {name} work?"))
   pay_rate = float(input(f"What is {name}'s pay rate?"))

   overtime_hours = 0
   if hours > 40:
      overtime_hours = hours - 40

   overtime_pay = overtime_hours * pay_rate
   regular_pay  = (hours - overtime_hours) * pay_rate
   gross_pay    = regular_pay + overtime_pay
   data.append([overtime_pay, regular_pay, gross_pay])

   print()
   print(f"Employee name: {name:20s}")
   print()
   print("Hours Worked   Pay Rate   Overtime   Overtime Pay   Regular Pay   Gross Pay")
   print("-" * 75)

   str_pay = f"{' ':8s}${overtime_pay:.2f}{' ':9s}${regular_pay:.2f}{' ':8s}${gross_pay:.2f}"

   print(f"{hours}{pay_rate:15.1f}{overtime_hours:10.1f}{str_pay}")
   print()

#Calculate total payments
overtime = 0
regular  = 0
gross    = 0
for v in data:
    overtime += v[0]
    regular  += v[1]
    gross    += v[2]

print()
print(f"Total number of employees entered:", len(data))
print(f"Total amount paid for overtime: $",  overtime)
print(f"Total amount paid for regular hours: $",  regular)
print(f"Total amount paid in gross: $",  gross)


