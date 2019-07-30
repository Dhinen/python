n,k=[int(i) for i in input().split()]
m=[int(i) for i in input().split()]
d=0
for i in m:
  if k==i:
    d=1
if d==0:
  print("no")   
else:
  print("yes")   
