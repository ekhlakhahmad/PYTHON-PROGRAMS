# Write a program to print Even number and find Sum of No from one to N (1 - N).

n = int(input("Enter any Number: "))
i = 0
sum = 0
while(i < n):
    print(i+2)
    i = i + 2
    sum = sum + i

print("Total Sum of Even No = ",sum)