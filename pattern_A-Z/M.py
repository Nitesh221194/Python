i=4
for row in range(7):
    for col in range(5):
        if (col==0 )or (row==col<3):
            print('*',end=" ")

        elif (col==4)or(col==i and row<2):
            print('*',end=" ")
            i-=1
        else:
            print(end="  ")
    print()