"""2. Factorial of a Number
In project scheduling, tasks are dependent on previous tasks, and the total number of ways to arrange them is calculated using factorial. Factorial of a number n is the product of all numbers from 1 to n.
Write a program to calculate the *factorial of a given number using loops*.

Input: n = 5
Output: Total Ways = 120"""

#____________________________________________________

#using for loop

"""n = int(input("Enter n:"))
fact = 1
for i in range(1,n+1):
     fact = fact*i
print("Total Ways: ",fact)"""
#_____________________________________________________

#using while loop

n = int(input("Enter n:"))
fact = 1
i = 1
while i <= n:
      fact = fact*i
      i += 1
print("Total ways: ",fact)