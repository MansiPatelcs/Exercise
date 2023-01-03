l=[10,20,4,45,99]

l.sort()
print(l)

print('2nd largest number',l[-2])


l1=set(l)
print(l1)

l1.remove(max(l1))
print(l1)
print(max(l1))


