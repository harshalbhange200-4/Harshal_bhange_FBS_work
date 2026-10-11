# Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)
# take values
gender = input('Enter the gender (male/female):')
age = int(input('Enter the age :'))
# aplly condition 
if( gender == 'male' and age >= 21):
    print('you are eligible to marry.')
elif( gender == 'female' and age >=18):
    print('you are eligible to marry .')
else:
    print('you are not eligible to marry .')