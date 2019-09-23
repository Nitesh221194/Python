for row in range(7):
    for col in range(7):
        if ((col==0 or col==6) and row!=6):
            print('*',end=" ")
        elif((col>0 and col<6)and row==6):
            print('*',end=" ")

        else:
            print(end="  ")
    print()







