"""Write a program to accept marks of five (5) subjects and find total marks and check student is pass or fail assuming full marks as 100 in each subject. """

math = int(input("Enter marks of math "))
phy = int(input("Enter marks of phy "))
che = int(input("Enter marks of che "))
eng = int(input("Enter marks of eng "))
hin = int(input("Enter marks of hin "))

total = math + phy + che + eng + hin

print("Tatal Marks = ",total)


if total >= 150:
    print("You are Pass")

else:
    print("You are Fail")