import pyperclip

# The string to be encrypted.
message = pyperclip.paste()

# Every possible symbol that can be encrypted.
LETTERS = ' !"#$%&\'()*+,_./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

# The encryption or decrytion key.
key = 14

# Stores the encrypted or decrypted form of the message.
translated = ""

# Tells the program to encrypt or decrypt.
mode = "encrypt"

# Runs the encrytion or decryption action on each symbol in the message.
for symbol in message:
    if symbol in LETTERS:
        # Gets the index positon of the symbol in LETTERS.
        num = LETTERS.find(symbol)

        if mode == "encrypt":
            num += key
        elif mode == "decrypt":
            num -= key

        '''Handles the wrap around if num is larger than the length of LETTERS
         or less than 0.'''
        if num >= len(LETTERS):
            num -= len(LETTERS)
        elif num < 0:
            num += len(LETTERS)

        # Adds the encrypted or decrypted symbol to the end of the string.
        translated += LETTERS[num]
    else:
        '''Adds the symbols that are not found in the
         LETTERS string in its corressponding place.
        Symbols like .,''"" etc and spaces are simply entered without
         encryption or decryption.'''
        translated += symbol

print(translated)

pyperclip.copy(translated)