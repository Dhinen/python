n,k=map(int,input().split())
m=[str(i) for i in input().split()]
d=[]
s=0
for i in range(len(m)-k,len(m)):
  if len(m)<k:
     s=1 
  else:
    d.append(m[i])
if s==1:
  d.append(m[i])
d=list(dict.fromkeys(d)) 
for i in range(0,len(m)-k):
  d.append(m[i])     
for i in d:
  print(i,end=" ")  

