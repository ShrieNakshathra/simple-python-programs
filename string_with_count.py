#a program to return string with its counts
string=input()
for i in string:
  count=0
  for j in string:
     if(i==j):
         count+=1
  print(i,count,sep=" ",end=" ")
