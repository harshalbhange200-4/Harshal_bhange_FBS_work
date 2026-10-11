Gender = input('Enter your (F/M):')
age = int(input('Enter your age :'))

if(Gender == 'F'):
    if(age >= 18):
        print('gril is eligible for lagan .')
    else:
        print('phele pad le bhen ')

else :
    if(age >= 21):
        print('Boy is eligible for lagan .')
    else:
        print('phele kama lo bhai.')