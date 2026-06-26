"""Check All Digits Are Even*
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to *check whether all digits of a number are even using loops*.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even"""

#using for loop 
n = int(input("Enter n : " ))
All_even = True

for i in str(n):
    if int(n)%2 != 0:
        All_even = false
if All_even:
   print("All even")
else:
   print("Not All even")


#using while loop
n = int(input("Enter n: "))
All_even = True

while n < 0:
   digit =n%10

   if digit%2 != 0:
       All_even = false
       break

   n = n//10
if All_even:
   print("All even")
else:
   print("Not All even")


   
    