"""12. Multiplication of Digits*
A puzzle game calculates a score by multiplying all digits of a number together. After calculating the score, the game also checks whether the final score is even or odd to assign a bonus.
Write a program to *find the product of all digits of a number using loops and then check whether the result is even or odd*.

Input: 1234
Output: 24
Even"""

#___________________________________________________________
#using for loop
n = int(input("Enter n : "))
pro = 1
for i in range(len(str(n))):
      digit = n%10
      pro = pro*digit
      n = n//10
      
print(pro)
if pro%2 == 0:
    print("even")
#___________________________________________________

      
n = int(input("Enter n : "))
pro = 1

while n>0:
     digit = n%10
     pro = pro*digit
     n = n//10
        
print(pro)
if pro%2 == 0:
    print("even")
#___________________________________________________
       
