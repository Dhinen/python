n=int(input())
a=[]
for i in range(n):
 s=list(map(int,input().split()))
 for j in s:
  a.append(j)
b=sorted(a)  
for i in b:
  print(i,end=" ")
