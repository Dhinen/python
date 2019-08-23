n=int(input())
s=0
for i in range(2,n):
  if n%i==0 and n!=i:
    s=1
if s==1:
  print("yes") 
else:
  print("no")     
