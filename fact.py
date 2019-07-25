n=int(input())
fact=1
if n<0:
	print("the factorial doesnot exist for negati=ve num")
elif n==0:
	print("the factorial 0 is 1")
else:
	for i in range(1,n+1):
		fact=fact*i
	print(fact)
	
	
