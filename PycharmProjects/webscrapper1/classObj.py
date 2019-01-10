class Superclass():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def kuttaname(self,teeth= 42):
        return "Woof, Woof, Hi i am {} {} and my teeth are {}".format(self.name,self.surname,teeth)
woofy= Superclass("karan","kalra")
print(woofy.kuttaname())