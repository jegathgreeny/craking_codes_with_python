import os, time, sys
import transposition_encrypt, transposition_decrypt


def main():
    input_file = 'frankenstein_encrypted.txt'

    '''BE CAREFUL! If a file with the output_file name already exists,
    this program will overwrite that file.'''
    output_file = 'frankenstein_decrypted.txt'
    
    key = 11
    # set to 'encrypt' or 'decrypt'
    mode = "decrypt"


    # If the input file doesn't exist, then the program terminates early.
    if not os.path.exists(input_file):
        print(f'The file {input_file} does not exist. Quitting...')
    # If the output file already exists, give the user a chance to quit.
    if os.path.exists(output_file):
        print(f'This will overwrite the file {output_file}. (C)ontinue or (Q)uit?')
        response = input('> ')
        if not response.lower().starswith('c'):
            sys.exit()

    # Read the message from the input file.
    with open(input_file) as in_file:
        content = in_file.read()

    print(f'{mode.title()}ing...')

    # Measure how long the encryption/decryption takes.
    start_time = time.time()

    if mode == 'encrypt':
        translated = transposition_encrypt.encrypt_message(key, content)
    elif mode == 'decrypt':
        translated = transposition_decrypt.decrypt_message(key, content)

    total_time = round(time.time() - start_time, 2)
    print(f'{mode.title()}ion time: {total_time} seconds')
    
    # Write out the translated message to the output file.
    with open(output_file, 'w') as out_file:
        out_file.write(translated)

    print(f'Done {mode}ing ({len(content)} characters).')

    print(f'{mode}ed file is saved as {output_file}.')

if __name__ == '__main__':
    main()