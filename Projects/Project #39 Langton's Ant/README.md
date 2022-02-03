# Langton's Ant
___
_by Al Sweigart_ [al@inventwithpython.com](mailto:al@inventwithpython.com)

A cellular automata animation. Press Ctrl-C to stop.

More info on Langton's Ant [here](https://en.wikipedia.org/wiki/Langton%27s_ant).

View the original code [here](https://nostarch.com/big-book-small-python-projects).

**Tags**: _large_, _artistic_, _bext_, _simulation_
___

I've added a simple counter `i` to display the number of iterations, in order to track the stages the simulation cycles through.

From the [Wiki article](https://en.wikipedia.org/wiki/Langton%27s_ant#Modes_of_behavior):
> These simple rules lead to complex behavior. Three distinct modes of behavior are apparent, when starting on a completely white grid.
> * Simplicity: During the first few hundred moves it creates very simple patterns which are often symmetric.
> * Chaos: After a few hundred moves, a large, irregular pattern of black and white squares appears. The ant traces a pseudo-random path until around 10,000 steps.
> * Emergent order: Finally the ant starts building a recurrent "highway" pattern of 104 steps that repeats indefinitely.


## TODO List:

* [ ] Let the player load and save the state of the board’s tiles from and to a text file.
* [ ] Create additional tile states with new rules of movement and see what behavior emerges.
* [ ] Implement some of the ideas suggested in the Wikipedia article for Langton’s Ant.
