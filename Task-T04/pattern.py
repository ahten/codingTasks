"""
Follow these steps:
● Create a new Python file in this folder called pattern.py.
● Write code to output the arrow pattern shown below, using an if-else
statement in combination with a for loop
o You are allowed to use more than one for loop. But use only one for
loop if you wish to challenge yourself):

*
**
***
****
*****
****
***
**
*

"""

# there are total 9 lines , first 5 lines are increasing and last 4 lines are decreasing

for i in range(9):
    if i < 5:
        print("*" * (i + 1))
    else:
        print("*" * (9 - i))
