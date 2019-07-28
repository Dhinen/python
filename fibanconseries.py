n=int(input())
m=0
d=1
while n>0:
  print(m,end="")
  N=m+d
  m=d
  d=N
  n-=1
