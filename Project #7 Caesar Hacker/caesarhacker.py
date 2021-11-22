"""Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com
 This program hacks messages encrypted with the Caesar cipher by doing
 a brute force attack against every possible key.
 More info at:
 https://en.wikipedia.org/wiki/Caesar_cipher#Breaking_the_cipher
 View this code at https://nostarch.com/big-book-small-python-projects
 Tags: tiny, beginner, cryptography, math"""

print("Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com")

# Let the user specify the message to hack:
print('Enter the encrypted Caesar cipher message to hack.')
message = input('> ')

# Every possible symbole tha can be encrypted/decrypted:
# (This must match the symbols used when encrypting the message.)
symbols = ''
for i in range(0, 256):
    if chr(i).isprintable():
        symbols += chr(i)

symbols = symbols[::-1]

for key in range(len(symbols)):  # Loop through every possible key.
    translated = ''

    # Decrypt each symbol in the message:
    for symbol in message:
        if symbol in symbols:
            num = symbols.find(symbol)  # Get the number of the symbol.
            num = num - key  # Decrypt the number.

            # Handle the wrap-around if the number is less than 0:
            if num < 0:
                num = num + len(symbols)

            # Add decrypted number's symbol to translated:
            translated = translated + symbols[num]
        else:
            # Just add the symbol without decrypting:
            translated = translated + symbol

    # Display the key being tested, along with its decrypted text:
    print(f'Key #{key}: {translated}')
