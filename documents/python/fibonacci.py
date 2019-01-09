num = int(input("Enter the number of"))
def fibonacci(num):
	i=0
	j=1
	a.append(0)
	a.append(1)
	num-=2
	while num>0:
		temp = i+j
		a.append(temp)
		i=j
		j=temp
		num-=1
	print(a)
fibonacci(num)


