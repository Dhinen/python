import math
n,m=map(int,input().split())
d=n*m
t=math.sqrt(d)
if (t-math.floor(t)==0):
  print("yes")
else:
  print("no")
