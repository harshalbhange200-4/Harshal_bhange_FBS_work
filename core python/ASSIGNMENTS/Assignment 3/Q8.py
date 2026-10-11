# write a program to prompt user has entered correct userid and password .after verifying userid and password display a 4 digit random number and ask user to enter the same . if user enters the same number then show him sucess massage otherwise failed .(something like captcha)
# take values 
import random
User_c = 'harshal'
Password_c = '1234'
User = input('Enter user name :')
Password = input('Enter possword :')
# condition 
if(User_c == User and  Password_c == Password):

    num = random.randint(1000,9999)
    print('LOGIN SUCCESFULLY')
    print(' but enter your varification code :',num)

    user_num = int(input('Enter the code:'))
    if user_num == num :
        print(' login sucess')
    else:
        print('login failed')

else :
    print('INVALID')


