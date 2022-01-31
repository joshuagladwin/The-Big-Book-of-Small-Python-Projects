# Etching Drawer
___
_by Al Sweigart_ [al@inventwithpython.com](mailto:al@inventwithpython.com)

An art program that draws a continuous line around the screen using the WASD keys. Inspired by Etch A Sketch toys.

For example, you can draw Hilbert Curve fractal with:
```
> SDWDDSASDSAAWASSDSASSDWDSDWWAWDDDSASSDWDSDWWAWDWWASAAWDWAWDDSDW

│┌─┐┌─┐#                                                                       
└┘┌┘└┐└┘                                                                       
┌┐└┐┌┘┌┐                                                                       
│└─┘└─┘│                                                                       
└┐┌──┐┌┘                                                                       
┌┘└┐┌┘└┐                                                                       
│┌┐││┌┐│                                                                       
└┘└┘└┘└┘    
```

Or an even larger Hilbert Curve fractal with:
```
> DDSAASSDDWDDSDDWWAAWDDDDSDDWDDDDSAASDDSAAAAWAASSSDDWDDDDSAASDDSAAAAWA
  ASAAAAWDDWWAASAAWAASSDDSAASSDDWDDDDSAASDDSAAAAWAASSDDSAASSDDWDDSDDWWA
  AWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWAAWDDDDSDDWDDSDDWDDDDSAASDDS
  AAAAWAASSDDSAASSDDWDDSDDWWAAWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWA
  AWDDDDSDDWWAAWDDWWAASAAWAASSDDSAAAAWAASAAAAWDDWAAWDDDDSDDWWWAASAAAAWD
  DWAAWDDDDSDDWDDDDSAASSDDWDDSDDWWAAWDD

──┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌─#                                                
┌─┘ └─┐ └─┘ ┌─┘ └─┐ └─┘ ┌─┘ └─┐                                                
│ ┌─┐ │ ┌─┐ └─┐ ┌─┘ ┌─┐ │ ┌─┐ │                                                
└─┘ └─┘ │ └───┘ └───┘ │ └─┘ └─┘                                                
┌─┐ ┌─┐ │ ┌───┐ ┌───┐ │ ┌─┐ ┌─┐                                                
│ └─┘ │ └─┘ ┌─┘ └─┐ └─┘ │ └─┘ │                                                
└─┐ ┌─┘ ┌─┐ └─┐ ┌─┘ ┌─┐ └─┐ ┌─┘                                                
┌─┘ └───┘ └───┘ └───┘ └───┘ └─┐                                                
│ ┌───┐ ┌───┐ ┌─┐ ┌───┐ ┌───┐ │                                                
└─┘ ┌─┘ └─┐ └─┘ └─┘ ┌─┘ └─┐ └─┘                                                
┌─┐ └─┐ ┌─┘ ┌─┐ ┌─┐ └─┐ ┌─┘ ┌─┐                                                
│ └───┘ └───┘ │ │ └───┘ └───┘ │                                                
└─┐ ┌─────┐ ┌─┘ └─┐ ┌─────┐ ┌─┘                                                
┌─┘ └─┐ ┌─┘ └─┐ ┌─┘ └─┐ ┌─┘ └─┐                                                
│ ┌─┐ │ │ ┌─┐ │ │ ┌─┐ │ │ ┌─┐ │                                                
└─┘ └─┘ └─┘ └─┘ └─┘ └─┘ └─┘ └─┘  
```

View the original code [here](https://nostarch.com/big-book-small-python-projects).

**Tags**: _large_, _artistic_

___

## TODO List

* [x] ~~Add a reset option~~

Currently, the "(C)lear" option erases the board, but it does not reset the cursor position to (0,0). I just need to add a few lines in to create a "(R)eset option that both erases the canvas _AND_ resets the cursor position to (0,0).



