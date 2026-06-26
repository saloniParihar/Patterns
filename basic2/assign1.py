"""1. Largest Digit in Number
A cybersecurity company checks numeric passwords used in smart lockers. To identify password strength, the system finds the highest digit present in the entered password. Higher digits indicate stronger variation in the password pattern.
Write a program to find the largest digit in a number using loops.

Input:
57294

Output:
Largest Digit = 9"""

#____________________________________________________________________
#using while loop
n = int(input("Enter number: "))
largest = 0
 
while n>0:
   digit = n%10
   if digit>largest:
       largest = digit
   n=n//10
print("Largest Digit= ",largest)

   
