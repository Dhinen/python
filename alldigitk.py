n,m=input().split()
s=0
for i in range(0,(len(n))):
  if int(n[i])<=int(m):
    s=1
  elif int(n[i])>int(m):
    s=2 
if s==1:
  print("yes") 
elif s==2:
  print("no")   
