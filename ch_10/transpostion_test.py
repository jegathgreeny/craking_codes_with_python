import sys, random
import transposition_encrypt, transposition_decrypt


def main():
    # set the random "seed" to a static value
    random.seed(40)

    # run 20 tests
    for i in range(20):

        # generate random messages to test
        message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * random.randint(3, 50)
        message = list(message)
        random.shuffle(message)
        message = "".join(message)

        print(f"Test #{i+1} {message[:50]}")

        # check all possible keys for each message
        for key in range(1, len(message)):
            encrypted = transposition_encrypt.encrypt_message(key, message)
            decrypted = transposition_decrypt.decrypt_message(key, encrypted)

            """if the decryption doesn't match the original message, display
            an errror message and quit"""
            if message != decrypted:
                print(f"Mismatch with key {key} and message {message}.")
                print(decrypted)
                sys.exit()

    print("Transposition cipher test passed.")


"""if transposition_test.py is run (instead of imported as a module) call
the main() function."""
if __name__ == "__main__":
    main()
