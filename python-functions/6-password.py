def validate_password(password):
    if len(password) < 8:
        return False
    contain_uppercas = any(char.isupper() for char in password)
    contain_lowercase = any(char.islower() for char in password)
    contain_digit = any(char.isdigit() for char in password)
    if not (contain_uppercas and contain_lowercase and contain_digit):
        return False
    if ' ' in password:
        return False
    return True
