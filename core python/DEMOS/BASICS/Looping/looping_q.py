num = int(input('Enter the number :'))

for i in range( 2 , num ):
    if(num % i == 0):
    
        print(f'{num} not prime number .')
        break
    else:
        print(f'{num} is a prime number .')
else:
     print(f'{num} prime number.')

# home work
#1. print prime numbers between 1 to n .
#2. print first n prime number .