num = int(input("enter the number"))
def fibonaccidm(num):
	if num == 0:
		return 0
	elif num == 1:
		return 1
	else:
		return fibonaccidm(num-1)+ fibonaccidm(num-2)
		
x = fibonaccidm(num)
print(x)