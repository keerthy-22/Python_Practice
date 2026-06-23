for row in range(1,6):
    for col in range(1,6):
        if row == 1 or row == 5 or col == 1 or col == 5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print(-----------)

cols = 5 
for row in range(5,0,-1):
    for col in range(cols,0,-1):
        if row == 1 or col == 1 or row == col or row == 5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        print(" ",end=" ")
    cols -= 1 
    print()






