# your code goes here
n,q=map(int,input().split())
for num in range(n,q+1):
	if num>1:
		for i in range(2,num):
			if num%i ==0:
				break
		else:
			print(num,end=" ")
