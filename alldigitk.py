n,m=input().split()
s=0
for i in range(0,(len(n))):
  if n[i]<=m:
    s=1
  elif n[i]>m:
    s=2 
if s==1:
  print("yes") 
elif s==2:
  print("no")   
