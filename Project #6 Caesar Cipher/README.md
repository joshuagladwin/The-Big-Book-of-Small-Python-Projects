# Caesar Cipher
____
_by Al Sweigart_ [al@inventwithpython.com](mailto:al@inventwithpython.com)

The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.

More info [here](https://en.wikipedia.org/wiki/Caesar_cipher).

View the original code [here](https://nostarch.com/big-book-small-python-projects).

**Tags**: _short_, _beginnner_, _cryptography_, _math_
____

## TODO List:

* [x] ~~Add numbers and punctuation marks to encrypt those symbols as well~~
  * [x]  ~~How else can this be extended? Using `ord()/chr()` and Unicode?~~

The easiest way to add in punctuation and numbers is to simply add them to the list of
valid symbols to check against:

`SYMBOLS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ'`

However, an easier way to do this is to generate the list of valid symbols, like this:

```
symbols = ''
for i in range(0, 256):
    if chr(i).isprintable():
        symbols += chr(i)
```
                
This creates a string of the printable characters from the
Basic Latin and Latin-1 Supplement Unicode blocks. This also makes it easier
add more characters when necessary. For example, using the range 1024-1120 adds
Cyrillic to the string of encryptable symbols: 

```
for i in range(1024, 1120):
    if chr(i).isprintable():
        symbols += chr(i)
```

A Caesar cipher is *really* simple and not very secure ([see Project #7](../Project%20%237%20Caesar%20Hacker)), and while there are many things
that *could* be done to improve upon it, that's a whole cryptography rabbit hole I'm not going to go down right now. 