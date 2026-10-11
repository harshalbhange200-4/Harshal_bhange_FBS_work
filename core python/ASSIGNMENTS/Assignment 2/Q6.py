# Write a program to calculate total salary of employe based on basic , da = 10% of basic , ta = 12% of basic , hra = 15% of basic .
#take values
Basic =int(input('Enter basic salary :'))
# condition aplly
DA = Basic * 10 / 100
TA = Basic * 12 / 100
HRA = Basic * 15 / 100
TOTAL_SALARY = Basic + DA + TA + HRA 
TA = TOTAL_SALARY
# display result
print('The total salary of employee is :',TA)
