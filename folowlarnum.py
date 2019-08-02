n=int(input())
m=[int(i) for i in input().split()]
t=m[0]
for i in range(0,len(m)):
  for j in range(i+1,len(m)):
    if m[i]<m[j]:
      t=m[i]
      m[i]=m[j] 
      m[j]=t
  print(m[i],end="")   
