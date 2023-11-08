# Write a program to print the Reverse of the given number.

n = int(input("Enter any Number: "))
reverse = 0
while(n > 0):
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reverse Number = ",reverse)