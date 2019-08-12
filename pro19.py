n=int(input())
a=[]
s=[int(i) for i in input().split()]
u=[int(i) for i in input().split()]
v=[int(i) for i in input().split()]
for i in s:
  a.append(i)
for i in u:
  a.append(i)
for i in v:
  a.append(i) 
b=sorted(a)   
print(b)  
