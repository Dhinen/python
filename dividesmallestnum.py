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
if f!=1:
  print(e)
else:     
  if x1<x2:
    print(s)  
  else:
    print(d)   
