"""5. Palindrome Check
A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to *check whether a given number is a palindrome using loops*.

Input: 121
Output: Palindrome"""

#______________________________
#Using for loop
"""n = input("Enter n : ")
orig = n
rev = ""
for i in n:
    rev = i + rev
if rev == orig:
   print("Palindrome")
else:
   print("Not Palindrome")"""
#________________________________

# also for i in range(len(str(n))
#using while loop
n = int(input("Enter n: "))
rev=0
orig = n
while n >0:
     rev = rev*10 + n%10
     n = n//10
if rev == orig:
   print("Palindrome")
else:
   print("Not Palindrome")
