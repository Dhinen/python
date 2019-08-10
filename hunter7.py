n=int(input())
s=list(map(int,input().split()))
d=0
for i in range(0,len(s)):
    if i%2==0 and s[i]%2==0  or i%2!=0 and s[i]%2!=0:
        continue
    else:
      print(s[i],end=" ")    
