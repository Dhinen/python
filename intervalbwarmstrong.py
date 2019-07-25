n,q=map(int,input().split())
for i in range(n,q+1):
	sum=0
	temp=i
	while temp>0:
		d=temp%10
		sum+=d**3
		temp//=10
	if sum==i:
		print(i,end=" ")
