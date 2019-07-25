n=int(input())
for i in range(n,(n*5)+1):
	if i==0:
		print("0 0 0 0 0")
	elif i%n==0:
		print(i,end=" ")

		
