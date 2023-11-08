# Write a program to Add two Number with argument take input from user using function.

def add(a, b):
    c = a + b
    return c

x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

z = add(x, y)
print("Addition = ", z)