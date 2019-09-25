import math
n,m,o=map(int,input().split())
a=n**2+m**2
b=m**2+o**2
c=n**2+o**2
if(o==math.sqrt(a))or(n==math.sqrt(b))or(m==math.sqrt(c)):
  print("yes")
else:
  print("no")  
