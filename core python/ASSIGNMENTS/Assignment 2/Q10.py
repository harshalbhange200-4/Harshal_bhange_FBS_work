#write a program to revers three-digit number.
# take values 
num = int(input('Enter 3 digit number :'))
# aplly condition 
a = num % 10
b = (num // 10) % 10
c = num // 100
# display result
print(f'the resvers number is : {a}{b}{c}.')
