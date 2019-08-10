n=int(input())
s=list(map(int,input().split()))
d=0
if n%2!=0:
  for i in range(0,len(s)):
    if i%2==0 and s[i]%2==0:
       break
    else:
      s[i]=s[i]
    print(s[i],end=" ")  
else:
    for i in range(0,len(s)):
      if i%2!=0 and s[i]%2==0:
       print(s[i],end=" ")

