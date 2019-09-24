n=int(input())
m=list([str(i) for i in input().split()])[:n]
b=min(m)
c=max(m)
a=m.index(b)+1
d=m.index(c)+1
print(str(a)+" "+str(d))
