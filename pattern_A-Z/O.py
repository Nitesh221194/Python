for row in range(7):
    for col in range(7):
        if ((row==0 or row==6)and(col>1 and col<5)):
            print('*',end=" ")

        elif((row==1 or row==5)and(col==1 or col==5)):
            print('*',end=" ")

        elif((col==0 or col==6)and (row>1 and row<5)):
            print('*', end=" ")
        else:
            print(end="  ")
    print()







