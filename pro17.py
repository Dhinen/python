x,y=map(int,input().split())
j=list(map(int,input().split()))[:x]
count=0
for k in range(0,len(j)-1):
  for sec in range(k+1,len(j)-1):
    if(y[k]+y[sec]==y):
      count+=1  
if count==1:
  print("yes")
else:
  print("no")
