
"""Count Odd Digits*
A banking system flags IDs with too many odd digits for further verification.
Write a program to *count the number of odd digits in a given number using loops*.

Input: 123456
Output: Odd digits count = 3"""



#using for loop
n = int(input("Enter n: "))
count = 0
for i in str(n):
    if int(n)%2 != 0:
      count =count+1

print("odd digit count: ",count)

# using while loop
n = int(input("Enter n : "))
count = 0
while n>0:
    digit = n%10
     
    if digit%2 != 0:
       count = count+ 1
    n = n//10
print("Odd digit count: ", count)
