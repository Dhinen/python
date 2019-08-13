n=int(input())
m=[int(i) for i in input().split()]
l=[]
d=1
for i in m:
  if i not in l:
    l.append(i)
for i in range(len(l)-1):
  if l[i]<l[i+1]:
    d+=1 
print(d)      
