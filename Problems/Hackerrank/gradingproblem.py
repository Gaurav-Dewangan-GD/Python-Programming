def gradingStudents(grades):
    #Write your code here
    for i in range(len(grades)):
        temp = grades[i]
        if temp > 35 and  temp%5 >=3:
            temp = temp + (5-temp%5)
            grades[i] = temp
    return grades
            