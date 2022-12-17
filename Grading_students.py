def gradingStudents(grades):
    # Write your code here
    global q
    for m in range(len(grades)):
        if 0<grades[m]<38:
            grades[m]=grades[m]
        elif 38<=grades[m]<100:
            for j in range(1, 6):
                q=0
                if (grades[m]+j)%5==0 and (grades[m]+j)-grades[m]<3:
                    grades[m]=grades[m]+j
                    q+=1
                    break
            if q==0:
                grades[m] = grades[m]
    return grades
