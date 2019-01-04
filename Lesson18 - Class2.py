import mydodule
import hero

from mydodule import *
from hero import *

myhero1 = Hero("Vurdalak", 4, "Orc")
mysupero1 = SuperHero("Moisey", 7, "Human", 5)

myhero1.show_hero()
mysupero1.show_hero()
mysupero1.make_magic()
print("---------------------------")
mysupero1.show_hero()

#mysupero1.magic = 70  # don't use it - use __ in variable it doesn't allow us to change it
mysupero1.show_hero()
myhero1.show_hero()
print(mysupero1.level)


