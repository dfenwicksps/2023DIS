#  This program will encrypt a message using caesar cipher
#  The user will enter a message and a key
#  The message will be encrypted using the key
#  The encrypted message will be displayed to the user
def encrypt_character(char, key):
    if char.isupper():  # Check if character is uppercase
        enchar = chr((ord(char) + key - 65) % 26 + 65)  # Encrypt uppercase character
    else:
        enchar = chr((ord(char) + key - 97) % 26 + 97)  # Encrypt lowercase character
    return enchar
x = "y"
while x == "y":
    #message = input("Enter a message: ")  # Get message from user
    #message = "vwduwljudeehghyhubwklqjlfrxogilqgsohdvhuhwxuqdqbeoxhsulqwviruydxowdqgdodupghvljqedvhgrqzkifkedqnbrxghflghrqldpvhwwlqjxsvdihkrxvhfr"
    #clue1 = "gluhtlishjrvbadvyyplkaohavbyjpwolypzavvdlhrvuuleatlzzhnlzdpajoavcpnlulyljpwolyrlfdvykpzaolopkkluzftivsvmklhaoputfmhcvypalovsilpuluk"
    #clue2 = "vwduwljudeehghyhubwklqjlfrxogilqgsohdvhuhwxuqdqbeoxhsulqwviruydxowd qgdodupghvljqedvhgrqzklfkedqnbrxghflghrqldpvhwwlqjxsvdihkrxvhfr"
    message = "vwduwljudeehghyhubwklqjlfrxogilqgsohdvhuhwxuqdqbeoxhsulqwviruydxowdqgdodupghvljqedvhgrqzkifkedqnbrxghflghrqldpvhwwlqjxsvdihkrxvhfr"

    key = int(input("Enter a key: "))  # Get key from user
    encrypted_message = ""  # Encrypted message to be returned to user
    for char in message:  # Loop through each character in the message
        if char.isalpha():  # Check if character is a letter
                encrypted_message += encrypt_character(char, key)
        else:
            encrypted_message += char
    print("Encrypted message:", encrypted_message)  # Print encrypted message
    x = input("Do you want to continue? (y/n): ")  # Ask user if they want to continue



''' Further explanation of the encryption process:
The ord function returns the ASCII value of the character char. For uppercase English letters,
this value will be in the range of 65 (for 'A') to 90 (for 'Z').

ord(char) + key - 65: This expression first adds the value of key to the ASCII value of char, shifting it by the desired amount. 
Then, 65 is subtracted to normalize the value to the range of 0 to 25 (since the English alphabet has 26 letters).

This allows the cipher to wrap around, so that shifting 'Z' with a key of 1 results in 'A', for example.

(ord(char) + key - 65) % 26 + 65: Finally, 65 is added back to the result to transform the value back into the 
ASCII range for uppercase English letters.

chr(...): The chr function takes an ASCII value and returns the corresponding character. This results in the encrypted character.
'''