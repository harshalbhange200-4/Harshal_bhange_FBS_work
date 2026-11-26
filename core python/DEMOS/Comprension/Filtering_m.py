li = [12,1,17,11,22]
# li2 =[]
# for i in li:
#     if i % 2 != 0:
#         li2.append(i**2)
# print(li2)


li2 = [i*i for i in li if i % 2 != 0]
print(li2)

