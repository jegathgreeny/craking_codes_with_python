'''Detect English module

To use this code:
    import detect
    detect.is_english(some_string) # returns True or False
(There must be a 'dictionary.txt' file in this directory with all english
words in it, one word per line. You can download this from
http://invpy.com/dictionary.txt).'''

UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS_AND_SPACE = f"{UPPER_LETTERS} {UPPER_LETTERS.lower()} \t\n"


def load_dictionary():
    with open("dictionary.txt") as dictionary:
        english_words = {}
        for word in dictionary.read().split("\n"):
            english_words[word] = None
        return english_words


ENGLISH_WORDS = load_dictionary()


def get_english_count(message):
    message = message.upper()
    message = remove_non_letters(message)
    possible_words = message.split()
    if possible_words == []:
        # no words at all, so return 0.
        return 0

    matches = 0
    for word in possible_words:
        if word in ENGLISH_WORDS:
            matches += 1
    return matches / len(possible_words)


def remove_non_letters(message):
    letters_only = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            letters_only.append(symbol)
    return "".join(letters_only)


def is_english(message, word_precentage=20, letter_percentage=85):
    """By default, 20% of the words must exist in the dictionary file, and
    85% of all the characters in the message must be letters or spaces
    (not punctuation or numbers)."""
    words_match = get_english_count(message) * 100 >= word_precentage
    num_letters = len(remove_non_letters(message))
    message_letters_percentage = num_letters / len(message) * 100
    letters_match = message_letters_percentage >= letter_percentage
    return words_match and letters_match
