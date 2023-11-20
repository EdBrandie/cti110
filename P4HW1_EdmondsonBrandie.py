# CTI-110
# P4HW1 - Score List
# Edmondson Brandie
# 11/20/2023
#


num_scores = int(input("How many scores do you want to collect?"))
grades = []

for i in range(num_scores):
    score = float(input(f"Enter score #{i + 1}: "))
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i + 1} again: "))
    grades.append(score)

low     = min(grades)
total   = sum(grades)
avg = total / len(grades)

grade = 'F'
if avg >= 90:
   grade = 'A'
elif avg > 80:
   grade = 'B'
elif avg > 70:
   grade = 'C'
elif avg > 60:
   grade = 'D'
elif avg > 50:
   grade = 'E'
else:
   grade = 'F'

print()
print("----------Results---------------------")
print(f"Lowest Grade:      {low}")
print(f"Modified List:     {grades}")
print(f"Average:           {avg:.2f}")
print(f"Grade:             {grade}")
print("--------------------------------------")
