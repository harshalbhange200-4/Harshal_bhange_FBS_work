# A list contains the denominations as follows :
# D = [2000, 500, 200, 100 , 50, 20, 10, 5]
# Accept an amount from user and calculate how many
# minimum number of notes will be needed for that
# amount.
D =[2000,500,200,100,50,20,10,5,2,1]
amount = int(input('Enter the amount :'))
total_notes = 0
for i in D:
    notes = amount // i
    amount = amount % i
    if notes > 0:
        print(i,'Notes =',notes)
    total_notes += notes
print('Total minimum notes =',total_notes)