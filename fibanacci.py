n=int(input("Enter how many input:"))

'''count=0
n1,n2=0,1
nth=0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms==0 or nterms==1:
   print(n1,n2)
else:
    while nterms>1:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
    
        if nterms==n1:
            break'''

        
a=0
b=1
c=0
for i in range(1,n+1):
    print(c,end=" ")
    c=a+b
    b=a
    a=c
