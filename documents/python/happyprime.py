from math import sqrt
# primeObj = open('primennum.txt','w')
# happyObj = open('happynum.txt','w')
i=2
j=2
primeList = set()
while i<1000:
	count =0
	for a in range(1,int(sqrt(i))+1):
		if i%a==0:
			count+=1

	if count ==1:
	#	primeObj.write(str(i)+"  ")
		primeList.add(i)
	i+=1
#print(primeList)
def returnsumofSquares(tempList):
	count = 0
	for numbers in tempList:
		count += int(numbers)**2
	return count
with open('primenum.txt','w') as primenum:
	primenum.write(str(primeList))

restricted = [4, 16, 37, 58, 89, 145, 42, 20]
#primeObj.close()
#happyObj.write(str(1)+"  ")
happyList = set('1')
while j<1000:
	tempList = list(str(j))
	sumOfHappy = 0
	while sumOfHappy!=1:
		sumOfHappy = returnsumofSquares(tempList)
		if sumOfHappy in restricted:
			break
		else:
			tempList = list(str(sumOfHappy))
			sumOfHappy = returnsumofSquares(tempList)

#	happyObj.write(str(j)+"  ")
	if sumOfHappy ==1:
		happyList.add(j)
		j+=1
	else:
		j+=1 
		continue
#happyObj.close()
#print(happyList)
comboList = set()
with open('happynum.txt','w') as happynum:
	happynum.write(str(happyList))
for inp in primeList:
	if inp in happyList:
		comboList.add(inp)

with open('primehappy.txt','w') as primeHappy:
	primeHappy.write(str(comboList))
with open('primehappy.txt','r') as primeHappy:
	print(primeHappy.read())

#4, 16, 37, 58, 89, 145, 42, 20
#TIC TAC TOE
#Happy Numbers
#guess the number( using class)
