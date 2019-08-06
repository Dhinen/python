x = int(input())
if x%2==0:
 for i in range(1, x):
    if x % i == 0:
        if i%2==0:
          print(i,end=" ")
        else: 
          print(i,end=" ") 
else:
  for i in range(1, x+1):
    if x % i == 0:
        if i%2==0:
          print(i,end=" ")
        else: 
          print(i,end=" ")  
