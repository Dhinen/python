m=int(input())
n=input()
vowels="AaEeIiOoUu"
x=[]
y=""
for i in n:
  if i not in vowels:
    x.append(i)
    s=1
if s==1:   
 for i in x:
   y=x[::-1] 
 for i in y:
  print(i,end="") 
else:
  y=n[::-1]  
  print(y,end="")  
