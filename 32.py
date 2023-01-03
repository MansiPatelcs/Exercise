# LCM = Least Common Multiple
"""smallest non zero common number which is the multiple of both the numbers"""

#24  - 24,48,72,96...............    # 72
#36  - 36,72,108,144............     #72

# 24= 2*2*2*3
# 36=2*2*3*3   #2*2*2*3*3=72

# import math
# print(math.lcm(4,18))
# print(math.lcm(24,36))

def lcm(a,b):
    if a>b:
        higher=a
    else:
        higher=b
    value=higher
    while True:
        if higher%a==0 and higher%b==0:
            print('LCM of',a ,'and',b,'is', higher)
            break
        else:
            higher= higher+value
lcm(24,36)
