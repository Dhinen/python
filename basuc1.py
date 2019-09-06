n,k=input().split()
m=[str(i) for i in input().split()]
for i in m :
   if i in k:
     print("yes")
     break
if i not in k:
   print("no")
