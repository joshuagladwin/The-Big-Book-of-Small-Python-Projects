# Fast Draw
___
_by Al Sweigart_ [al@inventwithpython.com](mailto:al@inventwithpython.com)

Test your reflexes to see if you're the fastest draw in the west.

View the original code [here](https://nostarch.com/big-book-little-python-projects)

**Tags**: _tiny_, _beginner_, _game_

```
It is high noon...
DRAW!

You took 0.0916 seconds to draw.
You are the fastest draw in the west! You win!
```

___

## TODO List:

* [x]  ~~Mess with the timings.~~

There's not too much that immediately comes to mind to add/change to this beyond the timings.
Increasing the `0.3` on `ln 30` makes the game easier, allowing for more time before the draw is
considered a "failure". Personally, I wouldn't decrease the time any more than 0.3 seconds, as I
found it difficult enough to win as it is...

Similarly, you could increase the range that the random integer (`ln 20`) is selected from, (i.e. 50 → 100 - 
this would change the max time before draw from 5 to 10 seconds.) Famously in any cowboy movie, while the
speed of the draw is _paramount_, the length of wait before drawing increases tension. In game terms,
a longer draw results in more time to flinch and press early, plus a greater risk that the player's
attention wanders before "DRAW!" is called.