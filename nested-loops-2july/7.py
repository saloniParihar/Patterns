
"""Neon Number Detector

Scenario:
A smart calculator system checks special numbers used in mathematical testing.
The user enters a range of numbers.
The system identifies all Neon Numbers using nested loops.

Theory:
A Neon Number is a number where the sum of digits of its square is equal to the original number.

Example:
9

Square of 9 = 81

8 + 1 = 9

Since the sum is equal to the original number, 9 is called a Neon Number.

Input:
Enter starting number: 1
Enter ending number: 100

Output:
Neon Numbers are:
1
9"""
#________________________________________________________
classes = int(input("Enter number of classes: "))
students = int(input("Enter students per class: "))
subjects = int(input("Enter subjects per student: "))

for i in range(1, classes + 1):
    print("Class", i)

    for j in range(1, students + 1):
        total = 0

        print("Student", j)

        for k in range(1, subjects + 1):
            mark = int(input("Enter mark: "))
            total += mark

        print("Student", j, "Total =", total)

    print()