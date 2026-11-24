# WAP to print Armstrong number within a given range
start = int(input('Enter the start of range :'))
end = int(input('Enther the end of range :'))
for i in range(start,end+1):
    count = 0
    temp = i
    while temp != 0:
        count += 1
        temp = temp//10
    sum = 0   
    temp = i
    while temp != 0:
       digit = temp % 10
       sum += digit ** count
       temp = temp // 10
    
    if sum == i :
     print(i)


