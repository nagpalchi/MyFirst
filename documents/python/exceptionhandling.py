try:
	a = int(input("Enter a number"))
	weld = 100/a
	print(a)
	print("Whatever.. if an error occurs i run")
except ArithmeticError:
	print("sorry 0 is not allowed")
else:
	print("This is else block")
finally:
	print("This si finally block")
