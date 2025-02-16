import pytest
from validation import name_check, check_mail, check_mobile, check_password

def test_name_check():
    assert name_check("John") == True
    assert name_check("jane") == False
    assert name_check("A") == False
    assert name_check("AB") == False
    assert name_check("Alice") == True

def test_check_mail():
    assert check_mail("test@example.com") == True
    assert check_mail("user.name@domain.com") == True
    assert check_mail("invalid-email") == False
    assert check_mail("no_at_symbol.com") == False

def test_check_mobile():
    assert check_mobile("911234567890") == True
    assert check_mobile("91987654321") == False
    assert check_mobile("001234567890") == False
    assert check_mobile("9123456789") == False

def test_check_password():
    assert check_password("Password1@") == "Valid password"
    assert check_password("short1@") == "Invalid password! Your password should contain more than 8 characters."
    assert check_password("password1@") == "Invalid password! Your password should have one uppercase letter."
    assert check_password("PASSWORD@") == "Invalid password! Your password should have one numeric number."
    assert check_password("Password1") == "Invalid password! Your password should have at least one special character."

if __name__ == "__main__":
    pytest.main()
