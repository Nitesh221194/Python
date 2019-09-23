for row in range(7):
    for col in range(7):
        if (row==0)or((col==3)and(row!=6))or((row==6)and (col>0 and col<3))or((row==4 or row==5)and col==0):
            print('*',end=" ")
        else:
            print(end="  ")
    print()