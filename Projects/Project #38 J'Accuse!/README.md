# J'Accuse!
___
_by Al Sweigart_ [al@inventwithpython.com](mailto:al@inventwithpython.com)

A mystery game of intrigue and a missing cat.

View the original code [here](https://nostarch.com/big-book-small-python-projects).

**Tags**: _extra-large_, _game_, _humor_, _game_

Play the original Flash game [here](https://homestarrunner.com/wheresanegg).

More info [here](http://www.hrwiki.org/wiki/Where's_an_Egg%3F).

___

## TODO List:

* [ ] Check clues

Currently, when at a place, there's no way to check the clues you've gathered so far when interviewing a suspect.
This would be useful to allow you to more easily check their answers against what clues you've already gathered.

The easiest way to achieve this would be to add another option in the dialogue options `(C)heck Clues` to allow the
player to quickly look at the clues, without having to go back to the taxi. 

* [ ] Remove option to ask suspect about themselves or their item.

Currently, when asking a suspect about their item or their item, the response is always "`They give you this clue: 
"No comment."`". These dialogue options don't serve any purpose and don't further the game, and the code could be easily
modified to drop them from the list. As the investigation goes on, the list of dialogue options gets very long, so
anything that can be (further) done to make this easier for the player to use would be beneficial.