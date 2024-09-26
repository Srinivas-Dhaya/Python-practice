m =  int(input("Marks in Math : "))
s =  int(input("Marks in Science : "))
e =  int(input("Marks in English : "))

total_marks = m+s+e
average = total_marks/3
percentage = (total_marks/3)*100

grade = " "
if percentage > 90:
    grade = "A"
elif percentage > 80 and percentage <=90:
    grade = "B"
elif percentage > 70 and percentage <=80:
    grade = "C"
else:
    grade = "pass"
print(f"Total marks : {total_marks}\nAverage marks : {average}\nGrade : {grade}")