n=int(input('Enter the number:'))

if n%2 == 0:
    print(n,'is a Even number')
else:
    print(n,'is a Odd number')


def odd_even(n):
    if n%2==0:
        print('EVEN')
    else:
        print('ODD')
odd_even(2)
odd_even(10)
odd_even(100)
odd_even(1111)
