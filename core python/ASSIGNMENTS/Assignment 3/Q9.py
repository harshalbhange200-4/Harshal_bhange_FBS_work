# input 5 subject markes from user and  dispaly grade ?
sub_1 = int(input('Enter the subject mark :'))
sub_2 = int(input('Enter the subject mark :'))
sub_3 = int(input('Enter the subject mark :'))
sub_4 = int(input('Enter the subject mark :'))
sub_5 = int(input('Enter the subject marl :'))
sum = sub_1 + sub_2 + sub_3 + sub_4 + sub_5
sum = (sum / 500) * 100
if(sum >= 75 ):
    print('Your grade is : A+')
elif(sum >= 60):
    print('Your grade is : A')
elif(sum >= 50):
    print('Your grade is : B')
elif(sum >= 40):
    print('Your grade is : C')
elif(sum >= 30):
    print('Your grade is : D')
else:
    print('You are fail ')