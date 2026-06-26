"""14.Floor Movement System (Elevator)
An elevator system takes the current floor and destination floor as input.

If current floor < destination → move upward and display floors
If current floor > destination → move downward and display floors
If both are same → display "Already on the same floor"

Write a program using if-elif-else and loops to simulate elevator movement.

Input: 1, 5
Output: 1 → 2 → 3 → 4 → 5

Input: 7, 3
Output: 7 → 6 → 5 → 4 → 3

Input: 4, 4
Output: Already on the same floor"""

#using for loop
cf = int(input("Enter current floor:"))
des = int(input("Enter destination: "))

if cf<des:
   for i in range(cf, des+1):
       print(i,"->",end=" ")
elif cf>des:
   for i in range(cf, des-1,-1):
       print(i,"->",end=" ")
else:
   print("Already on the same floor")
#_______________________________________________________________
#using while loop
cf =int(input("Enter current floor:"))
des =int(input("Enter destination: "))

if cf<des:  
    while cf<=des:
       print(cf,"->",end=" ")
       des = des+1
if cf>des:
    while cf>=des:
       print(cf,"->",end=" ")
       des = des-1
else:
    print("Already on the same floor")



    


