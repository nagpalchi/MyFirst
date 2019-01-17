class TicTacToe():
    tictac = [['1','2','3'],['4','5','6'],['7','8','9']]
    indexlist,indexofele = 0,0
    def __init__(self):
        pass

    def takeInputX(self):
        print("Enter X in the positions as 1-9")
        self.displayCurrent()
        inp = input()
        indexlist,indexofele = self.findIndex(inp)
        self.tictac[indexlist][indexofele]='X'

    def takeInputO(self):
        print("Enter O in the positions as 1-9")
        self.displayCurrent()
        inp = input()
        indexlist,indexofele = self.findIndex(inp)
        self.tictac[indexlist][indexofele]='O'

# 0,0 0,1 0,2
# 1,0 1,1 1,2
# 1,0 1,1 1,2
    def findIndex(self,x):
        for index_of_single_list, single_list in enumerate(self.tictac):
            if x in single_list:    
                return index_of_single_list,single_list.index(x)

    def checkResult(self):
        crammer = False
        for i in range(3):
            if self.tictac[i][0] == self.tictac[i][1] and self.tictac[i][1] == self.tictac[i][2]:
                crammer = True
                break
            elif self.tictac[0][i] == self.tictac[1][i] and self.tictac[1][i] == self.tictac[2][i]:
                crammer = True
                break
        if self.tictac[0][0] == self.tictac[1][1] and self.tictac[1][1] == self.tictac[2][2]:
            crammer = True
        if self.tictac[1][0] == self.tictac[1][1] and self.tictac[1][1] == self.tictac[0][1]:
            crammer = True
        return crammer

    def displayCurrent(self):
        for semilist in self.tictac:
            print(semilist)
    
    #def takeInput(self):
        

ticTacObj = TicTacToe()
win = False
print("O starts the game")
while(win == False):
    ticTacObj.displayCurrent()
    ticTacObj.takeInputO()
    win = ticTacObj.checkResult()
    if win == True:
        print("Congratulations 'O' Wins.. End of game")
        break
    ticTacObj.takeInputX()
    win = ticTacObj.checkResult()
    if win == True:
        print("Congratulations 'X' Wins.. End of game")
        break
if win == False:
    print("It is a draw .. Bazzinga ")
