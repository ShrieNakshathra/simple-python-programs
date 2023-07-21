#print each digit of number without str() type cast

num=int(input())
while(num>0):
    t=num%10
    num//=10
    print(t)
