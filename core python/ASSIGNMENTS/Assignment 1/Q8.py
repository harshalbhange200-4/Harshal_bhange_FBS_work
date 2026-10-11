# write a program to covert days into years and weeks and days ?
#Take values
Days = int(input('Enter days :'))
#perform task
Years = Days // 365
Remaining  = Days % 365 
Weeks = Remaining // 7
Remaining_days = Weeks % 7 
# display result
print(f'your years is: {Years},weeks is: {Weeks} and days is :{Remaining_days}')

