#Hollow square pattern
# for i in range(1 , 6):
#     for j in range(1,i + 1):
#         if(j == 1 or j == 5 or  i == 1  or i == 5 or i == j):
#             print('*', end= ' ')
#         else:
#             print(' ', end= ' ')
#     print()

#Hollow triangle 
# for i in range(1 , 6):
#     for j in range(1 , 6):
#         if j == 1 or i == 5 or i == j :
#             print('*', end= ' ')
#         else:
#             print(' ', end= ' ')
#     print()

#Hollow tringle reverse 
    
for i in range(1 , 6):
    for j in range(1 , 7 - i):
        if(j == 1 or   i == 1  or i + j == 6):
            print('*', end= ' ')
        else:
            print(' ', end= ' ')
    print()



    