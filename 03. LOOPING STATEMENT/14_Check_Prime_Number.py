# Write a program to check the given number is Prime No or Not.

n = int(input("Enter any number: "))
factor = 0
i = 1
while(i <= n):
    if n % i == 0:
        factor = factor + 1
    i = i + 1

if factor == 2:
    print("This Number is Prime Number")

else:
    print("This Number is Not a Prime Number")