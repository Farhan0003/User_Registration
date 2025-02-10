import re
import logging

logging.basicConfig(filename='mobile.log',level=logging.DEBUG)

def check_mobile(number):

    if len(number)!=13:
        logging.error("checking the length of the mobile number")
        return 'Invalid Number'
    
    if not re.match (r'^[91]',number):
        logging.error("checking the country code")
        return 'Invalid Number'
    
    return 'Valid Number'



number=input("Enter the number: ")
result = check_mobile(number)
print(result)
