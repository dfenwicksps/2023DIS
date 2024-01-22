#  This program takes a string and analyses the frequency of characters in the string
#  The user will enter a string
#  The program will analyse the frequency of characters in the string
#  The program will display the frequency of characters in the string
#  The program will display the frequency of characters in the string as a bar chart

text = input("Enter a string: ")  # Get string from user
text = text.lower()  # Convert string to lowercase
text1 =  "vwduwljudeehghyhubwklqjlfrxogilqgsohdvhuhwxuqdqbeoxhsulqwviruydxowdqgdodupghvljqedvhgrqzkifkedqnbrxghflghrqldpvhwwlqjxsvdihkrxvhfr"


def frequency_analysis(text):
    """Analyse the frequency of characters in a string"""
    frequency = {}  # Create an empty dictionary to store the frequency of characters
    for char in text1:  # Loop through each character in the string
        if char in frequency:  # If the character is already in the dictionary
            frequency[char] += 1  # Increment the frequency of the character by 1
        else:  # If the character is not in the dictionary
            frequency[char] = 1  # Set the frequency of the character to 1
    return frequency  # Return the dictionary containing the frequency of characters

#print(frequency_analysis(text))  # Print the frequency of characters in the string
print(text1)
for key, value in frequency_analysis(text).items():  # Loop through each key-value pair in the dictionary
    print(key, value)  # Print the key-value pair
    #print(key, "*" * value)  # Print the key followed by a number of asterisks equal to the value