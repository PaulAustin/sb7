#!/usr/bin/env python3
#
# Making an argument, or rather taking arguments
# taking as many as you want to make

#import the 'system' object
import sys

print ("Vector of arguements List:", sys.argv)
print ("Number of arguments passed:", len(sys.argv))

numBubbles = 2
if len(sys.argv) > 1:
    print("argv[1] argument type is", type(sys.argv[1]))
    numBubbles = int(sys.argv[1])
    print("Requested number of bubbles:", numBubbles)
else:
    print("Using default number of bubbles", numBubbles)

# How did that work out?
# What happens If we dont pass the right argument?

