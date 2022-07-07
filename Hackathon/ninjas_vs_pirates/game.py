from classes.ninja import Ninja
from classes.pirate import Pirate
import random
michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")



while (michelangelo.health > 0 and jack_sparrow.health > 0):
    randNumM = random.randint(1,5)
    if (randNumM == 1):
        michelangelo.punch(jack_sparrow)
    elif (randNumM == 2):
        michelangelo.attack3(jack_sparrow)
    else:
        michelangelo.attack(jack_sparrow)

    jack_sparrow.show_stats()

    randNumJ = random.randint(1,2)
    if (randNumJ == 1):
        jack_sparrow.attack(michelangelo)
    elif (randNumJ == 2):
        jack_sparrow.attack(michelangelo)

    michelangelo.show_stats()

if (jack_sparrow.health <= 0):
    print("Michelangelo wins")
elif (michelangelo.health <= 0):
    print("Jack Sparrow Wins")
