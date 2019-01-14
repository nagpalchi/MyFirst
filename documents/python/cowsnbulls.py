import random
cows=0
bulls = 0
bot=[]
user=[]
def findit(bot,user):
	cow = 0
	bull=0
	for x in bot:
		if x in user:
			if bot.index(x)==user.index(x):
				cow+=1
			else:
				bull+=1
	return cow,bull

while 0>-1:
	print("1. New Game \n 2. Exit ")
	inp = input("Enter your choice\t")
	if(inp=='1'):
		bot = str(random.randrange(1000,9999))
		bot = [int(x) for x in str(bot)]
		ch = 'y'
		while(ch=='y'):
			user = input("Enter a 4 digit number")
			user = [int(y) for y in str(user)]
			print(bot)
			cows,bulls = findit(bot,user)
			print("Cows are "+str(cows) + " Bulls are "+str(bulls))
			if cows ==4 and bulls ==0: 
				print("Congratulations, you win the game. !!! Hurrray ... !!!    ")
				break
			print("continue?")
			ch = input("y/n")
		break	
	else:
		print("Game Over. Bye..!! ")
		break
		