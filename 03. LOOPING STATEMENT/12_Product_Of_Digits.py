# Write a program to find the Product of Digits of a Given Number.

n = int(input("Enter any Number: "))
Product = 1
while(n > 0):
    rem = n % 10
    Product = Product * rem
    n = n // 10

print("Product of Digits = ",Product)