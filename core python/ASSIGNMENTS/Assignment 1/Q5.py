# Write a program to enter P, T,T and calulate compound intrest.
#Take values 
P =float(input('Enter principal amount :'))
R =float(input('Enter rate intrest :'))
T =float(input('Enter time :'))
#claculate amount 
Amount = P * (1 + R / 100)**T
CI =(Amount - P)
#display result 
print(f'The Coumpound intrest of {P},{R}and {T} is {CI}.')

