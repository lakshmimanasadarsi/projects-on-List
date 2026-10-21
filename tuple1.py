students = (
    ("Revathi", 101, 85),
    ("Sita", 102, 92),
    ("manasa", 103, 76)
)

print("=======STUDENT RECORDS=======")

for student in students:
    name = student[0]
    roll_no = student[1]
    marks = student[2]

    print("\nName:", name)
    print("Roll Number:", roll_no)
    print("Marks:", marks)

    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    else:
        print("Grade: C")