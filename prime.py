number=int(input("Enter the number:"))
if number==1:
    print( number ,"is not a prime number")
elif number==2:
    print(number,"is a prime number")
    
elif number>1:
    for i in range(2,int(number/2)+1):
        if (number%i)==0:
            print(number," is not prime number")
            break
    else:
        print(number ,"is prime number")

            
