import re
def validate_password(password):
    if len(password) < 8 or len(password) > 20:
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"\d", password):
        return False

    if not re.search(r"[$#@*]", password):
        return False
    return True

password = input("Enter the password: ")
if validate_password(password):
    print("Valid password")
else:
    print("Invalid password")