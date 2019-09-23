for row in range(7):
    for col in range(6):
        if ((row==0 or row==3 or row==6) and col>1) or ((col==0) and (row>1 and row<5)) or ((row==1 or row==5)and (col==1)) or ((row==4 or row==5)and col==5):
            print('*',end=" ")
        else:
            print(end="  ")
    print()