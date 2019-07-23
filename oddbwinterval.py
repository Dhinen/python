# your code goes here
N,Q=map(int,input().split())
if N==1 and Q<=10000:
	for i in range(N,Q,1):
		if (i%2!=0):
			print(i)
