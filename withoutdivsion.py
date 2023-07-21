'''a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
rem=a%b
div=0
if a<b:
    print(0)
else:
    for i in range(0,a):
        div=(b*i)+rem
        if div==a:
            print(i)
            break'''






a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
div=0
while a>=b:
    div+=1
    a-=b
print(div)

