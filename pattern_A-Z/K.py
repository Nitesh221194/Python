i=0
j=4
for row in range(7):
    for col in range(5):
        if (col==0)or(row==col+2 and col>1):
            print('*',end=" ")
        elif(row==i and col==j):
            print('*',end=" ")
            i+=1
            j-=1
        else:
            print(end="  ")
    print()

    # (col == 0) or ((col == 4) and (row == 0)) or ((col == 3) and (row == 1)) or ((col == 2) and (row == 2)) or (
    #             (col == 1) and (row == 3)) or ((col == 2) and (row == 4)) or ((col == 3) and (row == 5)) or (
    #             (col == 4) and (row == 6)):