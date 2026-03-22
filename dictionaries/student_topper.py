"""
Program: Student Topper Finder
"""

def find_topper(students):
    return max(students, key=students.get)


def main():
    try:
        no_of_students = int(input("Enter the number of students: "))

        if no_of_students <= 0:
            print("Student count must be greater than zero.")
            return

        info = {}

        for _ in range(no_of_students):
            name = input("Enter the name of the student: ")

            try:
                marks = int(input(f"Enter the marks of {name}: "))

                if 0 <= marks <= 100:
                    info[name] = marks
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter valid integer marks.")

        topper = find_topper(info)
        print(f"{topper} is the topper with {info[topper]} marks.")

    except ValueError:
        print("Please enter a valid number of students.")


if __name__ == "__main__":
    main()