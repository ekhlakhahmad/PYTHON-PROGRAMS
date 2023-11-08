# Write a program to print and Sum of the Counting from 1 to N.

n = int(input("Enter any Number where you want to Print & Find sum: "))
i = 1
sum = 0
while(i <= n):
    print(i)
    sum = sum + i
    i = i + 1

print("Total Sum = ",sum)