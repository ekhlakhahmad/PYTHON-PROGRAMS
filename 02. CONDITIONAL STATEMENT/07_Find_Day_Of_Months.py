# Write a program to find the number of the given months number.

n = int(input("Enter any Month Number: "))

if n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12:
    print("This Months in 31 Days")

elif n == 4 or n == 6 or n == 9 or n == 11:
    print("This Months in 30 Days")

elif n == 2:
    m = int(input("Enter Year: "))
    if m % 4 == 0:
        print("This Months in 28 Days")

    else:
        print("This Months in 29 Days")
    
else:
    print("Invalid Month Number ")