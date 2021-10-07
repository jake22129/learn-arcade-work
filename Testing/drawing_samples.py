my_grades = [65, 98, 100, 95, 92, 93]
print(my_grades[0] + 35)


for row in range(10):

    for j in range(row):
        print(" ", end=" ")

    for j in range(10 - row):
        print(j, end=" ")

    print()