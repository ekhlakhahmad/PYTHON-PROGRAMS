# Write a program to check the character is Vowel or Consonant.

ch = input("Enter any Character: ")

if ch >= 'a' and ch <= 'z' or ch >= 'A' and ch <= 'Z':    
    if ch == 'a' or ch == 'A' or ch == 'e' or ch == 'E' or ch == 'i' or ch == 'I' or ch == 'o' or ch == 'O' or ch == 'u' or ch == 'U':
        print("Vowel Character")
    else:
        print("Consonant Character")    
else:
    print("Invalid Character")