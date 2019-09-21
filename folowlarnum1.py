n=int(input())
m=[int(i) for i in input().split()]
s=m[0]
k=0
for i in range(0,len(m)):
  for j in range(i+1,len(m)):
    if m[i]<m[j]:
      
      t=m[i]
      m[i]=m[j] 
      m[j]=t 
      k=1
      
for i in m:
  if k==1:
    print(i,end="") 
  elif s==i:
    print(s)
    break
  
