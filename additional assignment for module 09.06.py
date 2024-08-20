grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
StudentGrade = dict()
studentsAlternate = sorted(students)
a = 0
for i in grades:
    avg = sum(grades[a]) / len(grades[a])
    StudentGrade.update({f'{studentsAlternate[a]}': avg})
    a = a + 1
print(StudentGrade)
