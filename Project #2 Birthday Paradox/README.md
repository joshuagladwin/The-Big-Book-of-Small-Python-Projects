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
that they _are_ `None`.

* [x] ~~Change multiple `print()` statements at end to one `print()` statement with a multi-line string.~~
* [x] ~~Change date order from ISO to DMY;~~ 
* [ ] Can I add markers for ordinal numbers? (-_th_, -_st_, -_nd_, -_rd_)
* [x] ~~Display full month names, (`Jan --> January`)~~
* [x] ~~Add in 29th Feb.~~ 
  * [ ] How can I handle 29th Feb being less frequent than other dates?

Setting `start_of_year` to a leap year (e.g. 2020) and the `datetime.timedelta(random.randint(0, 365))`
to a leap year allows for 29th Feb to occur in the birthdays.

* [ ] Order dates when displaying to make it easier to see duplicates.

