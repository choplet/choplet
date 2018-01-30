def is_palindrome(s):
    s=str(s)
    if list(s) ==  list(s [::-1]):
        return True
    else:
        return False

