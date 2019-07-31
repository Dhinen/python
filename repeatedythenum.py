n=input()
m=[int(i) for i in input().split()]
d=0
x=sorted(m)   
for i in range(0,len(x)):
  for j in range(i+1,len(x)):
    if x[i]==x[j]:
      print(x[i],end=" ")
      d=0
    else:
       d=1
if d==1:
  print("unique")      
