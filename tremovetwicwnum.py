n=int(input())
m=[int(i) for i in input().split()]
d=[]
s=[]
t=0
for i in range(0,len(m)):
  for j in range(i+1,len(m)):
    if m[i]==m[j] and m[i] not in d :
      d.append(m[i])
for i in m:
  if i not in d:
    s.append(i)    
for i in s:
  print(i,end=" ")
