n=input()
x=[int(i) for i in n.split()]
min=x[0]
for j in range(1,len(x)):
  if x[j]<min:
    min=x[j]
print(min)
