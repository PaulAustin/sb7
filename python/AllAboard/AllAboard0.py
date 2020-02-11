#!/usr/bin/env python3
#
# Making an argument, or rather taking arguments
# taking as many as you want to make

#import the 'system' object
import sys

print ("Which python is being run?" , sys.executable)
print ("Vector of arguements List:", sys.argv)
print ("Number of arguments passed:", len(sys.argv))

