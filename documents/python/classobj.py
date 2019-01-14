class NameOfClass():
	firstName = ""
	lastName = ""
	def __init__(self,firstName,lastName):
		self.firstName = firstName
		self.lastName = lastName
	def toString(self):
		return "Hi {} {} . Welcome to Chirag's PC.".format(self.firstName,self.lastName)

obj1 = NameOfClass("Virat","Kohli")
print(obj1.toString())
print(type(obj1))
