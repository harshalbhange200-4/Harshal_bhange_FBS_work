#1. Understand that your function is a object of Function class
def demo():
    print('I am in demo')
print(type(demo))
# LHS = RHS

#2. we can stored the function in variable.
def demo():
    print('I am in demo')
x = demo
demo()
x()

#3. we can pass the function a an agrumnet to the another function 
def hi():
    print('I am from hi')
def usit(a):
    print(a)# print (code)
    (a) # it call function print hi
usit(hi)

#4. we can return a function from another function 
def outside():
    print('i am from outside')
    def inside():
        print('i am from inside')
        return inside
ans = outside()
ans()

#5. clausore
def outside(a):
    print('i am from outside',a)
    def inside():
        print('i am from inside',a)
        return inside
ans = outside(10)
ans()

# call decorator

def outside(a):
    print('i am from outside')
    def inside(*a):
        print('i am from inside',a)
        return inside
ans = outside(10)
ans()











