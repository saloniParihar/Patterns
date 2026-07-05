start = int(input("Enter start year: "))
end = int(input("Enter end year: "))

count = 0

for year in range(start, end + 1):

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year, "-> Event Scheduled")
        count += 1
    else:
        print(year, "-> No Event")

print("Total Leap Years =", count)
print("Total Events Scheduled =", count)
