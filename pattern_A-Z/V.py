i=14
for row in range(8):
    for col in range(15):
        if (col==i>6):
            print('*',end=" ")
            i-=1
        elif col==row:
            print('*',end='')
        else:
            print('',end=" ")
    print()