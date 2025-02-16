import re
import logging

logging.basicConfig(filename='validation.log', level=logging.DEBUG)

def name_check(name):
    """Check if the name starts with a capital letter and has at least 3 characters."""
    try:
        if not re.match(r'^[A-Z][a-zA-Z]{2,}$', name):
            logging.debug("Invalid name format: Must start with a capital letter and have at least 3 characters.")
            return False
        return True
    except Exception as e:
        logging.error(f"Error in name_check: {e}")
        return False

def check_mail(mail_to_check):
    """Validate email format."""
    try:
        pattern = r'^[a-zA-Z0-9.+-_%]+@[a-zA-Z0-9.-]+\.[a-zA-Z]'
        if not re.match(pattern, mail_to_check):
            logging.error(f"Invalid email address: {mail_to_check}")
            return False
        return True
    except Exception as e:
        logging.error(f"Error in check_mail: {e}")
        return False

def check_mobile(number):
    """Validate mobile number: Must start with '91' and be 13 characters long."""
    try:
        if not re.match(r'^91[0-9]{10}$', number):
            logging.error("Invalid mobile number: Must start with '91' and have 13 characters in total.")
            return False
        return True
    except Exception as e:
        logging.error(f"Error in check_mobile: {e}")
        return False

def check_password(password):
    """Validate password: Must have at least 8 characters, an uppercase letter, and a numeric digit."""
    try:
        if not re.match(r'^.{8,}$', password):
            logging.warning("Password length is less than 8 characters.")
            return 'Invalid password! Your password should contain more than 8 characters.'

        if not re.search(r'[A-Z]', password):
            logging.warning("Password does not have an uppercase letter.")
            return 'Invalid password! Your password should have one uppercase letter.'

        if not re.search(r'[0-9]', password):
            logging.warning("Password does not have a numeric number.")
            return 'Invalid password! Your password should have one numeric number.'

        if not re.search(r'[@#$%^&*]', password):
            logging.warning("Password does not have a special character.")
            return 'Invalid password! Your password should have at least one special character.'

        return 'Valid password'
    except Exception as e:
        logging.error(f"Error in check_password: {e}")
        return 'Error validating password.'

def main():
    try:
        first_name = input("Enter the First name: ")
        print('Valid name!' if name_check(first_name) else 'Invalid name!')

        last_name = input("Enter the Last name: ")
        print('Valid name!' if name_check(last_name) else 'Invalid name!')

        email = input("Enter an email address: ")
        print('Valid email!' if check_mail(email) else 'Invalid email!')

        number = input("Enter the mobile number: ")
        print('Valid number!' if check_mobile(number) else 'Invalid number!')

        password = input("Enter the password: ")
        print(check_password(password))

    except Exception as e:
        logging.critical(f"Critical error in main: {e}")

if __name__ == "__main__":
    main()
