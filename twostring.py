 n,m=input().split()
a=[]
b=[]
s=0
for i in range(0,len(n)):
  a.append(n[i]) 
for j in range(0,len(m)):  
  b.append(m[j]) 
for i in b:
  if i in a:
    s=1
if s==1:
  print("Yes")   
else:
  print("No")   
