n,m=input().split()
s=0
b=[]
a=[]
for j in range(0,int(m)+1):
  b.append(j)          
for i in range(0,len(n)):
  a.append(int(n[i]))
for i in a:
  if i in b:
    s=1
  elif i not in b:
    s=2       
if s==1:
  print("yes") 
elif s==2:
  print("no") 
