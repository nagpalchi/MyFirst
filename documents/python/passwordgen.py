import random
import string
x = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
def retpas():
	return random.choice(x)
a=[]
for i in range(1,15):
	a.append(retpas())
b = "".join(a)
print(b)