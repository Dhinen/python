n=int(input())
m=[int(i) for i in input().split()]
l=1
d=1
for i in range(1,n):
  if m[i]>m[i-1]:
    d+=1
  else:
    if l<d:
      l=d  
    d=1   
if l<d:
  l=d   
print(l)   
