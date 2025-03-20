def average_cal(student_marks,name):
    n=len(student_marks[name])
    total=sum(student_marks[name])
    avg=format((total/n),'.2f')
    return avg