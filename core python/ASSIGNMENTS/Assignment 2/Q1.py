# covert the time entered in hh ,min and sec into seconds?
# take values 
Hours = int(input('Enter hours:'))
Minutes = int(input('Enter Minutes:'))
Seconds = int(input('Enter seconds :'))
#aplly condtion 
# formula = tottal seconds = (hours * 60 * 60) + (Minutes * 60) + seconds
total  = (Hours * 60 * 60) + (Minutes * 60) + Seconds
#display result 
print(f'the hours: {Hours},Minutes :{Minutes} ,seconds : {Seconds} is all in seconds is :{total}')