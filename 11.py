#*****
n = int(input("\nEnter n: "))
i=1
while i<=n:
   print("*",end="")
   i += 1
#____________________________

"""*
   *
   *
   *
   *"""
n = int(input("\nEnter n: "))
i =1
while i<=n:
    print("*")
    i += 1
#_______________________________
"""*
    *
     *
      *
       *"""
n =int(input("\nEnter n: "))
i = 1
while i<=n:
   print()
   s=1
   while s<=i-1:
       print(" ",end=" ")
       s=s+1
   j=0
   while j<1:
      print("*",end=" ")
      j = j+1
   i = i+1
#____________________________________
"""*****
   *****
   *****
   *****
   *****"""
n=int(input("\nEnter n: "))
i = 1
while i<=n:
    print()
    j=1
    while j<=n:
      print("*",end="")
      j +=1
    i+=1
#__________________________________
"""12345
   12345
   12345
   12345
   12345"""

n=int(input("\nEnter n: "))
i = 1
while i<=n:
   print()
   j = 1
   while j<=n:
      print(j,end="")
      j+=1
   i += 1
#__________________________________
"""11111
22222
33333
44444
55555"""

n=int(input("\nEnter n: "))
i = 1
while i<=n:
   print()
   j = 1
   while j<=n:
      print(i,end="")
      j+=1
   i += 1
#_____________________________

"""1
   00
   111
   0000
   11111"""

n = int(input("\nEnter n: "))
i = 1
while i<=n:
  print()
  j=1
  while j<=i:
    if i%2 == 0:
      print(0,end="")
    else:
      print(1,end="")
    j += 1
  i +=1
#_________________________________
"""*
   **
   ***
   ****
   *****"""

n = int(input("\nEnter n: "))
i= 1
while i<=n:
   print()
   j = 1
   while j<=i:
      print("*",end="")
      j += 1
   i += 1
#____________________________________
"""1
   12
   123
   1234
   12345"""

n = int(input("\nEnter n: "))
i = 1
while i<=n:
   print()
   j = 1
   while j<= i:
       print(j,end="")
       j += 1
   i += 1

#____________________________________
"""1
22
333
4444
55555"""
n = int(input("\nEnter n: "))
i = 1
while i<=n:
   print()
   j = 1
   while j<=i:
      print(i,end ="")
      j += 1
   i += 1
#___________________________________
"""A
   AB
   ABC
   ABCD
   ABCDE"""

n = int(input("\nEnter n: "))
i = 1
while i<=n:
   print()
   j = 1
   while j<=i:
       print(chr(64+j),end="")
       j += 1
   i += 1
#_____________________________________

"""a
   ab
   abc
   abcd
   abcde"""

n = int(input("\nEnter n: "))
i = 1
while i <= n:
   print()
   j = 1
   while j <= i:
      print(chr(96+j),end="")
      j += 1
   i += 1

#_____________________________________________
"""A
   BB
   CCC
   DDDD
   EEEEE"""

n = 5
i = 1
ch= 65
while i<=n:
   print()
   j = 1
   while j<=i:
       print(chr(ch),end="")
       j= j+1
   ch = ch +1
   i += 1















   