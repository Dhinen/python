n,m,k=map(int,input().split())
if (n+m<=k)or(m+k<=n)or(k+m<=m):
  print("no")
else:
  print("yes")
