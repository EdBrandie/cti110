# A brief description of the project
# 09/10/2023
# CTI-110 P2HW1 - Travel Expense
# Edmondson Brandie


#Pseudocode
#var budget, destination, gas, accom, food = input()
#var expenses = gas + accom + food
#var balance =  budget - expenses
#display destination, expenses, balance


print("A program for calculating travel expenses by Brandie.\n")
budget = float(input("What is your travel budget?"))
print()
dest = input("What is your destination?")
print()
amount_gas = float(input("What is your estimated gas budget?"))
print()
amount_accom = float(input("What is accomodation budget?"))
print()
amount_food = float(input("What is your food budget?"))
print()


total_expenses = amount_gas + amount_accom + amount_food
balance = budget - total_expenses

print()
print("----------Travel Expenses-------------")
print(f"Destination:     {dest}")
print(f"Initial Budget:  ${budget:.1f}")
print(f"Fuel:            ${amount_gas:.1f}")
print(f"Accomodation:    ${amount_accom:.1f}")
print(f"Food:            ${amount_food:.1f}")
print("--------------------------------------")
print(f"Balance:         ${balance:.1f}")
