# Write a program to remove or discard the element from set.

a = {1,2,3,4,5,6,7,8,9}
a.remove(5)
print(a)

b = {"Ekhlakh", "Ahmad"}
b.remove("Ahmad")
print(b)

c = {"siwan", "bihar", "mca", 786}
c.discard("bihar")
print(c)

d = {'a', "bihar"}
d.discard("patna")
print(d)

e = {"SAGAR", 'SONPAL', "NITESH"}
e.remove("EKHLAKH")
print(e)