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
    if not keyword.isalpha():
        return 'Error'
    shifts = 'abcdefghijklmnopqrstuvwxyz'
    if len(keyword) < len(plaintext):
        for i in range(len(plaintext)):
            keyword += keyword[i]
    digit_keyword = []
    for i in range(len(keyword)):
        digit_keyword.append(shifts.index(keyword[i].lower()))
    result = []
    for i in range(len(plaintext)):
        word = ''
        for k in plaintext[i]:
            if k.isalpha() and k.islower():
                word += chr((ord(k) - 97 + digit_keyword[i]) % 26 + 97)
            elif k.isalpha() and k.isupper():
                word += chr((ord(k) - 65 + digit_keyword[i]) % 26 + 65)
            else:
                word += k
        result.append(word)
    ciphertext = ''.join(result)
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
    if not keyword.isalpha():
        return 'Error'
    shifts = 'abcdefghijklmnopqrstuvwxyz'
    if len(keyword) < len(ciphertext):
        for i in range(len(ciphertext)):
            keyword += keyword[i]
    digit_keyword = []
    for i in range(len(keyword)):
        digit_keyword.append(shifts.index(keyword[i].lower()))
    result = []
    for i in range(len(ciphertext)):
        word = ''
        for k in ciphertext[i]:
            if k.isalpha() and k.islower():
                word += chr((ord(k) - 97 - digit_keyword[i]) % 26 + 97)
            elif k.isalpha() and k.isupper():
                word += chr((ord(k) - 65 - digit_keyword[i]) % 26 + 65)
            else:
                word += k
        result.append(word)
    plaintext = ''.join(result)
    return plaintext
