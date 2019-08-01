n,l=input().split()
m=[int(i) for i in input().split()]
k=[int(i) for i in input().split()]
d=0
for i in m:
  for j in k:
    if i==j:
      d=1
if d==1:
  print("YES")
elif d!=1:
  print("NO")     
