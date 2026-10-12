# write a program to calaculate simple intrest based on principal ,rate and time .
# take values 
P = int(input('Enter the pricipal :'))
T = int(input('Enter the time :'))
R = int(input('Enter the intrest  rate :'))
# conditions 
SI = (P * R * T) / 100
#display result 
print('simple intrest of P,T and R is :',SI)
