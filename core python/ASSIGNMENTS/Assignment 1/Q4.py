#Write a program to enter P,Rand T and calculate simple interest.
P =float(input('Enter principal amount :'))
R =float(input('Enter rate intrest :'))
T =float(input('Enter time :'))

#simple intrest = ( P*R*T )/ 100
SI = (P*R*T)/100
print(f'the simple intrest of {P}, {R}, {T} is {SI}')
