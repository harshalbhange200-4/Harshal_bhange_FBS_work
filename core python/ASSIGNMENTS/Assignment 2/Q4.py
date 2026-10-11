# write a program to calculate area of triangle and rectangle .
# take values
Base = int(input('Enter base : '))
Height = int(input('Enter height : '))
Length  = int(input('Enter length : '))
Breadth = int(input('Enter breadth  : '))
#calculate sum 
# formula - area of triangle = 1/2 * base * Height
# formula - area of rectriangle = len * breadth
Triangle = 1/2 * Base * Height
Rectriangle = Length * Breadth
#display result
print(f'the area of triangle is : {Triangle} and area of rectriangle is : {Rectriangle}.')
