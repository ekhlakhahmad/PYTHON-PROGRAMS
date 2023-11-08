"""Write a program to accept marks of five (5) subjects and find total mark, percentage and Grade assuming full marks as 100 in each subject. """

math = int(input("Enter marks of math "))
phy = int(input("Enter marks of phy "))
che = int(input("Enter marks of che "))
eng = int(input("Enter marks of eng "))
hin = int(input("Enter marks of hin "))

total = math + phy + che + eng + hin
per = total * 100 / 500
print("Tatal Marks = ",total)
print("Percentage = ",per)

if per >= 90 and per <= 100:
    print("Grade A")

elif per >= 80 and per < 90:
    print("Grade B")

elif per >= 60 and per < 80:
    print("Grade C")

elif per >= 30 and per < 60:
    print("Grade D")

else:
    print("Fail Grade E")