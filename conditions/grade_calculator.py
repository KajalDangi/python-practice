def calculate_grade(marks):
    if marks < 33:
        return "Fail"
    elif marks >= 90:
        return "O"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"


def main():
    try:
        marks = int(input("Enter your marks (0–100): "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        grade = calculate_grade(marks)

        if grade == "Fail":
            print("You failed the examination. Better luck next time.")
        else:
            print(f"You passed the examination with grade {grade}.")

    except ValueError:
        print("Please enter valid integer marks.")


if __name__ == "__main__":
    main()