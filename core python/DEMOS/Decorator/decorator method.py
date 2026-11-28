# main Decorator 
def outerfun(a):
    print('I am in Decorator...')
    def inerfun():
        print('Time Started...')
        a()
        print('Time Stoped...')
    return inerfun
@outerfun
def login():
    print('Login is Done...')
login()
@outerfun
def logout():
    print('Logout is Done...')
logout()
