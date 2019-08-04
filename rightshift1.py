n,k=map(int,input().split())
m=[str(i) for i in input().split()]
d=[]
for i in range(len(m)-k,len(m)):
  d.append(m[i])
for i in range(0,len(m)-k):
  d.append(m[i]) 
d=list(dict.fromkeys(d))
for i in d:
  print(i,end=" ")  

