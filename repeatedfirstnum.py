n=input()
m=[str(i) for i in input().split()]
d=0
x=[]  
for i in range(0,len(m)):
  for j in range(i+1,len(m)):
    if m[i]==m[j] and m[i] not in x :
      x.append(m[i])
      d=1
for k in x:
  print(k,end=" ")
  break
if d!=1:
  print("unique")  




 
