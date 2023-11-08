# Write a program to find sum of elements of the List.

a = []
n = int(input("How many Element you want to enter: "))
for i in range(n):
    val = int(input("Enter Number: "))
    a.append(val)
sum = 0 
for i in range(n):
    sum = sum + a[i]
print("Sum of List Element = ",sum)