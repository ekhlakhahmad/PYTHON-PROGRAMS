# Write a program to check the character is Small letter or Capital letter.

ch = input("Enter any Character: ")

if ch >= 'A' and ch <= 'Z':
    print("Chapital Character")

elif ch >= 'a' and ch <= 'z':
    print("Small Character")

else:
    print("Wrong Character")