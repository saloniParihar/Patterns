"""Count Even Digits*
A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are even.
Write a program to *count the number of even digits in a given number using loops*.

Input: 123456
Output: Even digits count = 3"""
#_____________________________________________
#using for loop
"""n = input("Enter n: ")
count =0
for i in str(n):
    if int(i)%2 == 0:
       count = count+1
print("Even digits count = ",count)"""

# using while loop
n = int(input("Enter n : "))
count = 0

while n>0:
    digit = n %10

    if digit%2 == 0:
       count = count+1

    n = n//10
print("Even digit count = ",count)