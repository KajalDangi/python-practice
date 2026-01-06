student_dic = {}
number_of_st = int(input("How many entries? "))

i = 1
while i <= number_of_st:
    name = input("Student name: ")
    marks = int(input("Marks: "))
    student_dic[name] = marks
    i += 1

highest = max(student_dic.values())

toppers = [name for name, mark in student_dic.items() if mark == highest]

print("Topper(s):", toppers)
print("Highest Marks:", highest)
