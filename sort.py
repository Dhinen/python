n=input()
x=[int(i) for i in input().split()] 
temp=0
for i in range(0,len(x)):
  for j in range(i+1,len(x)):
    if x[i]>x[j]:
      temp=x[i]
      x[i]=x[j]
      x[j]=temp
  print(x[i],end=" ")      
