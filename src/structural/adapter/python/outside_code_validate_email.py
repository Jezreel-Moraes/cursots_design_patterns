def is_email(email: str) -> bool:
    if '@' not in email:
        return False
    if '.' not in email:
        return False
    return True
