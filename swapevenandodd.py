n=list(map(str,input()))
for i in range(0,len(n),2):
  temp=n[i]
  n[i]=n[i+1]
  n[i+1]=temp
for i in n:
  print(i,end="") 
