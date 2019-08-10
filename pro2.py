from itertools import combinations
a,b=input().split()
s=int(b)
k=[]
d=combinations(a,len(a)-s)
d=list(d)
for i in d:
  k.append(i)
k=sorted(k)
print(''.join(k[0]))
