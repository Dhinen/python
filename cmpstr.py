n=input()
m=input()
s=0
for i in m:
   if i in n:
     s=1
   else:
     s=2
     break
if s==1:
  print("Yes")  
else:
  print("No")     
