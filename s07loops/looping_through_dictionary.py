student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

for grades in student_grades.items():
    print(grades)

for name in student_grades.keys():
    print(name)

for grade in student_grades.values():
    print(grade)

for name, grade in student_grades.items():
    print("{} has the grade {}".format(name, grade))
