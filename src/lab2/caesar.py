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
    result = []
    for i in plaintext.split():
        word = ''
        for k in i:
            if k.isalpha() and k.islower():
                word += chr((ord(k) - 97 + shift) % 26 + 97)
            elif k.isalpha() and k.isupper():
                word += chr((ord(k) - 65 + shift) % 26 + 65)
            else:
                word += k
        result.append(word)
    ciphertext = ' '.join(result)
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
    result = []
    for i in ciphertext.split():
        word = ''
        for k in i:
            if k.isalpha() and k.islower():
                word += chr((ord(k) - 97 - shift) % 26 + 97)
            elif k.isalpha() and k.isupper():
                word += chr((ord(k) - 65 - shift) % 26 + 65)
            else:
                word += k
        result.append(word)
    plaintext = ' '.join(result)
    return plaintext
