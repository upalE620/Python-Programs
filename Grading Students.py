def gradingStudents(grades):
    # Write your code here
    l = []
    for i in grades:
        if i >= 38:
            if i % 5 == 3:
                l.append(i + 2)
            elif i % 5 == 4:
                l.append(i + 1)
            else:
                l.append(i)
        else:
            l.append(i)
    return l


if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)
