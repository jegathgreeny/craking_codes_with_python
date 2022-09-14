import pyperclip

from detect import is_english
from transposition_decrypt import decrypt_message


def main():
    message = '''Ywnbe isee.ongy ybe   u   ool wuT fyetuetinhcaolh .hlaeoiuieh albyul?mraAt l'lu i vs aeldrBnhe rl l eaaa lewt n.ctlsomaoro kifhney etW n ogmsas htgww b cileo onaebcsir hu sreetvemalm   p.e eldetwtt d.f  hhh wi  tieaowidIohtrtsht  fr'e eahtt is w t hhlv aat yaoieirshcotuf,me aau ge p ttnrbh both   rttusheaboi htsorre'''


    hacked_message = hack(message)

    if hacked_message == None:
        print('Failed to hack encryption.')
    else:
        print('Copying hacked message to clipboard.\n')
        print(hacked_message)
        pyperclip.copy(hacked_message)

def hack(message):
    print('Hacking...')

    print('Press Ctrl-C to quit.')

    for key in range(1, len(message)):
        print(f'Trying key #{key}')
        decrypted_message = decrypt_message(key, message)

        if is_english(decrypted_message):
            print('\nPossible encryption hack:')
            print(f'key {key}: {decrypted_message[:100]}\n')
            print('Enter "done" for done, or just press Enter to continue hacking:')
            response = input('> ')
            if response.strip().lower().startswith('d'):
                return decrypted_message

        
    return None

if __name__ == '__main__':
    main()