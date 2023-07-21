'''n=int(input())
for i in range(n):
    for j in range(n-2):
        if j==0 or j==(n-2-1):
            print("*",end=" ")
        elif i==0 or i==(n//2):       this is for box type A with sharp edges
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''i=row
j=column'''



n=int(input())
for i in range(n):
    for j in range(n-2):
        if i==0 and (j==0 or j==(n-2-1)):
            print(" ",end=" ")
        elif j==0 or j==(n-2-1):
            print("*",end=" ")
        elif i==0 or i==(n//2):      
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
