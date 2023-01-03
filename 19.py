def newstr(str):
    if len(str) >= 2 and str[:2]=='Is':
        return str
    else:
        return 'Is' + str

print(newstr('ArrayIs'))
print(newstr('IsEmpty'))
print(newstr('Is it true'))
