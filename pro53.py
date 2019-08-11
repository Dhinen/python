import string as d
d=input()
d=d.lower()
a=0
alphabet='abcdefghijklmnopqrstuvwxyz'
for i in alphabet:
  if i not in d:
    a=1
  else:
    a=2  
if a==2:
  print("yes")  
else:
  print("no")  
