# Write a program to print first n prime numbers.
n = int(input('Enter the number: '))

num = 2
count = 0

while count < n:
    c = 0

    for i in range(2, num):
        if num % i == 0:
            c += 1

    if c == 0:
        print(num)
        count += 1

    num += 1 