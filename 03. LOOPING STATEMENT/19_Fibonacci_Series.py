#  Write a program to find the fibonacci series till given number.

n = int(input("Enter max term: "))
x = 0
y = 1
z = 0
while(z <= n):
    print(z)
    x = y
    y = z
    z = x + y
    