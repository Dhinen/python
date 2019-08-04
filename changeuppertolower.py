n=list(map(str,input()))
x=""
for i in n:
  if i.islower()==True:
    x+=i.upper()
  else:
    x+=i.lower() 
print(x)
