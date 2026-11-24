# Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
passenger = int(input('Enter the count of passenger :'))
per_tek_cost =int(input('Enter the cost of ticket :'))
total_cost = 0
for ticket in range(1,passenger+1):
    
    age = int(input('Enter the age of passenger :'))
    if age < 12  :
        discount = (per_tek_cost * 30)/100
        final_cost = per_tek_cost - discount
        
    elif age > 59 :
        discount = (per_tek_cost * 50)/100
        final_cost = per_tek_cost - discount
       
    else :
        final_cost = per_tek_cost
    print('ticket cost :',final_cost)
    total_cost += final_cost
print('Total amount for all passengers :',total_cost)

