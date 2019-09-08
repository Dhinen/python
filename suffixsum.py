n=int(input())
m=[int(i) for i in input().split()][:n]
d=0
a=[]
for i in range(len(m),0,-1):
  d=d+m[i-1] 
  a.append(d)
a.reverse()
for i in a:
  print(i,end=" ")
