n=str(input())
d=0
for i in n:
  if i=='0' or i=='1':
    d=1
  else:
    d=0  
if d==1:
  print("yes") 
elif d==0:
   print("no")  
