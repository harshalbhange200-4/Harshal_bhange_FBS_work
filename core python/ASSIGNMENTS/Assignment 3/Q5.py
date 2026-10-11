# Write a program to check whether the triangle is equilateral , isosceles or scalene triangles.
#take values
angle_1 = int(input('Enter the angle :'))
angle_2 = int(input('Enter the angle :'))
angle_3 = int(input('Enter the angle :'))
# conditions 
if(angle_1 == angle_2 and angle_2 == angle_3):
    #DISPLAY RESULT
    print('The triangle is : Equilateral ')
elif(angle_1 == angle_2) or (angle_2 == angle_3 or angle_1 == angle_3):
    print('The triangle is : Isosceles ')
else:
    print('The triangle is : Scalene')