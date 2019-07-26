n=int(input())
x=[int(i) for i in input().split()]
y=sorted(x)
N=len(x)
if N%2==0:
  d=(y[(N-1)//2]+y[(N+1)//2]/2.0)
  print(d)
else:
  d=y[(N-1)//2]
  print(d)
