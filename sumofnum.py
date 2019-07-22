# your code goes here
num=int(input())
if num<0:
	print("enter the positive interger")
else:
	sum=0
	while (num>0):
		sum += num
		num -=1
	print(sum)
