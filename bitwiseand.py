N=int(input())
m=[int(i) for i in input().split()][:N]
for i in range(1,len(m)):
  d=m[i] & m[i-1]
  print(d)  
