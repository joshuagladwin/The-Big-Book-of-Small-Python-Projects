# Birthday Paradox Simulation

___

_by Al Sweigart_ [al@inventwithpython.com](mailto:al@inventwithpython.com)

Explore the surprising probabilities of the "Birthday Paradox".
More info at [here](https://en.wikipedia.org/wiki/Birthday_problem).

View the original code [here](https://nostarch.com/big-book-small-python-projects).

**Tags**: _short_, _math_, _simulation_

___

## TODO List:
* [x] ~~Change `!=` to `is none` for comparisons with `None`.~~

Check for identity, not for equality with `None`. Objects may _equal_ `None` but that doesn't necessarily mean
that they _are_ `None`. See [this Stack Overflow](https://stackoverflow.com/questions/1504717/why-does-comparing-strings-using-either-or-is-sometimes-produce-a-differe)
question for more details.

* [x] ~~Change multiple `print()` statements at end to one `print()` statement with a multi-line string.~~
* [x] ~~Change date order from ISO to DMY.~~ 
* [x] ~~Can I add markers for ordinal numbers? (-_th_, -_st_, -_nd_, -_rd_)~~
* [x] ~~Display full month names, (`Jan --> January`)~~
* [x] ~~Add in 29th Feb.~~ 
  * [ ] How can you handle 29th Feb being less frequent than other dates?

Setting `start_of_year` to a leap year (e.g. 2020) and the `datetime.timedelta(random.randint(0, 365))`
to a leap year allows for 29th Feb to occur in the birthdays.

* [x] ~~Order dates when displaying to make it easier to see duplicates.~~
* [ ] Return multiple duplicate dates, if occurring, not just first.

Currently, when displaying the duplicate birthdays using `get_match()`, once the function finds _a match_, it returns 
that duplicate birthday and ignores any subsequent duplicates. The `print()` text has been amended to better reflect 
this, but you could also amend the `for` loops in `get_match()` to display multiple duplicate birthdays.

___

## Extension Project - Lottery Paradox Simulation
### Premise

Following on from this project and [Bagels](https://github.com/joshuagladwin/The-Big-Book-of-Small-Python-Projects/tree/master/Project%20%231%20Bagels), you could combine the two to create a Lottery 
Paradox Simulation.

The [_Lotto_](https://en.wikipedia.org/wiki/National_Lottery_(United_Kingdom)#Lotto) is a lottery game run by the 
[National Lottery](https://en.wikipedia.org/wiki/National_Lottery_(United_Kingdom)) in the UK.

In a standard 6-ball lottery draw, using the numbers 1-49[[^]](x "Since 2015, the Lotto has used the numbers 1-59, 
but for the purposes here, it doesn't matter."), there is a [1 in 13,983,816 chance of winning](https://en.wikipedia.org/wiki/Lottery_mathematics). 
There are usually tens of millions of players each draw.

Yet despite these low odds, there is often more than one jackpot winner, matching all 6 numbers. [In one case](https://www.lottery.co.uk/lotto/results-14-01-1995), 133 players had chosen the same winning numbers and had to split the jackpot accordingly.

### Task

Making a 6-digit non-repeating number, as per [Bagels.py](https://github.com/joshuagladwin/The-Big-Book-of-Small-Python-Projects/blob/master/Project%20%231%20Bagels/bagels.py), you could then run a simulation similar to the Birthday Paradox 
to determine how the probability of there being more than one player with the same numbers changes as you increase the 
number of players.

Beyond the purely random selected numbers, there are several other factors that could be incorporated into the
simulation to more accurately reflect the real-world distributions of chosen numbers, such as:

* The "birthday" numbers `1-31`
* Superstitious numbers, lucky `7` or unlucky numbers `13`
* Consecutive numbers or patterns of numbers, `1, 2, 3, 4, 5, 6` or `2, 4, 6, 8, 10, 12`

This project could be further developed still into a fully-fledged lottery simulator, simulating players, the draw and
prize money distribution accordingly.
