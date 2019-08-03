n=int(input())
fact=1
if n<0:
	print("the factorial doesnot exist for negative num")
elif n==0 or n==1:
	print("1")
else:
	for i in range(2,n+1):
		fact=fact*i
	print(fact)
	
	
