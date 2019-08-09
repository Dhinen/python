x,j=map(int,input().split())
y=list(map(int,input().split()))[:x]
count=0
for k in range(0,len(y)-1):
  for sec in range(k+1,len(y)-1):
    if(y[k]+y[sec]==j):
      count+=1  
if count==1:
  print("yes")
else:
  print("no")
