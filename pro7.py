n=int(input())
a=[]
if n%2==0:
  print("0")
else:  
  for i in range(n+1):  
     if n!=i**2 and i**2<n:
       i=n-i**2
       a.append(i)
  print(min(a))      
