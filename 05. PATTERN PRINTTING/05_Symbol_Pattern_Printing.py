"""Write a code to this pattern print.

* * * * *
  * * * *
    * * *
      * *
        *

"""
for i in range(5, 0, -1):
    for j in range(i, 5):
        print(" ", end="")
    
    for k in range(0, i):
        print("*", end="")
    
    print()