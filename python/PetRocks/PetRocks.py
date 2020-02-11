class PetRock:
    def __init__(self, name):
        self.name = name
        print("I've been created, my name is", self.name, ".")

    def roll(self):
        print(self.name, "is rolling.")

sully = PetRock('Sully')
sully.roll()

boo = PetRock('Boo')
boo.roll()

