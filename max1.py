# your code goes here
n=int(input())
a=[]
for i in range(0,n):
  temp=int(input())
  a.append(temp)
print(a) 
max=a[0]
for j in  range(0,len(a)):
  if max<a[j]:
    max=a[j]
print(max)
  
