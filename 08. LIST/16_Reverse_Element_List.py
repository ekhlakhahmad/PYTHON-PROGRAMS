# Write a program to Reverse element in List.

a = []
for i in range(5):
    x = int(input("Enter Number: "))
    a.append(x)
print("Original List is", a)
a.reverse()
print("After Reverse List is: ",a)