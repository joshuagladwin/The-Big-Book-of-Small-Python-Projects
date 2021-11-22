# Caesar Hacker
____
_by Al Sweigart_ [al@inventwithpython.com](mailto:al@inventwithpython.com)

This program hacks messages encrypted with the Caesar cipher by doing a brute force attack against every possible key.
More info [here](https://en.wikipedia.org/wiki/Caesar_cipher#Breaking_the_cipher).

View the original code [here](https://nostarch.com/big-book-small-python-projects).

**Tags**: _tiny_, _beginner_, _cryptography_, _math_
____

Using the same `symbols`* as defined in [Project #6](../Project%20%236%20Caesar%20Cipher), you can easily try:

```
Enter the encrypted Caesar cipher message to hack.
> 7V££5}¬¤v¥5wz~¥|ª5v©z5w¦©¥5{©zz5v¥y5z¨¬v£5~¥5y~|¥~«±5v¥y5©~|}«ªC5i}z±5v©z5z¥y¦¯zy5¯~«}5©zvª¦¥5v¥y5x¦¥ªx~z¥xz5v¥y5ª}¦¬£y5vx«5«¦¯v©yª5¦¥z5v¥¦«}z©5~¥5v5ª§~©~«5¦{5w©¦«}z©}¦¦yC7

Key #0: 7V££5}¬¤v¥5wz~¥|ª5v©z5w¦©¥5{©zz5v¥y5z¨¬v£5~¥5y~|¥~«±5v¥y5©~|}«ªC5i}z±5v©z5z¥y¦¯zy5¯~«}5©zvª¦¥5v¥y5x¦¥ªx~z¥xz5v¥y5ª}¦¬£y5vx«5«¦¯v©yª5¦¥z5v¥¦«}z©5~¥5v5ª§~©~«5¦{5w©¦«}z©}¦¦yC7
Key #1: 6U¢¢4|«£u¤4vy}¤{©4u¨y4v¥¨¤4z¨yy4u¤x4y§«u¢4}¤4x}{¤}ª°4u¤x4¨}{|ª©B4h|y°4u¨y4y¤x¥®yx4®}ª|4¨yu©¥¤4u¤x4w¥¤©w}y¤wy4u¤x4©|¥«¢x4uwª4ª¥®u¨x©4¥¤y4u¤¥ª|y¨4}¤4u4©¦}¨}ª4¥z4v¨¥ª|y¨|¥¥xB6
Key #2: 5T¡¡3{ª¢t£3ux|£z¨3t§x3u¤§£3y§xx3t£w3x¦ªt¡3|£3w|z£|©¯3t£w3§|z{©¨A3g{x¯3t§x3x£w¤¬xw3¬|©{3§xt¨¤£3t£w3v¤£¨v|x£vx3t£w3¨{¤ª¡w3tv©3©¤¬t§w¨3¤£x3t£¤©{x§3|£3t3¨¥|§|©3¤y3u§¤©{x§{¤¤wA5
--snip--
Key #20: #Bmm!ivnbo!cfjoht!bsf!cpso!gsff!boe!frvbm!jo!ejhojuz!boe!sjhiut/!Uifz!bsf!foepxfe!xjui!sfbtpo!boe!dpotdjfodf!boe!tipvme!bdu!upxbset!pof!bopuifs!jo!b!tqjsju!pg!cspuifsippe/#
Key #21: "All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood."
--snip--
```

***Extension Idea**: One interesting point to note is that this requires the exact list of symbols and in the exact same order as used in the encryption. It wouldn't be *too* difficult to brute force your way to the correct order (`n!` possible combos). Though, without knowledge of which and how many symbols are used, you'd need to keep intercepting encrypted messages until you've enough to determine the set of symbols used in the encryption. 

That being said, a Caesar Cipher is a simple enough form of encryption that it might be easier to decrypt linguistically, e.g. identifying patterns in the encrypted message, performing a statistical analysis of the symbol distribution and comparing it to letter distribution in English, etc.
