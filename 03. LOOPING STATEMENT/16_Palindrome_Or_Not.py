# Write a program to check the Number is Palindrome or Not of the given number.

n = int(input("Enter any Number: "))
original = n
reverse = 0
while(n > 0):
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Yes,",original,"is a Palindrome")

else:
    print("No,",original,"is Not a Palindrome")