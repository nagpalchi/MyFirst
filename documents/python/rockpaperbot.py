import random
options = ["rock","paper","scissors"]

while 0>-1:
	print("1. New Game")
	print("2. Exit")
	i = input("Enter your choice\t")
	if(i=='1'):
		print("Choose From rock paper scissors")
		a = input("Your Turn\t")
		b = random.choice(options)
		print("Bot chooses\t"+b)
		if(a==b):
			print("It is a Draw")
			continue
		while(a =="rock"):
			if b =="scissors":
				print("Congratulations.. !!  Player 1 Wins !!")
				break
			if b =="paper":
				print("You loose. Bot Wins.")
				break
		while(a =="scissors"):
			if b =="rock":
				print("You loose. Bot Wins.")
				break
			if b =="paper":
				print("Congratulations.. !!  Player 1 wins")
				break
		while(a =="paper"):
			if b =="scissors":
				print("You loose. Bot Wins.")
				break
			if b =="rock":
				print("Congratulations.. !!  Player 1 wins")
				break
		while(a!="rock" and a!="scissors" and a!="paper"):
			print("Wrong choice")
			break
		while(b!="rock" and b!="scissors" and b!="paper"):
			print("Wrong choice")
			break
	else:
		print("Game Over.. Have a nice day.!")
		break

