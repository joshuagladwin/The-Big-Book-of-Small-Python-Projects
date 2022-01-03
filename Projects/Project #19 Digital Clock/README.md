# Digital Clock
___
_by Al Sweigart_ [al@inventwithpython.com](mailto:al@inventwithpython.com)

Displays a digital clock of the current time with a seven-segment
display.

View the original code [here](https://nostarch.com/big-book-small-python-projects).

**Tags**: _tiny_, _artistic_

___

## TODO List:

* [x] ~~Add indicator for a.m./p.m.~~

 Seeing as this is a 12-hour clock, it might be useful to add in indicators for A.M. and P.M.
 You can't display 'M' using a seven-segment display, so we can only use 'A' and 'P'.

These are drawn at the start of the `digitalclock.py` as `A` and `P`, as if they are drawn by `sevseg.get_sev_seg_str()`.
If `current_time.tm_hour` is greater than `12`, `P` is passed as the 12-hour period to display on the clock, else `A`.
The indicator is then parsed and displayed just as the numbers for hours, minutes and seconds.

E.g. for 4:59:39 PM:

```
 __            __   __       __   __    __
|  | |__|  *  |__  |__|  *   __| |__|  |__|
|__|    |  *   __|  __|  *   __|  __|  |
```