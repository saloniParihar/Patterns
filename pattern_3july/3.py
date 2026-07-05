start = 1990
end = 2025

while start<= end:
   if start%400 == 0 or(start%4 == 0 and start%100 != 0):
           print(start)
   start += 1



