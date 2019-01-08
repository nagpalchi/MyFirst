name = input("Enter the word ")
length = len(name)
flag = True
for i in range(0,int(length/2)):
	if name[i]==name[length-1-i]:
		flag = True
	else: 
		flag = False
if flag == True :
	print("Is a palindrome")
else:
	print("Is not a palindrome")
