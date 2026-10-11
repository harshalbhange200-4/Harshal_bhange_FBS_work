# Write a program to input all sides of a triangle and check whether triangle is valid or not.
# take vales 
Angle_1 = int(input('Enter the angle :'))
Angle_2 = int(input('ENter the angle :'))
Angle_3 = int(input('Enter the angle :'))
# aplly conditions 
triangle = Angle_1 + Angle_2 + Angle_3
#traingle is = 180 its a valid 
#it triangle is graterthe 180 the triangle is not valid and also the triangle is less then 180 its also called not valid .
if(triangle is 180):
#display result
    print('the triangle is valid. ')
else:
    print('the triangle is not valid .')
