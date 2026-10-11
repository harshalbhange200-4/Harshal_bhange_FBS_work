# Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
# take values
total = 0
ticket = float(input('Enter per person ticket amount :'))

age1 = int(input('Enter age of person : '))
age2 = int(input('Enter age of person : '))
age3 = int(input('Enter age of person : '))
age4 = int(input('Enter age of person : '))
age5 = int(input('Enter age of person : '))

if(age1 < 12):
    t1 = ticket -(ticket * 30 /100)
elif(age1 > 59):
    t1 = ticket - (ticket * 50 / 100)
else:
    t1 = ticket 

"""-----------"""

if(age2 < 12):
    t2 = ticket -(ticket * 30 /100)
elif(age2 > 59):
    t2 = ticket - (ticket * 50 / 100)
else:
    t2 = ticket 

"""-----------"""

if(age3 < 12):
    t3 = ticket -(ticket * 30 /100)
elif(age3 > 59):
    t3 = ticket - (ticket * 50 / 100)
else:
    t3 = ticket 

"""-----------"""

if(age4 < 12):
    t4 = ticket -(ticket * 30 /100)
elif(age4 > 59):
    t4 = ticket - (ticket * 50 / 100)
else:
    t4 = ticket 
    
"""-----------"""

if(age5 < 12):
    t5 = ticket -(ticket * 30 /100)
elif(age5 > 59):
    t5 = ticket - (ticket * 50 / 100)
else:
    t5 = ticket 

total = t1 + t2 + t3 + t4 + t5

print('Your total ticket amount is :',total)
