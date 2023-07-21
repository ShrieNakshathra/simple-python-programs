num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
divisor=0
for i in range(1,min(num1,num2)+1):
    if num1%i==num2%i==0:
        divisor=i
        print("The common divisor of",num1,"and",num2,"are:",divisor)
        break
