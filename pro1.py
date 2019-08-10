a = int(input())
s=[]
for i in range(0,a):
 n=input()
 s.append(n)
d=[]
for i in zip(*s):
  if i.count(i[0])==len(i):
    d.append(i[0])
print(''.join(d))    
