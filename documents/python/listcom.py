c=[]
a=[1,12,23,34,45,56,67,78,89]
b=[3,12,45,43,54,65,67,89,87]
for x in a:
	if x in b:
		c.append(x)

print(c)