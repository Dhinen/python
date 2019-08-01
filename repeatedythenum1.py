n=input()
m=[str(i) for i in input().split()]
d=0
x=[]  
for i in range(0,len(m)):
  for j in range(i+1,len(m)):
    if m[i]==m[j] and m[i] not in x :
      x.append(m[i])
y=sorted(x)
for k in y:
  print(k,end=" ")
