# A simple recursive function credited to Wilhelm Ackermann
# https://en.wikipedia.org/wiki/Ackermann_function

def ackermann(m, n):
    if m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n -1))
    elif m == 0:
        return n + 1
    else:
        print("Could this line ever happen?")

print (ackermann(3, 6))
# print (ackermann(2, 3))
# print (ackermann(1, 1))
# print (ackermann(4, 2)) # that should be easy.
