for row in range (1, 3):
    for col in range (1,8):
        if row == 1:
            if col == 2 or col == 3 or col == 5 or col == 6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif row == 2:
            if col == 1 or col == 4 or col == 7:
                print("*",end=" ")
            else:
                print(" ", end=" ")
    print()
cols = 7
for row in range(4,0,-1):
    for space in range(1,4-row+1):
        print(" ",end=" ")
    for col in range(1,cols+1):    # cols == cols checking for last column in the row 
        if row == 1 or col == 1 or col == cols :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    cols -= 2 
