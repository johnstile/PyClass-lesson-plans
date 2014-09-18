#!/usr/bin/env python

# print the docstring for the object
# print dir.__doc__

# print all the first files
#dir()

# look up the the sub stuff
#dir(__builtin__)

# print id.__doc__

# enter help
#help()

# prompt changes to "help>"
#help> keywords

#----------------------------
lol = list()           # create empty list
for num in range(5):   # Loop from 0 to 5, num = x
    lol.append(list()) # Add anohter list to the list

print lol   # Print  list-of-lists
# Output:  [[], [], [], [], []]

for each in lol:       # for each list
    print id(each)     # print the memory address of each sub-list

# globals() will dump all items in your current namespace
print globals.__doc__
# globals() -> dictionary
# Return the dictionary containing the current scope's global variables.

globals()

import functools

print dir(__builtins__.__doc__)


# https://docs.python.org/2/library/functions.html
# dir(), help(), globals(), input(), open(), rawinput()
# hash(), len(), range(), enumerate(), zip(), any(), all()
# map()


# Old format
print "this list %s" % ls
# New format  of string formatting
print "this list: {}".format(ls)





