i=1
j=3
for row in range(7):
    for col in range(7):
        if(row>j and col>i):
            print('*',end=' ')
            j=j+1
            i=i-1

        elif col==0 or (col==6)or (row==col>2):
            print('*',end=' ')


        else:
            print(' ',end=' ')
    print()