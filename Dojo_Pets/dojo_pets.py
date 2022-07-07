class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def ninja_info(self):
        print(f"My first name is {self.first_name}")
        print(f"My last name is {self.last_name}")
        print(f"My favorite treat to give to my pet is {self.treats}")
        print(f"I feed my pets {self.pet_food}")
        print(f"My pet is {self.pet}")
        return self

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

class Pet:
    def __init__(self, name, kind, tricks, health, energy):
        self.name = name
        self.kind = kind
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def pet_info(self):
        print(f"My name is {self.name}")
        print(f"I am a {self.kind}")
        print(f"I know this trick: {self.tricks}")
        print(f"My health is {self.health}")
        print(f"I have this much energy {self.energy}")
    
    def sleep(self):
        self.energy += 100
        print(f"{self.name} is sleeping")
        return self

    def eat(self):
        self.health += 50
        self.energy += 50
        print(f"{self.name} ate the food and gained health and energy")
        return self

    def play(self):
        self.energy -= 50
        print(f"{self.name} played hard and is tired")
        return self

    def noise(self):
        self.health -= 25
        print(f"{self.name} says get me outta here")
        return self

cheese = Pet("cheese", "dog", "give paw", 100, 100)
patrick = Ninja("Patrick", "Purington", "milkbone", "purina", cheese)
# cheese.pet_info()
# patrick.ninja_info()
patrick.walk()
patrick.bathe()
patrick.feed()