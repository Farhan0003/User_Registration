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

def main():
    try:
        first_name = input("Enter the First name: ")
        print('Valid name!' if name_check(first_name) else 'Invalid name!')

    except Exception as e:
        logging.critical(f"Critical error in main: {e}")

if __name__ == "__main__":
    main()
