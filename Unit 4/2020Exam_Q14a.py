from Cryptodome.Cipher import Blowfish
from struct import pack


def BlowfishInitiate(key):
    """Initializes the Blowfish cipher"""
    return Blowfish.new(key.encode(), Blowfish.MODE_ECB)


def BlowfishCrypt(value, keyset, process_type):
    """Encrypts or decrypts using Blowfish"""
    value_bytes = value.encode()
    if process_type == 1:  # Encryption
        # Blowfish requires input to be a multiple of 8 bytes
        plen = 8 - len(value_bytes) % 8
        padding = [plen] * plen
        padding = pack('b' * plen, *padding)
        encrypted = keyset.encrypt(value_bytes + padding)
        return encrypted
    elif process_type == 2:  # Decryption
        decrypted_bytes = keyset.decrypt(value_bytes)
        # Remove padding before returning decrypted text
        padding_len = decrypted_bytes[-1]
        return decrypted_bytes[:-padding_len].decode()
    else:
        raise ValueError("Invalid process type")


def main():
    key = input("Enter the key: ")  # 8 characters long
    if any(char.isalpha() for char in key) and len(key) == 8:  # Check if key is valid
        MyKeySet = BlowfishInitiate(key)  # Initialize Blowfish cipher with key from user

        user_text = input("Enter user text: ")  # User text to encrypt
        print("User Text:", user_text)
        cipher_text = b""  # Encrypted text to be returned to user as bytes object (hexadecimal)
        print("Cipher Text:", cipher_text)

        if len(user_text) >= 8:  # Check if user text is long enough
            for i in range(0, len(user_text), 8):  # Encrypt 8 characters at a time
                BlockSet = user_text[i:i + 8]  # Get 8 characters from user text
                cipher_text += BlowfishCrypt(BlockSet, MyKeySet, 1)  # Encrypt 8 characters and add to cipher text
                print("Block Set:", BlockSet)  # Print block set
                print(len(BlockSet))    # Print length of block set
                print("Cipher Text:", cipher_text)  # Print cipher text

            print("Cipher Text:", cipher_text.hex())  # Print cipher text as hexadecimal string (bytes object)
        else:
            print("User text is too short.")  # User text is too short
    else:
        print("Invalid key. Ensure it contains letter characters and has a length of 8.")  # Invalid key


if __name__ == "__main__":
    main()  # Run main function
