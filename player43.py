n,m=input().split()
s=0
for i in m:
  if i not in n:
    s=1
if s!=1:
  print("yes")
else:
  print("no")      

