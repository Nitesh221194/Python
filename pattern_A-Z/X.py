i=6
for row in range(7):
    for col in range(7):
        if(col==row<3 or col==row>3):
            print('*',end=' ')
        elif(col==i):
            print('*',end=' ')
            i=i-1
        else:
            print(' ',end=' ')
    print()