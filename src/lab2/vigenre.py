def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    shifts = 'abcdefghijklmnopqrstuvwxyz'
    if len(keyword) < len(plaintext):
        for i in range(len(plaintext)):
            keyword += keyword[i]
    digit_keyword = []
    for i in range(len(keyword)):
        digit_keyword.append(shifts.index(keyword[i].lower()))
    s = []
    for i in range(len(plaintext)):
        r = ''
        for k in plaintext[i]:
            if k.isalpha() and k.islower():
                r += chr((ord(k) - 97 + digit_keyword[i]) % 26 + 97)
            elif k.isalpha() and k.isupper():
                r += chr((ord(k) - 65 + digit_keyword[i]) % 26 + 65)
            else:
                r += k
        s.append(r)
    ciphertext = ''.join(s)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    shifts = 'abcdefghijklmnopqrstuvwxyz'
    if len(keyword) < len(ciphertext):
        for i in range(len(ciphertext)):
            keyword += keyword[i]
    digit_keyword = []
    for i in range(len(keyword)):
        digit_keyword.append(shifts.index(keyword[i].lower()))
    s = []
    for i in range(len(ciphertext)):
        r = ''
        for k in ciphertext[i]:
            if k.isalpha() and k.islower():
                r += chr((ord(k) - 97 - digit_keyword[i]) % 26 + 97)
            elif k.isalpha() and k.isupper():
                r += chr((ord(k) - 65 - digit_keyword[i]) % 26 + 65)
            else:
                r += k
        s.append(r)
    plaintext = ''.join(s)
    return plaintext
