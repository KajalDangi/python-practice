"""
Student Percentage Management System

Features:
- Accept multiple students
- Accept dynamic number of subjects
- Validate inputs (IDs, marks, duplicates)
- Calculate percentage
- Display formatted student report
"""

def percent(marks: dict) -> float:
    """
    Calculate percentage from subject marks.
    Assumes all subjects are out of 100.
    """
    return round(sum(marks.values()) / len(marks), 2)


def student_details(name: str, student_id: int, marks: dict) -> str:
    """
    Generate formatted student details.
    """
    if not marks:
        return f"{name} (ID: {student_id}) was absent."

    return (
        f"Name       : {name}\n"
        f"Student ID : {student_id}\n"
        f"Percentage : {percent(marks)}%\n"
        f"Marks      : {marks}\n"
    )



while True:
    try:
        number_of_students = int(input("Enter the number of students: "))
        if number_of_students <= 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid positive number.")

results = []

for i in range(1, number_of_students + 1):
    print(f"\n--- Student {i} ---")
    name = input("Enter student name: ")

    while True:
        try:
            student_id = int(input("Enter student ID: "))
            break
        except ValueError:
            print("Student ID must be numeric.")

    while True:
        try:
            no_of_subjects = int(input("Enter number of subjects studied: "))
            if no_of_subjects < 0:
                raise ValueError
            break
        except ValueError:
            print("Enter a valid number (0 or more).")

    subjects = {}

    for _ in range(no_of_subjects):
        subject_name = input("Enter subject name: ")

        if subject_name in subjects:
            print("Subject already entered. Skipping.")
            continue

        while True:
            try:
                marks = int(input(f"Enter marks for {subject_name}: "))
                if 0 <= marks <= 100:
                    subjects[subject_name] = marks
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Marks must be numeric.")

    results.append(student_details(name, student_id, subjects))


print("\n======= STUDENT REPORT =======\n")
for record in results:
    print(record)

