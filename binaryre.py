n=int(input())
k=bin(n)
s=0
for i in k:
  if i=='1':
    s=s+1
print(s)      
