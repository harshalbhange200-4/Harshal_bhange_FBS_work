#Pyramind pattren

# for i in range(1 , 6):
#     for j in range(1 , 6 - i):
#         print(' ' , end=' ')
#     for j in range(1 , i + 1):
#         print('*', end=' ')
#     print()


for i in range(1,6):
    for j in range(1, 6 - i):
        print(' ',end=' ')
    for j in range(1, i  + 1):
        print('*',end=' ')
    for j in range(1, i):
        print('*', end=' ')
    print()


# #reverse 
# for i in range(5, 0, -1):
#     for j in range(5 - i):
#         print(' ', end=' ')
#     for j in range(2 * i - 1):
#         print('*', end=' ')
#     print()