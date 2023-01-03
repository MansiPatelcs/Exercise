s=input('Enter the string:')

a1=0
a=0

for i in s:
    if i.isnumeric():
        a1=a1+1
    else:
        a=a+1
print('Total digits found',a1)
print('Total letters found',a)

