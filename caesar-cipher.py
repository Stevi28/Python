# create a user-defined function
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet*2
    return doubleAlphabet
#print(getDoubleAlphabet('ABC'))

# encrypting a message
def getMessage():
    # this function just returns a string. That's why doesn't take arguments
    stringToEncrypt = input('Please enter a message to encrypt: ')
    return stringToEncrypt
#print(getMessage())
    
# getting a cipher key
# any integer from 1-25. 26 returns back to 1
def getCipherKey():
    shiftAmount = input('Please enter a key (whole number from 1-25): ')
    return shiftAmount
#print(getCipherKey())

# function for encrypting a message
def encryptMessage(message,cipherKey,alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

# decrypting a message
def decryptMessage(message,cipherKey,alphabet):
    decryptKey = (-1) * int(cipherKey)
    return (encryptMessage(message,decryptKey,alphabet))

# main function
def runCaesarCipherProgram():
    myAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
runCaesarCipherProgram()


