from random import randint
import matplotlib.pyplot as plt
class stairs():
	currentpos = 0
	histo = []
	def __init__(self):

		pass
	def function(self):
		temp = randint(1,7)
		print(temp)
		if temp == 1 or temp == 2 or temp == 3:
			if self.currentpos == 0:
				pass
			else:
				self.currentpos -= 1
		elif temp == 4 or temp == 5:
			self.currentpos +=1
		else:
			temp = randint(1,7)
			print(temp)
			self.currentpos+=temp
		print("Current position is "+str(self.currentpos))
		self.histo.append(self.currentpos)

strRef = stairs()
inp = input("Enter the number of throws you want")
for iterate in range(int(inp)):
    strRef.function()
print("The person is at "+str(strRef.currentpos)+"th position")
plt.hist(strRef.histo)