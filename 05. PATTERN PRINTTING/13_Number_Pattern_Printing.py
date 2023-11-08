"""Write a code to pattern print

5 5 5 5 5
4 4 4 4 
3 3 3
2 2 
1

"""

i = 5
while(i >= 1):
    j = 1
    while(j <= i):
        print(i, " ", end="")
        j = j + 1
    print()
    i = i - 1