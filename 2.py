#square root , cube , and square 
import math
n = int(input("Enter n:"))
i = 1
while i<=n:
    print("Square:",i**2,end=" ")
    print("Cube: ",i**3,end=" ")
    print("Square root:",math.sqrt(i),end = " ")

    i = i+1
