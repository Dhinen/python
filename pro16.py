s=int(input())
c=list(map(int,input().split()))
xy=[1]*s
for p in range(s):
    if p==0:
        if c[p]>c[p+1]:
            xy[p]=xy[p]+xy[p+1]
    elif p>0:
        if c[p]>c[p-1]:
            xy[p]=xy[p]+xy[p-1]
print(sum(xy))
