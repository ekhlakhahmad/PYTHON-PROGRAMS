# Write a program to implementation of some Arithmatical operation like: add, sub, multiple, division, modulus, division without decimal point, and power.

a = int(input("Enter First Number: "));
b = int(input("Enter Second Number: "));
add = a + b;
print("Addition of Two Number = ",add);

sub = a - b;
print("Subtraction of Two Number = ",sub);

multiple = a * b;
print("Multiplication of Two Number = ",multiple);

div = a / b;
print("Division of Two Number with decimal value = ",div);

mod = a % b;
print("Modular of Two Number = ",mod);

division = a // b;
print("Division of two Number without decimal = ",division);

power = a ** b;
print("Explonancial of the Number = ", power);
