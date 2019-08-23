n,m=input().split()
s=0
for i in n:
  if i in m:
    s=1
if s==1:
  print("yes")
else:
  print("no")      

