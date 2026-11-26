# with using dictionary

# li = {}
# for i in range(11,26):
#     li[i] = i*i
# print(li)

# use compre
dic = {i : i * i  for i in range (11,26) if i % 2 != 0}
print(dic)

