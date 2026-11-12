# method 1
def seq (n):
    return n*n
data = [1,2,3,4,5,6,7,8,9,10]
res =list(map(seq,data))
print(res)

#method 2 using lambda 
data = [1,2,3,4,5,6,7,8,9,10]
res = list(map(lambda n:n ** 2, data))
print(res)
