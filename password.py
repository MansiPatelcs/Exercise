a=input('Enter the password:')
upper=0
lower=0
character=0
number=0

print(len(a))

if len(a)<=6:
    print('please, enter more than 6 character')
elif len(a)>=16:
    print('please,enter less than 16 character')
else:
    for x in a:
        if x.isupper:
            upper=upper+1
        if x.islower:
            lower=lower+1
        if x.isdigit:
            number=number+1
        if x=='$' or x=='#' or x=='@':
            character=character+1

if number>=1 and lower>=1 and upper>=1 and character>=1:
    print('yes')
else:
    print('no')

