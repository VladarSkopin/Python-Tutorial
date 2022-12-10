# . -> any character except \n
# ? -> 0 or 1
# + -> 1 or many
# * -> 0 or many
# \w -> digit ar letter
# \W -> any except digit or letter
# \d -> digit
# \D -> any except digit
# \s -> whitespace
# \S -> any except whitespace
# \b -> word boundary ???
# [a-z]
# ^ -> starts with
# $ -> ends with
# {n, m}
# a|b -> a or b
# ESCAPE SEQUENCE: \. \? \- \+ \* \^ \$

import re

logfile = open('logfile.txt', 'r')
for string in logfile:
    if re.findall(r'Did not receive', string):
        print(re.findall(r'\d+\.\d+\.\d+\.\d+', string))

