n=int(input())
m=[int(i) for i in input().split()][:n]
for i in range(1,len(m),2):
  temp=m[i]
  m[i]=m[i-1]
  m[i-1]=temp
for i in m:
  print(i,end=" ")  
