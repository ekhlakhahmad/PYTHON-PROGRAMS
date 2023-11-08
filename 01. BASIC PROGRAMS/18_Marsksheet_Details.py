"""Write a program to accept marks of five (5) subjects and find total marks and percentage assuming full marks as 100 in each subject. """

math = int(input("Enter marks of math "))
phy = int(input("Enter marks of phy "))
che = int(input("Enter marks of che "))
eng = int(input("Enter marks of eng "))
hin = int(input("Enter marks of hin "))

total = math + phy + che + eng + hin
per = total * 100 / 500
print("Tatal Marks = ",total)
print("Percentage = ",per)