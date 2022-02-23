# Hitomezashi-Stitch-Patterns

Hitomezashi stitch patterns, discussed in [this Numberphile video](https://youtu.be/JbfhzlMk2eY), takes two binary type strings to create a stitching pattern. The state of each element of the string determines whether its stitch starts in the first position or the second position. 

The `stitch_pattern` takes two phrases as inputs. First phrase determines the starting positions of the horizontal stitches (going from left to right). The second phrase determines the starting positions of the verticle stitches (going from top to bottom). Each letter represents a stitch. If the letter is a vowel, then the stitch starts in the first position. If it's a consenant, the sticht begins in the second position. 

Imputing the phrase "Hello! My name is Casey and I am new to GitHub" as phrase 1 and "This is my code. I hope you like it!" as phrase two yeilds the stitch pattern below.

![Hitomezashi Stitch, Phrase 1 HELLOMYNAMEISCASEYANDIAMNEWTOGITHUB, Phrase 2 THISISMYCODEIHOPEYOULIKEIT](https://user-images.githubusercontent.com/74943315/155252536-8d7174de-a602-497c-a7d8-c4e5da151b31.png)
