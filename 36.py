def add(a,b):
    if not(isinstance(a,int) and isinstance(b,int)):
        return 'Inputs must be integers!'

    return a+b
print(add(10,20))
print(add(10,"20"))
print(add(10,20.23))
print(add("10","20"))
