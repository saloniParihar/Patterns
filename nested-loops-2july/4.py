
"""Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407"""
#_______________________________________________
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Armstrong Numbers are:")

for i in range(start, end + 1):
    temp = i
    count = 0

    while temp > 0:
        count += 1
        temp //= 10

    temp = i
    s = 0

    while temp > 0:
        digit = temp % 10
        s += digit ** count
        temp //= 10

    if s == i:
        print(i)