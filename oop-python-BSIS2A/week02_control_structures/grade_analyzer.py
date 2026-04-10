# Name: Bostero, Alexa C.

name_acb = input("Enter student name: ")

g1_acb = float(input("Enter grade 1: "))
g2_acb = float(input("Enter grade 2: "))
g3_acb = float(input("Enter grade 3: "))

average_acb = (g1_acb + g2_acb + g3_acb) / 3

print("\n----- STUDENT GRADE REPORT -----")
print("Student Name:", name_acb)
print("Average Grade:", format(average_acb, ".2f"))

if average_acb >= 90:
    print("Remark: Excellent")
elif average_acb >= 85:
    print("Remark: Very Good")
elif average_acb >= 80:
    print("Remark: Good")
elif average_acb >= 75:
    print("Remark: Fair")
else:
    print("Remark: Failed")