import string as d
d=input()
d=d.lower()
a=0
alphabet='abcdefghijklmnopqrstuvwxyz'
for i in alphabet:
  if i not in d:
    a=1
if a==1:
  print("no")
else:
  print("yes")      
