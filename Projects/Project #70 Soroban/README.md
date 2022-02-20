Soroban - The Japanese Abacus
===
___
_by Al Sweigart_ [al@inventwithpython.com](mailto:al@inventwithpython.com)

A simulation of a Japanese abacus calculator tool.

More info [here](https://en.wikipedia.org/wiki/Soroban).

View the original code [here](https://nostarch.com/big-book-small-python-projects).

**Tags**: _large_, _artistic_, _math_, _simulation_
___

The number 42692022:

```
+================================+
I  O  O  O  O  |  |  O  O  O  O  I
I  |  |  |  |  |  |  |  |  |  |  I
I  |  |  |  |  O  O  |  |  |  |  I
+================================+
I  |  |  O  O  O  O  O  |  O  O  I
I  |  |  O  O  |  O  O  |  O  O  I
I  O  O  O  |  |  O  |  O  |  |  I
I  O  O  O  O  O  O  O  O  O  O  I
I  O  O  |  O  O  |  O  O  O  O  I
I  O  O  |  O  O  |  O  O  O  O  I
+==0==0==4==2==6==9==2==0==2==2==+
```


TODO List:
---

- Implement the "Dots" to allow for decimals.

There are dots on the real physical versions of a Soroban, on every third rod. Rods to the right of the dotted rod can then be used to represent decimals.

- [ ] Set a fixed Dot.

Add a dot to rod 7. Start 1s, 10s, 100s, etc from Rod 7 to the left. Rods 8 and 9 then represent 10ths and 100ths. Would be useful for calculations involving money (e.g. €, £, $). This reduces the max possible number to 99,999,999.99: 

```
+================================+
I  O  O  O  O  O  O  O  O  O  O  I
I  |  |  |  |  |  |  |  |  |  |  I
I  |  |  |  |  |  |  |  |  |  |  I
+=======================.========+
I  |  |  |  |  |  |  |  |  |  |  I
I  |  |  |  |  |  |  |  |  |  |  I
I  O  O  O  O  O  O  O  O  O  O  I
I  O  O  O  O  O  O  O  O  O  O  I
I  O  O  O  O  O  O  O  O  O  O  I
I  O  O  O  O  O  O  O  O  O  O  I
+==0==0==0==0==0==0==0==0.=0==0==+
```

- [ ] Allow User to choose the dot to start at.

Place two more dots on the board, on Rod 1 and Rod 4.
Before starting the calculations, allow the user to enter 0, 1, 2, or 3 to select which of the three dots to set or none (0)

```
+================================+
I  O  O  O  O  O  O  O  O  O  O  I
I  |  |  |  |  |  |  |  |  |  |  I
I  |  |  |  |  |  |  |  |  |  |  I
+=====.========.========.========+
I  |  |  |  |  |  |  |  |  |  |  I
I  |  |  |  |  |  |  |  |  |  |  I
I  O  O  O  O  O  O  O  O  O  O  I
I  O  O  O  O  O  O  O  O  O  O  I
I  O  O  O  O  O  O  O  O  O  O  I
I  O  O  O  O  O  O  O  O  O  O  I
+==0==0.=0==0==0.=0==0==0.=0==0==+
```
