s=int(input())
d=[int(i) for i in input().split()]
n=d[0:s:2]
n1=d[1:s:2]
if sum(n)>=sum(n1):
  print(sum(n))
else:
  print(sum(n1))  
