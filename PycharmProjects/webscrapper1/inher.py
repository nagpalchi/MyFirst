class Animal():
    def __init__(self):
        print("Animal Created")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I eat pedigree")
class Mammal():
    def __init__(self):
        print("Mammal Created")
    def who_am_i(self):
        print("I am a mammal")
class Dog(Mammal,Animal):
    def __init__(self):
        print("Dog Created")
    def who_am_i(self):
        print("i am a Dog")
myanimal = Dog()
myanimal.eat()
myanimal.who_am_i()
