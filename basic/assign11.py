"""*11. Count Occurrence of a Digit*
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to *count how many times a given digit appears in a number using loops*.

Input: Number = 122312, Digit = 2
Output: 3"""
#_______________________________________________
#using for loop
n = int(input("Enter number: "))
count = 0
target = 2

for i in range(len(str(n))):
    digit = n%10
    if target == digit:
       count = count +1
    n = n//10
print(count)
#________________________________________________
#usign while loop
n = int(input("Enter number: "))
count = 0
target = 2

while n>0:
      digit = n%10
      if target == digit:
         count = count + 1
      n = n//10
print(count)
