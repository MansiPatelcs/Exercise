l = [11,100,22,3,10,5]

l.sort()
print(l)

l=(4,2,3)
y=list(l)
y.sort()

print(tuple(y))

x=int(input('Input first number:'))
y=int(input('Input second number:'))
z=int(input('Input third number:'))

a1= min(x,y,z)
a3= max(x,y,z)
a2= (x+y+z)-a1-a3

print('Numbers in sorted order:',a1,a2,a3)
