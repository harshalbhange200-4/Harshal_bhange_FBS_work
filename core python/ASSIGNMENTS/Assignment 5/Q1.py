# Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.
uid = 'admin'
pas = '1234'
attempt = 0
while attempt < 3:
    userid = input('Enter userid :')
    password = input('Enter the password :')

    if uid == userid and pas == password:
        print('Login Successfully')
        break
    else :
        print('incorrect id OR Password')
        attempt += 1
if attempt == 3:
    print('your account is blocked')