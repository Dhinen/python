  
  
  
  n=int(input())
m=[int(i) for i in input().split()]
x=sorted(m)
x=list(dict.fromkeys(x))
y=x[-1::-1]
for i in y:
  print(i,end="")



n=int(input())
m=[int(i) for i in input().split()]
x=[]
for i in range(0,len(m)):
  for j in range(i+1,len(m)):
    if m[i]<m[j]:
      t=m[i]
      m[i]=m[j] 
      m[j]=t 
for i in m:
  if i not in x:
    x.append(i)
for i in x:
  print(i,end="")

