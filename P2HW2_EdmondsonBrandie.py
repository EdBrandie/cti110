# CTI-110
# P2HW2 - List
# Edmondson Brandie
# 10/16/2023
#


#Pseudocode
#var grade_m1, grade_m2, grade_m3, grade_m4, grade_m5, grade_m6 = input()
#var grades = [grade_m1, grade_m2, grade_m3, grade_m4, grade_m5, grade_m6]
#var low, high, total, average = min(grades), max(grades), sum(grades),  sum(grades)/len(grades)
#show low, high, total, avaerage


grade_m1 = float(input("Enter grade for Module 1:"))
grade_m2 = float(input("Enter grade for Module 2:"))
grade_m3 = float(input("Enter grade for Module 3:"))
grade_m4 = float(input("Enter grade for Module 4:"))
grade_m5 = float(input("Enter grade for Module 5:"))
grade_m6 = float(input("Enter grade for Module 6:"))

#a list of grades
grades = [grade_m1, grade_m2, grade_m3, grade_m4, grade_m5, grade_m6]

low     = min(grades)
high    = max(grades)
total   = sum(grades)
average = total / len(grades)

print()
print("----------Results-------------")
print(f"Lowest Grade:      {low}")
print(f"Highest Grade:     {high}")
print(f"Sum of Grades:     {total}")
print(f"Average:           {average:.2f}")
print("--------------------------------------")
