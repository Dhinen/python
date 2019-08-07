n,k=map(int,input().split())
m=[int(i) for i in input().split()]
x=[]
for i in range(n+1):
  if i==0:
    for i in range(0,len(m)):
      for j in range(i+1,len(m)):
       if m[i]==m[i+1] and  m[i] is not x:
         x.append(m[i])
d=0   
for i in range(len(x)):
  d=d+x[i]
if d==0:
  print("no")
elif d<=k and d!=0:
  print("yes")
else:
  print("no")
