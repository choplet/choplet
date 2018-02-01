def is_palindrome(s):
    s=str(s)
    if s ==  s [::-1]:
        return True
    else:
        return False

print (is_palindrome([101]))
d = str(102)
print (d[::-1])
