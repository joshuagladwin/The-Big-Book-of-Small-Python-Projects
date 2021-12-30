# Diamonds
___
_by Al Sweigart_ [al@inventwithpython.com](mailto:al@inventwithpython.com)

Draws diamonds of various sizes.

View the original code [here](https://nostarch.com/big-book-small-python-projects).

**Tags**: _tiny_, _beginner_, _artistic_

___
```
                                                     /\         /\
                                                    /  \       //\\
                                  /\       /\      /    \     ///\\\
                                 /  \     //\\    /      \   ////\\\\
                   /\     /\    /    \   ///\\\  /        \ /////\\\\\
                  /  \   //\\  /      \ ////\\\\ \        / \\\\\/////
        /\   /\  /    \ ///\\\ \      / \\\\////  \      /   \\\\////
       /  \ //\\ \    / \\\///  \    /   \\\///    \    /     \\\///
/\ /\  \  / \\//  \  /   \\//    \  /     \\//      \  /       \\//
\/ \/   \/   \/    \/     \/      \/       \/        \/         \/
```

## TODO List:

* [x] ~~Create scripts for other shapes, e.g. triangle, rectangle, rhombus.~~

`triangle.py` 

```
                                                    /\         /\   
                                 /\       /\       /  \       //\\  
                  /\     /\     /  \     //\\     /    \     ///\\\ 
       /\   /\   /  \   //\\   /    \   ///\\\   /      \   ////\\\\
/\ /\ /__\ //\\ /____\ ///\\\ /______\ ////\\\\ /________\ /////\\\\\
```

`rectangle.py`

```
                                             _____   _____
                               ____   ____  |     | |#####|
                   ___   ___  |    | |####| |     | |#####|
         __   __  |   | |###| |    | |####| |     | |#####|
 _   _  |  | |##| |   | |###| |    | |####| |     | |#####|
|_| |#| |__| |##| |___| |###| |____| |####| |_____| |#####|
```

`rhombus.py`

```
                                                             ______      ______
                                        _____     _____     /     /     /#####/
                       ____    ____    /    /    /####/    /     /     /#####/
          ___   ___   /   /   /###/   /    /    /####/    /     /     /#####/
 __  __  /  /  /##/  /   /   /###/   /    /    /####/    /     /     /#####/
/_/ /#/ /__/  /##/  /___/   /###/   /____/    /####/    /_____/     /#####/
```

* [x] ~~Output the shapes to a text file.~~

`diamonds_to_file.py` uses the modified `return_outline_diamond()` and `return_outline_diamond()` to return strings with  the diamonds produced by `display_outline_diamond()` and `display_outline_diamond()`. These can then easily be written to a text file, `diamonds.txt`.
