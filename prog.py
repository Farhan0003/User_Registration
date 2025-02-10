import re
import logging

logging.basicConfig(filename='password.log',level=logging.DEBUG)

def check_password(password):

    if not re.match (r'^.{8,}$',password):
        logging.warning("Password length is less than 8 characters ")
        return 'Invalid password! your password should contain more than 8 chracters'
    
    if not re.search(r'[A-Z]',password):
        logging.warning("Password does not have upper case")
        return 'Invalid password! your password should have one uppercase'
    
    if not re.search(r'[0-9]',password):
        logging.warning("Password does not have numeric number")
        return 'Invalid password! your password should have one numeric number'
    
    if not re.match(r'^[^@#$%^&*]*[@#$%^&*][^@#$%^&*]*$', password):
        logging.warning("Password does not have Special characters")
        return 'Invalid password! your password should have one special character'
    
    return 'Valid password'




password = input("Enter the password: ")
result=check_password(password)
print(result)
