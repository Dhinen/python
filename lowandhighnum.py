n=int(input())
m=[int(i) for i in input().split()]
min=m[0]
max=m[0]
for i in range(0,len(m)):
  if m[i]<min:
    mi=m[i]
  elif m[i]>max:
    max=m[i]  
  
print(min,max)    
  
  
