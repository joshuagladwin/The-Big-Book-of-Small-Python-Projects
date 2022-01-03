# Dice Roller
___
_by Al Sweigart_ [al@inventwithpython.com](mailto:al@inventwithpython.com)

Simulates dice rolls using the Dungeons & Dragons dice roll notation.

View the original code [here](https://nostarch.com/big-book-small-python-projects).

**Tags**: _short_, _simulation_

___
Example Dice Strings:

| Dice String | No. of Dice | d | Number of Sides | Modifier | Mod. Amount |
|--------|--------|--------|--------|--------|--------|
| 2d4+2 | 2 | d | 4 | + | 2 |
| 3d8-4 | 3 | d | 8 | - | 4 |
| d20+3 | (1) | d | 20 | + | 3 |
| 4d8*2 | 4 | d | 8 | * | 2 |

## TODO List:

* [x] ~~Add multiplication modifier.~~

Now recognises `*` as a multiplication modifier and calculates roll accordingly. 

* [x] ~~Allow for optional 1 when only rolling on die (i.e. d20 == 1d20).~~

* [ ] Add ability to auto remove the lowest/highest die roll (i.e. to simulate rolls with advantage/disadvantage.)

* [ ] Allow for mixing different types of dice in the sum (i.e. 2d6, 1d4, +2)
