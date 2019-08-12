n=int(input())
m=[int(i) for i in input().split()]
a=int(n//2)
s=m[:a]
d=m[a::]
if sum(s)//len(s)==sum(d)//len(d):
  print("yes")
else:
  print("no")  

