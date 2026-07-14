n = 5
i = 1
while i<=n:
   print()
   s = 1
   while s<=n-i:
        print(" ",end="")
        s += 1
   j = 1
   while j<= i:
      if j%2 == 0: 
         print(0,end="")
      else:
         print(1,end="")
      j+=1
   i += 1


  
    