# Write a program to find the Sum of Digits of a Given Number.

n = int(input("Enter any Number: "))
sum = 0
while(n > 0):
    rem = n % 10
    sum = sum + rem
    n = n // 10

print("Sum of Digits = ",sum)