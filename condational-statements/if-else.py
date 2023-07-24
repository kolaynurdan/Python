if 3>2:
    print('Welcome')

if 3>3:
    print('Welcome')

isLoggedin = True

if isLoggedin:
    print('Welcome')

username = 'nurdan'
password = '123'

if (username == 'nurdan') and (password == '123'):
    print('Welcome')
else:
    print('username or password is wrong!')

if (username == 'nurdan'): 
    if (password == '123'):
        print('Welcome')
    else:
        print('passowrd is wrong')
else:
    print('username is wrong!')