items=[]
a=int(input('enter 4 digit number made from 0 and 1:'))
num=[x for x in a().split(',')]
for p in num:
    x=int(p,2)
    if not x%5:
        items.append(p)
print(','.join(items))
