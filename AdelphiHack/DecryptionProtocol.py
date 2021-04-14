# Author: Omer Basar
# Filename: DecryptionProtocol.py
# Version: 4/14/21
# Additional Notes: Learned how to convert hexadecimal to base ordinal value from following link
# https://stackoverflow.com/questions/9210525/how-do-i-convert-hex-to-decimal-in-python

# ----------------------------------------------------------------
'''
shiftMethod: Takes a ciphertext and performs a shift to decrypt the message
@Parameter: cipherText - text to be decrypted
@Parameter: cipherLength - length of cipherText
@Return: shiftedText - text that has been shifted
@Precondition: A ciphertext is provided
@Postcondition: Returns the message in a shifted manner
'''
def shiftMethod(cipherText,cipherLength):

    # Create a list that stores the alphabet
    alphabetList = []
    for i in range(0, 26):
        # Use ASCII codes to call in the appropriate characters
        alphabetList += chr(65 + i)

    # Initialize an empty string that will be used to store the shifted text
    shiftedText = ""

    # Iterate through each index of the ciphertext
    for j in range(0, cipherLength):
        # Determine which index the character from the ciphertext is in the alphabet list
        position = alphabetList.index(cipherText[j])
        # Perform the shift using the formula -4 modulo 26
        position = (position - 4) % 26
        # Add the shifted letter to the string that stores the shifted text
        shiftedText += alphabetList[position]

    # Return updated text
    return shiftedText

# ----------------------------------------------------------------
'''
characterDecoder: Takes a ciphertext and decrypts it using various methods
@Parameter: givenCipher - cipher to be decrypted
@Return: resultString - the decrypted message
@Precondition: A ciphertext is provided
@Postcondition: Displays the decrypted text in plaintext without any punctuation
'''
def characterDecoder(givenCipher):

    # Initialize variable to store ciphertext
    cipherText = str(givenCipher)

    # Remove spacing considering we know each hex value is comprised of 4 characters
    cipherText = cipherText.replace(" ", "")

    # Create a list to store each hex value in its own index
    cipherList = []

    # Add each value to its own position in the list
    for i in range(0, len(cipherText)):
        # For every four characters, which is one hex value
        if (i % 4) == 0:
            cipherList.append(cipherText[i: i + 4])

    # Store length of cipherList
    cipherLength = len(cipherList)

    # Create two lists to sort the hex values into the odd and even index positions
    oddIndexes, evenIndexes = [], []

    # The first 5 indexes in the cipherList contained the odd indexes
    for i in range(0, int(cipherLength/2)):
        oddIndexes.append(cipherList[i])
    # The last 5 indexes in the cipherList contained the even indexes
    for k in range(int(cipherLength/2), cipherLength):
        evenIndexes.append(cipherList[k])

    # Initialize list to hold sorted hex values
    plainList = []

    # Sort the hex values appropriately
    for i in range(0, len(oddIndexes)):
        plainList.append(oddIndexes[i])
        plainList.append(evenIndexes[i])

    # Initialize empty string to later hold plaintext message
    plainText = ""
    resultString = ""

    # Convert each hexadecimal value back into a character
    for i in range (0, cipherLength):
        plainText += chr(int(plainList[i], 0))

    # Perform shift to decrypt message
    plainText = shiftMethod(plainText, cipherLength)

    # Display plaintext message with spacing in between each character
    for i in range(0, cipherLength):
        resultString += plainText[i] + " "

    # Return decrypted message string
    return resultString
    
# ----------------------------------------------------------------