class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        print(f"{self.first_name} and {self.pet} go outside for a walk to the park.")


    def feed(self):
        print(f"{self.first_name} leaves {self.pet_food} in {self.pet}'s food tray.")
    
    def bathe(self):
        print(f"{self.first_name} gives {self.pet} a shower.")


class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        pass
    
    def eat(self):
        pass

    def play(self):
        pass

    def noise(self):
        pass

ozzy = Ninja("Osvaldo", "Rivera", "Shih Tzu", "Dog Bites", "Pedigree")

ozzy.walk()
ozzy.feed()
ozzy.bathe()

lulu = Pet("lulu", "Shih Tzu", "roll over", 100, 100)

