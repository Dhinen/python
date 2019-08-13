n=int(input())
m=[str(i) for i in input().split()]
d=m[::-1]
print(*d,sep="->")
