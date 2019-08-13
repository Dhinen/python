n,k=map(int,input().split())
m=[int(i) for i in input().split()]
d=0
for i in range(0,len(m)):
  for j in range(i+1,len(m)):
    if m[i]+m[j]==k:
      d=1
if d==1:
  print("YES")
else:
  print("NO")        

