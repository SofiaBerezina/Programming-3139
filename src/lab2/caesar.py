def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    s = []
    for i in plaintext.split():
        r = ''
        for k in i:
            if k.isalpha() and k.islower():
                r += chr((ord(k) - 97 + shift) % 26 + 97)
            elif k.isalpha() and k.isupper():
                r += chr((ord(k) - 65 + shift) % 26 + 65)
            else:
                r += k
        s.append(r)
    ciphertext = ' '.join(s)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    s = []
    for i in ciphertext.split():
        r = ''
        for k in i:
            if k.isalpha() and k.islower():
                r += chr((ord(k) - 97 - shift) % 26 + 97)
            elif k.isalpha() and k.isupper():
                r += chr((ord(k) - 65 - shift) % 26 + 65)
            else:
                r += k
        s.append(r)
    plaintext = ' '.join(s)
    return plaintext
