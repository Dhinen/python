N=input()
d=0
k=0
a=[]
for i in N:
  if i.islower()==True:
    d=i.upper()
    a.append(d)
  elif i.isupper()==True:
    k=i.lower()
    a.append(k)  
print(''.join(a))    
