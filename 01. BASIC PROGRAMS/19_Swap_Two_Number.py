# Write a program to swap value of two numbers.

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

temp = a
a = b
b = temp

print("After swaped First Number = ",a)
print("After swaped Second Number = ",b)