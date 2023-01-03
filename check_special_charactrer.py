import re

# str='welcome@@2To%%Python**Programing'
str='welcome to python programing'

regex=re.compile('[@_!#$%^&*()<>?/\|}{~:]')

if(regex.search(str)==None):
    print('NO SPECIAL CHARACTER')
else:
    print('PRESENT SPECIAL CHARACTER')
