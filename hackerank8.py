def gradingStudents(grades):
    #  Write your code here
    actual_grades=[]
    for each_grade in grades:
        val_of_grade = each_grade
        nex_mul_of_five=0
        counter = 0
        while True:
            val_of_grade+=1
            counter+=1
            if val_of_grade%5==0:
                nex_mul_of_five=val_of_grade
                break
        if counter<3 and each_grade>=38:
            actual_grades.append(nex_mul_of_five)
        elif counter>=3 and each_grade>=38:
            actual_grades.append(each_grade)
        elif each_grade<38:
            actual_grades.append(each_grade)

    return actual_grades

grades = [75,73,67,38,33]

print(gradingStudents(grades))