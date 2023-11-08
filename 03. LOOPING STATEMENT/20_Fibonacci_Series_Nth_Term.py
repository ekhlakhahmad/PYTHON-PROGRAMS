#  Write a program to find the fibonacci series Nth Term.

n = int(input("Enter Nth term: "))
x = 0
y = 1
z = 0

i = 1
while(i <= n):
    print(z)
    x = y
    y = z
    z = x + y
    i = i + 1
    