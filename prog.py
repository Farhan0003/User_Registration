
import re
import logging

logging.basicConfig(filename='demo.log',level=logging.DEBUG)

def name_check(name):

    if len(name)<3:
        logging.debug("cheking the name length")
        return 'Invalid name!'
    
    if not re.match(r'^[A-Z]',name):
        logging.debug("check the first alphabet of name...it should be Capital")
        return 'Invalid name!'
    
    return 'Valid name!'
    
First_name=input("Enter the First name: ")
last_name=input("Enter the Last name: ")
result=name_check(First_name)
print(result)
result1=name_check(last_name)
print(result1)
