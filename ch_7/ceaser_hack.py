import pyperclip

# The string to be decrypted.
message = pyperclip.paste().upper()

# Every possible symbol that can be encrypted.
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Loop through every possible key.
for key in range(len(LETTERS)):

    # Stores the decrypted form of the message.
    # This needs to be cleared during each cycle.
    # So the new decrypted message may take its place.
    translated = ""

    for symbol in message:
        if symbol in LETTERS:
            # Gets the index positon of the symbol in LETTERS.
            num = LETTERS.find(symbol)
            num -= key

            """Handles the wrap around if num is larger than the length of LETTERS
             or less than 0."""
            if num >= len(LETTERS):
                num -= len(LETTERS)
            elif num < 0:
                num += len(LETTERS)

            # Adds the encrypted or decrypted symbol to the end of the string.
            translated += LETTERS[num]
        else:
            """Adds the symbols that are not found in the
             LETTERS string in its corressponding place.
            Symbols like .,''"" etc and spaces are simply entered without
             encryption or decryption."""
            translated += symbol

    print(f"#{key} {translated}")
