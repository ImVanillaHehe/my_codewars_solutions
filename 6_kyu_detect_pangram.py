import string

def is_pangram(s):
    if len(set("qwertyuiopasdfghjklzxcvbnm") - set(s.lower())) == 0:
        return True
    return False
