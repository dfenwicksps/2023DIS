#  This program will encrypt a message using the vigniere cipher
#  The user will enter a message and a key
#  The message will be encrypted using the key

def encrypt_character(char, key_char):
    if char.isupper():
        offset = 65
        key_offset = ord(key_char.upper()) - 65
    else:
        offset = 97
        key_offset = ord(key_char.lower()) - 97

    return chr((ord(char) - offset + key_offset) % 26 + offset)

def decrypt_character(char, key_char):
    if char.isupper():
        offset = 65
        key_offset = ord(key_char.upper()) - 65
    else:
        offset = 97
        key_offset = ord(key_char.lower()) - 97

    return chr((ord(char) - offset - key_offset + 26) % 26 + offset)

def encrypt_message(message, key):
    encrypted_message = ""
    for i in range(len(message)):
        char = message[i]
        key_char = key[i % len(key)]
        if char.isalpha():
            encrypted_message += encrypt_character(char, key_char)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt_message(message, key):
    decrypted_message = ""
    for i in range(len(message)):
        char = message[i]
        key_char = key[i % len(key)]
        if char.isalpha():
            decrypted_message += decrypt_character(char, key_char)
        else:
            decrypted_message += char
    return decrypted_message


def main():
    #message = input("Enter a message: ")  # Get message from user
    #key = input("Enter a key: ")  # Get key from user
    oldclue2 = "vwduwljudeehghyhubwklqjlfrxogilqgsohdvhuhwxuqdqbeoxhsulqwviruydxowd qgdodupghvljqedvhgrqzklfkedqnbrxghflghrqldpvhwwlqjxsvdihkrxvhfr"
    clue2 = "Klkbnqlcytfysryucocphgbdizzfcmjwkuchzyeswfogmmetwwossdchrzyldsbwnydednzwnefydthtddbojicemlucdygicczhoadrzcylwadsxpilpiecskomoltejtkmqqymehpmmjxyolwpeewjckznpccpsvsxauyodhalmriocwpelwbcniyfxmwjcemcyrazdqlsomdbfljwnbijxpddsyoehxpceswtoxwbleecsaxcnuetzywfn"
    key = "skull"
    encrypted_message = encrypt_message(clue2, key)
    print("Encrypted message:", encrypted_message)  # Print encrypted message
    decrypted_message = decrypt_message(encrypted_message, key)
    print("Decrypted message:", decrypted_message)  # Print decrypted message

if __name__ == "__main__":
    main()  # Run main function
