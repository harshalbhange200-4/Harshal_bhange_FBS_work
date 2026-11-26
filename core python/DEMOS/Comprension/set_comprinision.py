# wap to create  list of values present in string 
# str = 'i am good in Python'
# newlist = []
# for i in str:
#     if i in 'AEIOUaeiou':
#         newlist.append(i)
# print(set(newlist))

# using set comprision  #####  new topic
str = 'i am good in Python'
newlist = {i for i in str if i in 'AEIOUaeiou'}
print(newlist)