# Write a program to check if given 3 digit number is a palindrome or not.
# take values
num = int(input('Enter the 3 digit number :'))
first  = num % 10 
last = num // 100

if first == last :
    print( 'number is palindrome.')
else :
    print( 'number is not palindrome.')
