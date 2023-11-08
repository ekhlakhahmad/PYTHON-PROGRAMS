"""Write a code to this pattern print.

* * * * * 
* * * *
* * * 
* *
*

"""
i = 5
while(i >= 1):
    j = 1
    while(j <= i):
        print("*  ", end="")
        j=j+1    
    print()
    i = i - 1