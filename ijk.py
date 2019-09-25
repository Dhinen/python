n=int(input())
m=[int(i) for i in input().split()][:n]
s=0
for i in range(0,len(m)):
  for j in range(1,len(m)):
    for k in range(2,len(m)):
      if m[i]>m[j] and m[j]>m[k]:
        s=1
if s==1:
  print("yes")
else:
  print("no")          
