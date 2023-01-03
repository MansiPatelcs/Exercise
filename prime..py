# number > 1
# which has only 2 factors 1 and itself

# n=int(input('Enter number:'))
#
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print('Not Prime')
#             break
#     else:
#         print('Prime')


# for i in range(2,100):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i,end=' ')

num=5
count=0
if num>1:
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        print('Number is prime')
    else:
        print('Number is not prime')
