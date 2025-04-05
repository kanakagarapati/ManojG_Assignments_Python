import re
password = input("Enter your password: ")
def is_password_valid(password):
    password_format = re.search(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password)
    if password_format:
        return True
    else:
        return False
    
if is_password_valid(password):
    print("Password Looks good!")
else:
    print("Password is invalid")
    print("Password should be atleast 8 char long, should be alpha numeric, contains atleast one uppercase, one lowercase and one special character.")