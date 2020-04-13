# Basic string concatenation

def mystery1(value):
    s = ""
    for i in range(value):
        s += str(i)
    return s

def mystery2(value):
    s = ""
    for i in range(value):
        s = str(i) + s
    return s

def mystery3(value):
    s = ""
    for i in range(value):
        if (i % 2 == 0):
            s = str(i) + s
    return s

def mystery4(value):
    s = ""
    for i in range(value):
        if (i % 2 != 0):
            s = str(i) + s
    return s


print(mystery1(5))

print(mystery2(5))

print(mystery3(5))

print(mystery4(5))
