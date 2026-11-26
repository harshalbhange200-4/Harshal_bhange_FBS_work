li = [1,22,24,65,33,21]
# li1 = []
# for i in li :
#     if i % 2 == 0:
#         li1.append('Even')
#     else :
#         li1.append('odd')
# print(li1)

# using comprinsion
li1 =['Even' if i%2==0 else 'odd' for i in li]
print(li1)
