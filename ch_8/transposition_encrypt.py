import pyperclip

def main():
    message = "Common sense is not that common."

    key = 7

    cipher_text = encrypt_message(message, key)

    # Prints encrypted text with the pipe character at the end.
    # The pipe character shows the 
    print(f"{cipher_text}|")

    pyperclip.copy(cipher_text)

def encrypt_message(message, key):
    """Encrypts the message using transposition encrypt with the given key."""

    # Each string in cipher_text represents a column in the grid.
    cipher_text = [""] * key

    # Loop through each coloumn in cipher text.
    for col in range(key):
        pointer = col

        # Keep looping until pointer goes past the length of the message.
        while pointer < len(message):
            cipher_text[col] += message[pointer]

            
            pointer += key

    return "".join(cipher_text)

if __name__ == "__main__":
    main()