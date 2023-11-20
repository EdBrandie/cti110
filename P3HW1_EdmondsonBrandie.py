# Fix bugs in the given program
# 11/02/2023
# CTI-110 P3HW1 - Fix Bugs
# Brandie Edmondson
#


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low    = min(grades)
high   = max(grades)
total  = sum(grades)
avg    = total / len(grades)
total_marks = len(grades) * 100

print('--------------Results--------------')
print(f'Lowest Grade:        {low:.1f}')
print(f'Highest Grade:       {high:.1f}')
print(f'Sum of Grades:       {total:.1f}/{total_marks:.1f}')
print(f'Average:             {avg:.2f}')
print('----------------------------------')

# determine letter grade for average

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
    
print(f'Your grade is: {grade}') #show grade





