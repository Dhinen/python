n=[int(i) for i in input().split()]
t=n[0]
for i in range(0,len(n)):
  for j in range(i+1,len(n)):
    if n[i]>n[j]:
      t=n[i]
      n[i]=n[j]
      n[j]=t
print(n[i])    
