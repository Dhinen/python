n=int(input())
m=list([str(i) for i in input().split()])[:n]
b=min(m)
c=max(m)
a=m.index(b)
d=m.index(c)
print(str(a)+" "+str(d))
