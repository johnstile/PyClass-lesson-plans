#!/usr/bin/env python


"""
Surprised with the result? Remember the .* value - this value catches ANYTHING. The result is that the whole string is matched.
How do we extract the information we want??
Grouping! https://docs.python.org/2/howto/regex.html#grouping
Move on to regex2.py.
"""
import re

# string we are trying to mach
test_string_1 = "This is a test string."

# the parenthesis allow the match to be accessed
#regex_extraction_str = r'(.*)(test)(.*)'
#regex_extraction_str = r'(.*)((t)est)(.*)'
regex_extraction_str = r'(.*)((t)(e)st)(.*)'

# compile the regex on the pattern string above
pg = re.compile(regex_extraction_str)

# still using test_string_1
matched_group = pg.match(test_string_1)
print "group:", matched_group.group()
print "start:", matched_group.start()
print "end:", matched_group.end()
print "span:", matched_group.span()

print "Still the whole match: %s" % test_string_1[matched_group.start(): matched_group.end()]
print
print "Now the whole group: %s" % matched_group.group()
print "The whole group once more: %s" % matched_group.group(0) # same as if nothing, whole string
print "And our first group: %s" % matched_group.group(1) # prints the target
print "And our second group: %s" % matched_group.group(2) # prints the target
print "And our third group: %s" % matched_group.group(3) # prints the target
print "And our fourth group: %s" % matched_group.group(4) # prints the target
# side note: strings can be nested
print "Number of matching groups:", pg.groups
# show there is a list of matches.
# need to add one... for the zero group
print range(pg.groups+1)
# Star the tuple unpacks the tuple.
print matched_group.group( *tuple(range(pg.groups+1)) )
#
# Know these: https://docs.python.org/2/library/re.html
# search(), match(),
# findall(), -> return list
# finditer() - > returns iterator
#
print "group index:"
for key in pg.groupindex.keys() :
    print pg.groupindex[key]
print "------------------------------------"
#
# module level things are faster
#
print "Try matching dynamicly: ", re.match(r'From\s+', 'Fromage amk')

str_1 = 'This is a test sring.'
match_obj = re.match(r'test', str_1)
srch_obj = re.search(r'test', str_1)
print srch_obj.string
print srch_obj.group()
print srch_obj.groups()

