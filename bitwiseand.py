N=int(input())
M=[int(i) for i in input().split()][:N]
for i in range(1,len(M)):  
   print(M[i-1] & M[i])
