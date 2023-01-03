#GCD= Greatest Common Divisor

# divisor
# common divisor
# greatest divisor

# 4           18
# 18=4*4 +2(reminder)
# 4= 2*2 +0
# 2=0

# import math
# print(math.gcd(64,48))
# print(math.gcd(4,18))

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(18,4))
