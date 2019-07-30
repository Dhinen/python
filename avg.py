n=int(input())
m=[int(i) for i in input().split()]
sum=m[0]
for i in range(0,len(m)):
  sum=sum+m[i]
  avg=sum/len(m)
print(round(avg))  
