num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

product = num1 * num2 * num3 * num4
total   = num1 + num2 + num3 + num4
average = total / 4

#Rounded integers
print(f'{product:.0f} {average:.0f}')

#as floats
print(f'{product:.3f} {average:.3f}')