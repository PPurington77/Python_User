class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        return self

    def punch(self, pirate):
        pirate.health -= self.strength * 2
        return self

    def attack3 (self, pirate):
        pirate.health -= self.strength * 3
        return self

