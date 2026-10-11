# Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# # An additional surcharge of 20% is added to the bill
# take values 
units = int(input('Enter the total units :'))
# apllying condition 
if (units <= 50):
    bill = units * 0.05
elif (units >= 150):
    remaining = units - 50
    bill = (50 * 0.05) + (remaining * 0.75)
elif (units >= 250):
    remaining = units - 250
    bill = (50 * 0.05) + (150 * 0.75) + (remaining * 1.20)
else :
    remaining = units - 250
    bill = (50 * 0.05) + (150 * 0.75) + (250 * 1.20) + (remaining * 1.50)

subcharge = bill * 20 / 100
total = bill + subcharge

print('Your electricity bill is :',bill)
print('your subcharge bill is :',subcharge)
print('your total bill is :',total)