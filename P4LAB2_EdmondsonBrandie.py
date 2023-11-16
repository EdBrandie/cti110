first = int(input())
second = int(input())

if second < first:
    print("Second integer can't be less than the first.")
else:
    for i in range(first, second + 1, 5):
        print(i, end=" ")
    print()