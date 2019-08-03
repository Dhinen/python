n=int(input())
m=[int(i) for i in input().split()]
d=0
for i in range(0,len(m)):
  if m[i]==i:
    print(m[i],end=" ")
