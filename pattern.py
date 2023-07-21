row=int(input())
a=1
for i in range(row):
    print(" "*(row-1-i),end="")
    print("*"*a)
    a+=2
