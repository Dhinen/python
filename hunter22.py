n=int(input())
m=[int(i) for i in input().split()]
d=1
for i in range(0,len(m)):
  for j in range(len(m)):
    if m[i]!=m[j]:
      d=d*m[j] 
    elif m[n-1] ==m[n-1]:
      d=d
  print(d,end=" ") 
  d=1   
  
