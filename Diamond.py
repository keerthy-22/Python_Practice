#Diamond
n = 5 
for row in range(1,n+1):
    for space in range(1,(n-row)+1): 
        # row = 1 -> 5 - 1 + 1 = 5 
        # row = 2 -> 5 -2 + 1 = 4 
        # row = 3 -> 5 - 3 + 1 = 3 
        print(" ",end="")
    for col in range(1,row+1):
       print("*",end=" ")
    print()

#  * * * * * 
#   * * * *
#    * * *

for row in range(n-1,0,-1):
    for space in range(1,n-row+1):
        print(" ",end="")
        
    for col in range(1,row+1):
         print("*",end=" ")
    print()
#Hollow Diamond
n = 5 
for row in range(1,n+1):
    for space in range(1,(n-row)+1): 
        # row = 1 -> 5 - 1 + 1 = 5 
        # row = 2 -> 5 -2 + 1 = 4 
        # row = 3 -> 5 - 3 + 1 = 3 
        print(" ",end="")
    for col in range(1,row+1):
        if col == 1 or row ==1 or row == col:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#  * * * * * 
#   * * * *
#    * * *

for row in range(n-1,0,-1):
    for space in range(1,n-row+1):
        print(" ",end="")
        
    for col in range(1,row+1):
        if col == 1 or row ==1 or row == col:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
