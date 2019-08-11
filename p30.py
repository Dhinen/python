s=list(map(str,input().split()))
d=[]
count=0
for i in s:
  if i.isalpha():
   d.append(i)
  else:
    a=int(i)
for i in zip(*d):
  if i.count(i[0])!=len(i):
    count+=1
if count==a:
  print("yes")
else:
  print("no")  
