marks = int(input("Enter marks: "))
Grade = ""

if marks > 60:
    if marks >= 90:
        Grade = "A"
    elif marks >= 80:
        Grade = "B"
    elif marks >= 70:
        Grade = "C"
    else:
        Grade = "D"
    print(f"Congrats! You passed with Grade {Grade}")
else:
    print("You failed. Try again.")
