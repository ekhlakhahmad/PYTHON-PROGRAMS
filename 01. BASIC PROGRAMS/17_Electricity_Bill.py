# Write a program to accept electricity unit consumption and calculate total price of the rate of Rs. 5 unit. Give a discount of 10% on all over bill.

unit = int(input("Enter electricity unit :"))
ans = unit * 5
dis = ans * 10/100
total = ans - dis
print("After discount of 10 % total electricity bill = ",total)