n,k=input().split()
m=[str(i) for i in input().split()]
x=sorted(m)
d=0
for i in range(0,len(x)):
  if x[i]==k:
    d=1 
if d==1:
  print("Yes")   
else:
  print("No")   
