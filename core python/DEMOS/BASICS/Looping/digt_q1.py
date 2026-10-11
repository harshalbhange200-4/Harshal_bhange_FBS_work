# take values
num = int(input('Enter number :'))
sum = 0
# condition 
while(num > 0):
    d = num % 10
    sum += d
    num = num // 10
    print('num :',num)#Display resulat