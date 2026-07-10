"""6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong"""

"""#using for loop
n = int(input("Enter n : "))
sum = 0
orig = n
for i in range(len(str(n))):
    digit =n%10
    sum = sum + (digit**3)
    n = n//10
if orig == sum:
   print("Amstrong")
else:
   print("Not Amstrong")"""


#using while loop
n = int(input("Enter n: "))
orig = n
sum = 0
while n>0:
     digit = n%10
     sum = sum+(digit**3)
     n = n//10
if orig == sum:
   print("Amstrong")
else:
   print("Not Amstrong")
    

