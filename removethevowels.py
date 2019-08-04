m=int(input())
n=input()
vowels="AaEeIiOoUu"
x=[]
y=""
for i in n:
  if i not in vowels:
    x.append(i)
  else:
    x.append(i)  
for i in x:
  y=x[::-1] 
for i in y:
  print(i,end="")  
