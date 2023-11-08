# Write a program to accept total sales amount and find the profit amount @ 5%.

s = int(input("Enter total sales = "))
per = s * 5 / 100
profit = s - per
print("Profit Amount = ",profit)