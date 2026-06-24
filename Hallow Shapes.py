counter = 1
for row in range(1,6):
    for col in range(1,6):
        if row == 1 or row == 5 or col == 1 or col == 5:
            print(counter,end=" ")
        else:
            print(" ",end=" ")
        counter += 1
    print()
print("-----------------")
counter = 1
for row in range(1,6):
    for col in range(1,6):
        if row == 1 or row == 5 or col == 1 or col == 5:
            print(counter,end=" ")
            counter += 1
        else:
            print(" ",end=" ")
        
    print()
print("----------------")
cols = 1
counter = 1
for row in range(1,6):
    for col in range(1,cols+1):
        if row == 1 or col == 1 or row == col or row == 5:
            print(counter,end=" ")
        else:
            print(" ",end=" ")
        counter += 1
    cols += 1 
    print()
print("----------------")
cols = 1
counter = 1
for row in range(1,6):
    for col in range(1,cols+1):
        if row == 1 or col == 1 or row == col or row == 5:
            print(counter,end=" ")
            counter += 1
        else:
            print(" ",end=" ")
    cols += 1 
    print()
print("----------------")
counter = 1
for row in range(5,0,-1):
    for space in range(1,row+1):
        print(" ",end="")
    for col in range(1,6-row+1):
        print(counter,end=" ")
        counter += 1
    print()
        
