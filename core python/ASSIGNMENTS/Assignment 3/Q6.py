# write a program to calculate profit or loss .
# take vales 
CP = int(input('Enter the cost price :'))
SP = int(input('Enter the selling price :'))
# coditions
if(SP > CP):
    #display result
    print('the deal is in  : Profit.')
elif(SP < CP):
    print('the deal is in : loss.')
else:
    print('the deal is in : no profit no loss.')


