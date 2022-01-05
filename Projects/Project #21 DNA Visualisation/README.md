# DNA Visualisation
___
_by Al Sweigart_ [al@inventwithpython.com](mailto:al@inventwithpython.com)

A simple animation of a DNA double-helix.

Inspired by matoken https://asciinema.org/a/155441

View the original code [here](https://nostarch.com/big-book-small-python-projects).

**Tags**: _short_, _artistic_, _scrolling_, _science_

___

## TODO List:

[x] Emoji DNA

There are Twitter bots, like [Every DNA](https://twitter.com/everydna), that create "Emoji DNA", choose two emojis and wrapping them into a double helix, like DNA.

It's really easy to be able to do that, swapping the DNA bases for randomly selected emojis. You can limit `random_selection` to 1 or 2, to allow for randomly ordered pairs made from 2 emojis or directly insert `left_selection` and `right_selection`.

Using [Tweepy](https://docs.tweepy.org/en/stable/), you can easily set up a bot to tweet out these strings.

```
           🦴🐕
          🦴---🐕
        🐕-----🦴
       🦴-------🐕
      🦴--------🐕
     🐕--------🦴
     🐕-------🦴
      🐕-----🦴
      🦴---🐕
       🐕🦴
      🦴---🐕
      🐕-----🦴
     🦴-------🐕
     🦴--------🐕
      🦴--------🐕
       🐕-------🦴
        🐕-----🦴
         🐕---🦴
           🦴🐕
         🐕---🦴
        🦴-----🐕
       🦴-------🐕
      🐕--------🦴
     🦴--------🐕
```