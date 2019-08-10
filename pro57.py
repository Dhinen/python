a,b=input().split()
d=0
for i in range(0,len(a)):
  for j in range(0,len(b)):
    if a[i]==b[j]:
      d+=1
if d>=2:
  print("yes")
else:
  print("no")  
