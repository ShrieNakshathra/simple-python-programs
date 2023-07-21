r=int(input("enter the number:"))
pi=3.14
area=pi*r*r
print("area of circle=",int(area))






n=int(input("Enter the number: "))
c=0
a=1
b=1
if n==0 or n==1:
    print("Yes")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("Yes")
    else:
        print("No")







        string = "Great responsibility";  
   
print("Duplicate characters in a given string: ");  
#Counts each character present in the string  
for i in range(0, len(string)):  
    count = 1;  
    for j in range(i+1, len(string)):  
        if(string[i] == string[j] and string[i] != ' '):  
            count = count + 1;  
            #Set string[j] to 0 to avoid printing visited character  
            string = string[:j] + '0' + string[j+1:];  
   
    #A character is considered as duplicate if count is greater than 1  
    if(count > 1 and string[i] != '0'):  
        print(string[i]);  
