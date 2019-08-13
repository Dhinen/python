n=int(input())
m=[int(i) for i in input().split()]
d=1
a=[]
for i in m:
  d=d*i
for i in m:
  a.append(d//int(i))
print(*a)  
