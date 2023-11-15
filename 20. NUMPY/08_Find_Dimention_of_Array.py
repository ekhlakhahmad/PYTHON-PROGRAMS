# CREATE ARRAY AND PRINT IT AS WELL AS FIND DIMENSION OF THOSE ARRAY.

import numpy as np
arr = np.array([6])
print(arr)
print(arr.ndim)

print("\n print array and as well as dimension of those array")

ar2 = np.array([[4,5],[9,8]])
print(ar2)
print(ar2.ndim)

print("\n print array and as well as dimension of those array")

ar3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(ar3)
print(ar3.ndim)

print("\n print array and as well as dimension of those array")

ar4 = np.array([[[[1,2,3],[4,5,6],[7,8,9],[12,12,13]]]])
print(ar4)
print(ar4.ndim)

print("\n print array and as well as dimension of those array")

ar10 = np.array([[[[[[[[[[1,2,3],[4,5,6],[7,8,9],[12,12,13],[3,4,5]]]]]]]]]])
print(ar10)
print(ar10.ndim)

print("\n print array and as well as dimension of those array")

ar20 = np.array([3,4,5],ndmin = 20)
print(ar20)
print(ar20.ndim)