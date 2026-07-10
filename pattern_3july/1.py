#WAP to sum of integers between 100 and 200 which is divisible by 9
i = 100
sum = 0
while i<=200:
   if i%9 == 0: 
      sum = sum+i
   i = i+1
print("Sum",sum)