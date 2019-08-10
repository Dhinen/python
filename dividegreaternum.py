n=[int(i) for i in input().split()]
s=n[0]
d=n[1]
e=s*d
f=0
for i in range(1,len(n)):
  if n[i]%s==0:
    x1=e//s 
    x2=e//d 
    f=1
  else:
    f=0  
if f==0:
   if s>d:
     print(s-d)
   else:
      print(d-s) 
else:     
  if x1>x2:
    print(s)  
  else:
    print(d)   
