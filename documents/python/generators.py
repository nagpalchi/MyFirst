# import random
# def squaresgenerator(low,high,count):
# 	for i in range(count):
# 		yield random.randint(low,high)

# a = int(input("Enter lower value"))
# b = int(input("Enter higher value"))
# c = int(input("Number of random output values you want "))
# for num in squaresgenerator(a,b,c):
# 	print(num)

s = 'hello'
def iter():
	for char in str(s):
		yield char
for ch in iter():
	print(ch)