#!/usr/bin/env python3
#
# Making an argument, or rather taking arguments
# taking as many as you want to make

#import the 'system' object
import sys

print ("Vector of arguements List:", sys.argv)
print ("Number of arguments passed:", len(sys.argv))

i = 0
for arg in sys.argv:
    print("arg", i, "-", arg)
    i += 1

numBubbles = 0
if len(sys.argv) > 1:
    numBubbles = sys.argv[1]

print("number of bubbles requested", numBubbles)
print("numBubbles type is", type(numBubbles))

# Let's add a few more
numBubbles = numBubbles + 10
print("number of bubbles to make", numBubbles)

# How did that work out?
