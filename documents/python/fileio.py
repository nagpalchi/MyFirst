fileObj = open('test.txt','w')
fileObj.write("Hellow hellow my fillow.\n This is my file.")
fileObj.close()
#fileObj.read('test.txt')
with open ('test.txt','r') as testfile :
	print(testfile.readlines())