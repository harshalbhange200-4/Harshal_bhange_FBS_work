# covert distent given in feet and inches into meter and centimeter
# take values
Feet = float(input('Enter feet :'))
Inches = float(input('Enter inches : '))
# aplly condition 
# 1 feet = 0.3048 meter 
# i inch = 2.54 centimeter
Meter = Feet * 0.3048
Centimeter = Inches * 2.54 
# display result
print(f'covertion of Inche to meter is :{Feet} to {Meter} and inches to centimeter is : {Inches} to {Centimeter}.')