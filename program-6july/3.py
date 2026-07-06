"""3.

Fibonacci Population Growth Tracker

A wildlife research team is studying the growth of a rare species.  
They observe that the population follows a Fibonacci pattern:

- Month 1 → 0 animals  
- Month 2 → 1 animal  
- Every next month → sum of previous two months  

The researchers want to analyze the growth pattern.

Write a program to:

- Read number of months n
- Generate Fibonacci series up to n months using loop
- Print population for each month
- Find total population observed
- Count how many months population exceeded 5

Input:
8

Output:
Population Growth:
0 1 1 2 3 5 8 13"""

n= int(input("Enter numbe of months: "))
a= 0
b= 1
count=0
total = 0
temp = 0
while count<n:
   total += a
   if a > 5:
      temp += 1
   print(a,end =" ")
   c=a+b
   a=b
   b=c
   count += 1

print("Month population exceeded by 5: ",temp)
print("Total population observed: ",total)



  

