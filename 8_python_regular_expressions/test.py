#!/usr/bin/env

import re
#
# Regex:  one or more chars, then test 
#
regex_example_string1 = r'.*test.*'
regex_example_string2 = r'+test+'

#
# Create regex objects, second is case insensetive
#
p = re.compile(regex_example_string1)
p1 = re.compile(regex_example_string1, re.IGNORECASE)

#
# Display the objects
#
print(p)
print(p1)

#
# Test string
#
test_string_1 = "This is a test string."
#
# This capitolizes first letter of each word
#
test_string_2 = test_string_1.title()

#
# display the test strings
#
print "Test String 1", test_string_1
print "Test String 2", test_string_2

#
# Search string for a match
#
print "Test1: RE: p = ", p.match(test_string_1)     # Returns object
print "Test1: RE: p1 = ", p1.match(test_string_1)   # Returns object

print "Test2: RE: p = ", p.match(test_string_2)     # returns None
print "Test2: RE: p1 = ", p1.match(test_string_2)   # Returns object

#---------------------------------------------------
# 
matched = p.match(test_string_1)
print "group:", matched.group()
print "start:", matched.start()
print "end:", matched.end()
print "span:", matched.span()
print "len:", len(test_string_1)

# Grouping  https://docs.python.org/2/howto/regex.html#grouping



