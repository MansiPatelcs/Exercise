for i in range(7):
    for j in range(5):
        if j==0 or (i%3==0 and j!=0):
            print('*',end=' ')
        else:
            print(end=' ')
    print()


for i in range(7):
    for j in range(5):
        if (i in {0,3,6} and j in {0,1,2,3,4}) or (i in {1,2,4,5}):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
