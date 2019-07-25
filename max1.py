# your code goes here
n=int(input())
a=[]
for i in range(0,n):
  temp=int(input())
  a.append(temp)
print(a) 
for j in  range(0,len(a)):
  max=a[0]
  if a[j]>max:
    max=a[j]
    print(max)
    break
