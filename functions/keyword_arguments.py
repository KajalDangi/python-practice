def student_info(**details):
    if not details:
        return {}
    return details

students = []

no_of_students = int(input("Enter number of students: "))
for i in range(no_of_students):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students.append(student_info(Name=name, Marks=marks))

for student in students:
    print(student)
