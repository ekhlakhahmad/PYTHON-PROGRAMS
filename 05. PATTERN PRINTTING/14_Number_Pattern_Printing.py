""" Write a code to pattern print input from the user and print same digit 

n n n n n
n n n n
n n n 
n n 
n

"""

n = int(input("Enter any Number: "))
i = 5
while(i >= 1):
    j = 1
    while(j <= i):
        print(n, " ", end="")
        j = j + 1
    print()
    i = i - 1
