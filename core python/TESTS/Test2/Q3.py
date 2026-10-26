#3.


length = float(input('Enter wall length: '))
height = float(input('Enter wall height: '))
rate = float(input('Enter  rate per sq unit: '))

area = length * height * 4
cost = area * rate

print('Total painting cost =', cost)
