# Write a program to check the year is leap year or normal year.

year = int(input("Enter year: "))

if year % 4 == 0:
    print(year, "is Leap Year")
else:
    print(year, "is Not a Leap Year")
