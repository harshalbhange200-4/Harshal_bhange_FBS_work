#Nested comprinsion 
# li = []
# for i in range(1,4):
#     for j in range(1,4):
#         li.append([i,j])
# print(li)

# using nested com method 
nli = [[i,j] for i in range(1,4) for j in range(1,4)]
print(nli)

