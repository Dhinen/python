n=input()
d=0
c=0
for i in n:
  if i.isalpha():
     d=1 
  if i.isnumeric():
    c=1
    print(c)
if d==1 and c==1:
  print("Yes")  
else:
  print("No")    
