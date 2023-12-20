#x = 10
#if x > 5:
#    raise Exception("x is not bigger than 5")
'''
def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception("Password contains least 7 characters")
    elif not re.search("[a-z]", psw):
        raise Exception("Password contains lower case characters")
    elif not re.search("[A-Z]", psw):
        raise Exception("Password contains upper case characters")
    elif not re.search("[0-9]", psw):
        raise Exception("Password contains digits characters")
    elif not re.search("[_@$]", psw):
        raise Exception("Password contains alpha numeric characters")
    elif re.search("\s", psw):
        raise Exception("Password doesnt contain space character")
    else:
        print("Passed Password")
    
password = "1234567aB_"

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("Passed Password: else")
finally:
    print("validation completed.")

'''

class Person:
    def __init__(self,name, year):
        if len(name) > 10:
            raise Exception("name contains more than 10 characters")
        else:
            self.name = name 

p = Person("NurdanKolay",1989)
print(p)