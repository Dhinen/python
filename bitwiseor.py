n=int(input())
m=[int(i) for i in input().split()][:n]
for i in range(1,len(m)):
  print(m[i-1] | m[i],end=" ")
