n=int(input())
m=[int(i) for i in input().split()]
for j in range(0,len(m)):
  for k in  range(j+1,len(m)):
    if m[j]>m[k]:
      t=m[j]
      m[j]=m[k]
      m[k]=t
min=m[0]   
max=m[0]
for i in range(0,len(m)): 
  if m[i]<min:
    min=m[i]
  elif m[i]>max:
    max=m[i]  
  
print(min,max)    
  


  
