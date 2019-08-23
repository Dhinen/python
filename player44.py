n,k=input().split()
k=int(k)
a=[]
d=[]
for i in range(k,len(n)):
  a.append(n[i])
for i in range(0,len(n)):
  if  n[i] not in a:
    a.append(n[i])
print(''.join (a))    
