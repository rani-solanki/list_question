student_marks=[23,45,67,89,90,54,34,21,34,23,19,28,10,45,86,87]
index=0
less_than50=0
more_than50=0
count1=0
count2=0
while(index<len(student_marks)):
    marks=student_marks[index]
    if marks < 50:
        count1=count1+1
        less_than50=less_than50+student_marks[index]
    else:
        count2=count2+1
        more_than50=more_than50+student_marks[index]
    index=index+1
print("marks more than 50:",more_than50,count2)
print("marks less trhan 50:",less_than50,count1)