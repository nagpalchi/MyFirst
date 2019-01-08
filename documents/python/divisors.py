import math
a = []
def divisors(x):
	x = int(x)
	for i in range(1,int(math.sqrt(x))+1):
		if(x%i==0):
			if x/i == i:
				a.append(i)
			else:
				a.append(i)
				a.append(int (x/i))
	return 0
divisors(16)
print(a) 			
