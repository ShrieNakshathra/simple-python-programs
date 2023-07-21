row=int(input())
for i in range(row):
    for j in range(row-2):
        if i==0 or i==row-1 or j==0:
            if(i==0 or i==row-1) and j==0:
                print(" ",end=" ")
            else:
                print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
