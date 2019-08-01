n,l=input().split()
m=[str(i) for i in input().split()]
k=[str(i) for i in input().split()]
d=0
for i in k:
  if i in m:
    d=1
  else:
    d=0  
if d==1:
  print("YES") 
else:
  print("NO")     
