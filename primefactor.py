a=int(input())
for i in range(2,a+1):
  if a%i==0:
    for j in range(2,i):
       if i%j==0:
        break
    else:
      print(i,end=" ")    
      
