import re
import logging

logging.basicConfig(filename='email.log',level=logging.DEBUG)

def check_mail(mail_to_check):
  pattern='^[a-zA-Z0-9.+-_%]+@[a-zA-Z0-9.-]+\.[a-zA-Z]'

  if re.match(pattern,mail_to_check):
    return True
  else:
    return False  

email=input("Enter an email addredd: ")
if check_mail(email):
  logging.info(f"{email} is a Valid Email Address.")
else:
  logging.error(f"{email} is an Invalid Email Address.")
