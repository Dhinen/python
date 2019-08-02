n,k=map(int,input().split())
m=[str(i) for i in input().split()]
x=sorted(m)
max=x[0]
for i in range(1,len(x)):
  if x[i]>max:
    max=x[i]
print(x[i-(k-1)])  
