#num=5
#1*2*3*4*5=120

# factorial=1
# num=10
# if num<0:
#     print('Factorial does not exist for negative number')
# elif num==0:
#     print('The factorial of 0 is 1')
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print('The factorial of', num, 'is',factorial)

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))
# print(factorial(10))
# print(factorial(2))


def factorial(n):
    return 1 if(n==1 or n==0) else n* factorial(n-1)
print(factorial(5))
