#progrom to find the roots of Quadratic equation ?
# take values
import math
a =int(input('Enter your number :'))
b =int(input('Enter your number :'))
c =int(input('Enter your number :'))
# calculation 
# formula  
# x1= (-b+-//(b**2-4ac))/21
# condition aplly
d = b**2 - 4*a*c
x1 =( -b+ math.sqrt(d)) / (2*a)
x2 =( -b-math.sqrt(d)) / (2*a)

print(f' the value of x1 is {x1}  and x2 is {x2}')


