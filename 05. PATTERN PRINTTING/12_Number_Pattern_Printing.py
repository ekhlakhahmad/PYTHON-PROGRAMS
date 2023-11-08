"""Write a code to pattern print

1 1 1 1 1
2 2 2 2
3 3 3
4 4
5

"""

i = 1
while(i <= 5):
    j = 5
    while(j >= i):
        print(i, " ", end="")
        j = j - 1
    print()
    i = i + 1