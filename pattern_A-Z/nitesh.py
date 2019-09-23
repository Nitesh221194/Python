for row in range(7):
    for col in range(7):
        if ((col==0)or(row==col))or(col==6):
            print('*',end=" ")
        else:
            print(end="  ")
    for col in range(1):
        print(' ',end=' ')

    for col in range(7):
        if (row==0 or row==6)or((col==3)and (row!=0 and row!=6)):
            print('*',end=" ")
        else:
            print(end="  ")

    for col in range(1):
        print(' ',end=' ')

    for col in range(7):
        if (col==3)or(row==0):
            print('*',end=" ")
        else:
            print(end="  ")

    for col in range(1):
        print(' ',end=' ')


    for col in range(5):
        if (col==0)or ((row==0 or row==3 or row==6)and (col>0)):
            print('*',end=" ")
        else:
            print(end="  ")

    for col in range(1):
        print(' ',end=' ')


    for col in range(7):
        if ((row==0 or row==3 or row ==6) and (col<6 and col>0)):
            print('*',end=" ")
        elif(col==0 and (row<3 and row>0)) or (col==6 and (row>3 and row<6)):
            print('*',end=" ")
        else:
            print(end="  ")

    for col in range(1):
        print(' ',end=' ')


    for col in range(6):
        if (col==0 or col==5) or ((col>0 or col<5)and row==3):
            print('*',end=" ")
        else:
            print(end="  ")
    print()






