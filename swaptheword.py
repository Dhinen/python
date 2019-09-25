n=input()
a=[]
p=1
for i in range(0,len(n)):
  if i%2==0:
    a.append(n[i+p])
  else:
    a.append(n[i-p])  
print(''.join(a))    
