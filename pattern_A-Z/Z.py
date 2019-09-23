i=5
for row in range(7):
    for col in range(7):
        if(row==0 or row==6):
            print('*',end=' ')

        elif(col==i):
            print('*',end=' ')
            i=i-1

        else:
            print(' ',end=' ')
    print()