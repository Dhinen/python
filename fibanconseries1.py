n=int(input())
m=0
d=1
while n>0:
  N=m+d
  m=d
  d=N
  print(m,end=" ")
  n-=1
