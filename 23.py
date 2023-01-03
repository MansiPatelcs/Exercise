def substring(str, n):
    a=2
    if a > len(str):
        a=len(str)
    substr = str[:a]

    result= ' '
    for i in range(n):
        result=result+substr
    return result

print(substring('abcdef', 2))
print(substring('p', 3))

n=int(input('enter the number'))
str=input('enter the str')
flag=''
for i in range(n):
    flag=flag+str[i]
print(flag*n)

def newstr(str,n):
    if len(str)<2:
        return str*n
    return str[:2]*n

print(newstr('ab',5))
print(newstr('a',10))


