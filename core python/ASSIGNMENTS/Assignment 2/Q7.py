# Find the sum of three-digit number.
# take values 
num = int(input('Enter your 3 digit number :'))
# aplly condition 
first = num // 100
second = (num // 10) % 10
third = num % 10

sum = first + second + third 

#display result 
print('the sum of three digit  is :',sum)
