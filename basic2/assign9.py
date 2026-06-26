n = int(input("Enter number: "))

square = n * n
sum = 0

while square > 0:
    digit = square % 10
    sum += digit
    square = square // 10

if sum == n:
    print("Glowing Success! You've found the Neon Number!")
else:
    print("Try again! Not quite glowing yet.")