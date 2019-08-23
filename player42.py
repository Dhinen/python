n=input()
d=list(map(int,input().split()))
s=0
for i in range(1,len(d)):
  if d[i]<d[i-1]:
    s=1 
    break   
if s==1:
  print("no")   
else:
  print("yes")    
