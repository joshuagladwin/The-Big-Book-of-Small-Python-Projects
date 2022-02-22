"""Simple Substitution Cipher, by Al Sweigart al@inventwithpython.com
A simple substitution cipher has a one-to-one translation for each
symbol in the plaintext and each symbol in the ciphertext.
More info at: https://en.wikipedia.org/wiki/Substitution_cipher
View the original code at https://nostarch.com/big-book-small-python-projects
Tags: short, cryptography, math"""

import random

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's not big deal.

# Every possible symbol that can be encrypted/decrypted.
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    print('''Simple Substitution Cipher, by Al Sweigart
A simple substitution cipher has a one-to-one translation for each
symbol in the plaintext and each symbol in the ciphertext.''')

    # Let the user specify if they are encrypting or decrypting:
    while True:  # Keep asking until thebuser enters e or d.
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ').lower()
        if response.startswith('e'):
            my_mode = 'encrypt'
            break
        elif response.startswith('d'):
            my_mode = 'decrypt'
            break
        print('Please enter a letter e or d.')

    # Let the user specify the key to use:
    while True:  # Keep asking until the user enters a valid key.
        print('Please specify the key to us.')
        if my_mode == 'encrypt':
            print('Or enter RANDOM to have one generated for you.')
        response = input('> ').upper()
        if response == 'RANDOM':
            my_key = generate_random_key()
            print(f'The key is {my_key}. KEEP THIS SECRET!')
            break
        else:
            if check_key(response):
                my_key = response
                break

    # Let the user specify the message to encrypt/decrypt:
    print(f'Enter the message to {my_mode}.')
    my_message = input('> ')

    # Perform the encryption/decryption:
    if my_mode == 'encrypt':
        translated = encrypt_message(my_message, my_key)
    elif my_mode == 'decrypt':
        translated = decrypt_message(my_message, my_key)

    # Display the results:
    print(f'The {my_mode}ed message is:')
    print(translated)

    try:
        pyperclip.copy(translated)
        print(f'Full {my_mode}ed text copied to clipboard.')
    except:
        pass  # Do nothing if pyperclip wasn't installed.


def check_key(key):
    """Return True if key is valid. Otherwise return False."""
    key_list = list(key)
    letters_list = list(LETTERS)
    key_list.sort()
    letters_list.sort()
    if key_list != letters_list:
        print('There is an error in the key or symbol set.')
        return False
    return True


def encrypt_message(message, key):
    """Encrypt the message using the key."""
    return translate_message(message, key, 'encrypt')


def decrypt_message(message, key):
    """Decrypt the message using the key."""
    return translate_message(message, key, 'decrypt')


def translate_message(message, key, mode):
    "Encrypt or decrypt the message using the key."
    translated = ''
    chars_a = LETTERS
    chars_b = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        chars_a, chars_b = chars_b, chars_a

    # Loop through each symbol in the message:
    for symbol in message:
        if symbol.upper() in chars_a:
            # Encrypt/decrypt the symbol:
            sym_index = chars_a.find(symbol.upper())
            if symbol.isupper():
                translated += chars_b[sym_index].upper()
            else:
                translated += chars_b[sym_index].lower()
        else:
            # The symbol is not in LETTERS, just add it unchanged.
            translated += symbol

    return translated


def generate_random_key():
    """Generate and return a random encryption key."""
    key = list(LETTERS)  # Get a list from the LETTERS string.
    random.shuffle(key)  # Randomly shuffle the list.
    return ''.join(key)  # Get a string from the list.


# If this program was run (instead of imported), run the program:
if __name__ == '__main__':
    main()
