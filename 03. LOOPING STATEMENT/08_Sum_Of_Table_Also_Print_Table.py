# Write a program to Print the any number of Table and find the Sum of Table.

n = int(input("Enter any Number: "))
i = 1
sum = 0
while(i <= 10):
    temp = n * i
    sum = sum + temp
    print(n,"x",i,"=",temp)
    i = i + 1

print("Total Sum of Table =",sum)