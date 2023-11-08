# Write a program to check the given number is Armstrong Number or Not.

n = int(input("Enter any Number: "))
original = n
square = 0
while(n > 0):
    digit = n % 10
    temp = digit ** 3
    square = square + temp
    n = n // 10

if original == square:
    print("Yes,",original,"is a Armstrong Number")

else:
    print("No,",original,"is Not a Armstrong Number")