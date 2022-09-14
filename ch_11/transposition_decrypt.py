import math
import pyperclip


def main():
    cipher_text = "Csshmoe aomnntnmso .oetcn  o itm"

    key = 7

    message = decrypt_message(cipher_text, key)

    """Prints with a | (called "pipe character") after it in case
    there are spaces at the end of the decrypted message."""
    print(f"{message}|")

    pyperclip.copy(message)


def decrypt_message(key, cipher_text):
    """Decrypts the transposition cipher text message with the given key."""

    # The number of "columns" in the transposition grid.
    no_of_columns = math.ceil(len(cipher_text) / key)

    # The number of "rows" in the transposition grid.
    no_of_rows = key

    # The number of "shaded boxes" in the last "column" of the grid.
    no_of_shaded_boxes = (no_of_columns * no_of_rows) - len(cipher_text)

    # Each string in plaintext represents a column in the grid
    plain_text = [""] * no_of_columns

    col = 0
    row = 0

    for symbol in cipher_text:
        plain_text[col] += symbol
        col += 1

        """If there are no more columns OR we're at a shaded box, go back to
        the first column  and the next row."""
        if (col == no_of_columns) or (col == no_of_columns - 1 and row >= no_of_rows - no_of_shaded_boxes):
            col = 0
            row += 1

    return "".join(plain_text)


"""If the transpositon_decrypt.py is run (instead of imported as a module)
call the main() function."""
if __name__ == "__main__":
    main()
