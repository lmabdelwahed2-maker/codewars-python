import string

def is_pangram(st):
    alphabet = set(string.ascii_lowercase)
    pangram = set()
    for s in st:
        s = s.lower()
        if s in alphabet:
            pangram.add(s)
    if alphabet.issubset(pangram):
        return True
    else:
        return False
