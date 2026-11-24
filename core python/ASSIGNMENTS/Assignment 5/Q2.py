# Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.
Student =int(input('Enter the student count :'))
total_per= 0
for students in range(1,Student +1):
    tomarks = 0
    
    for subject in range(1,6):
      marks = int(input('Enter the marks:'))
      tomarks += marks
    print('total marks ',tomarks)
    percentage = (tomarks / 500)*100
    print(percentage)
    
    total_per += percentage

avrege_per = total_per / Student
print('avrage of all student percentage is :',avrege_per)


