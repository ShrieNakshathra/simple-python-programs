row=int(input())
for i in range(row):
    for j in range(row-2):
        if j==0 or i==0 or i==row//2 or i==row-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
