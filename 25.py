l = [1,5,8,3]
l=[1,5,8,3]

print(3 in l)
print(-1 in l)


def value(list,n):
    for i in list:
        if n==i:
            return True
    return False

print(value([1,5,8,3],3))
print(value([1,5,8,3],-1))

