# A brief description of the project
# 09/29/2023
# CTI-110 P1HW2 - Travel Expense
# Edmondson Brandie


#Pseudocode
#var budget, destination, gas, accom, food = input()
#var expenses = gas + accom + food
#var balance =  budget - expenses
#display destination, expenses, balance


print("A program for calculating travel expenses by Brandie.\n")
budget = int(input("What is your travel budget?"))
dest = input("What is your destination?")

amount_gas = int(input("What is your estimated gas budget?"))
amount_accom = int(input("What is accomodation budget?"))
amount_food = int(input("What is your food budget?"))


total_expenses = amount_gas + amount_accom + amount_food
balance = budget - total_expenses

print()
print("............Travel Expenses...........")
print("Destination:", dest)
print("Initial Budget:", budget)
print()
print("Your expenses:")
print("   Fuel:", amount_gas)
print("   Accomodation:", amount_accom)
print("   Food:", amount_food)
print("Total:" , total_expenses)
print("Balance:", balance)
