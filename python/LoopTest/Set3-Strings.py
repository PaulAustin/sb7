# String work

def Mystery1(s):
    count = 0
    for c in s:
        if c.isspace():
            count += 1
    return count

def Mystery2(s):
    count = 0
    for c in s:
        if c.isnumeric():
            count += 1
    return count

def Mystery3(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1
    return count

def Mystery4(s):
    count = 0
    for c in s:
        if c.islower():
            count += 1
    return count

def Mystery5(s):
    count = 0
    for c in s:
        if c.isalpha():
            count += 1
    return count

def Mystery6(s):
    count = 0
    for c in s:
        if c.isalnum():
            count += 1
    return count

arg ="1200 big Bumble Bees in the bush"
print(arg, Mystery1(arg))
print(arg, Mystery2(arg))
print(arg, Mystery3(arg))
print(arg, Mystery4(arg))
print(arg, Mystery5(arg))
print(arg, Mystery6(arg))
