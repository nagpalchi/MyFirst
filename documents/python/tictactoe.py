class TicTacToe():
	tictac = [['1','2','3'],['4','5','6'],['7','8','9']]

	def __init__(self):

	def takeInputX():
		print("Enter X in the positions as 1-9")
		displayCurrent()
		inp = takeInput()
		tictac.index(inp)='X'

	def takeInputO():
		print("Enter O in the positions as 1-9")
		displayCurrent()
		inp = takeInput()
		tictac.index(inp)='O'

	def checkResult(self):

	def displayCurrent(self):
		for semilist in tictac:
			print(semilist)
	def takeInput(self):
		inp = input()
		return inp
ticTacObj = TicTacToe()

win = False
while(win == False):

