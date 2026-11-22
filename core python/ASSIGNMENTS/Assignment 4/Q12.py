# Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# # 4*4*4*4)
n = int(input('Enter the number: '))
temp = n
count = 0
sum = 0

# Count total digits
while n > 0:
    count += 1
    n = n // 10

n = temp

# Calculate Armstrong number
while n > 0:
    digit = n % 10
    sum = sum + digit ** count
    n = n // 10

if sum == temp:
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')