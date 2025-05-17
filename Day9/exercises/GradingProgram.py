#Grading program app

student_scores = {
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key in student_scores:
    scores = student_scores[key]
    if scores >= 91 and scores <= 100:
        student_grades[key]="Outstanding"
    elif scores >= 81 and scores <=90:
        student_grades[key]="Exceed Expectations"
    elif scores >= 71 and scores <=80:
        student_grades[key]="Acceptable"
    elif scores<=70:
        student_grades[key]="Fail"

print(student_grades)