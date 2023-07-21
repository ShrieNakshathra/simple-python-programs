row=int(input())
for i in range(row):
    for j in range(row-2):
        if j==0 or j==row-2-1 or i==0 or i==(row-1) or i==row//2:
            if(i==0 or i==row//2 or i==row-1) and j==row-2-1:
                print(" ",end=" ")
            else:
                print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
