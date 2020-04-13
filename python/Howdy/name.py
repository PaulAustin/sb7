


name = "안녕 세상"
# data = bytes(name, 'utf-8')

def rev(name):
    newname = ''
    for c in name:
        newname = c + newname
    return newname

print(name, rev(name))

