for row in range(7):
    for col in range(6):
        if (col==0)or ((row>0 and row<3)and(col==5)):
            print('*',end=" ")
        elif((row==0 or row ==3)and (col<5)):
            print('*',end=" ")
        else:
            print(end="  ")
    print()