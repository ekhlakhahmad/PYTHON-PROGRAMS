# Write a program to find the Greatest Number out of Three Number From the user input.

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a > b and a > c:
    print(a, "is greatest Number")

elif b > a and b > c:
    print(b, "is greatest Number")

elif c > a and c > b:
    print(c, "is greatest Number")

else:
    print("All Nubmer are Equal")