n=int(input())
m=[int(i) for i in input().split()]
a=[]
for i in m:
  s=bin(i)
  a.append(s)
d=sorted(a)  
d.reverse()
for j in d:
  print(int(j,2))
