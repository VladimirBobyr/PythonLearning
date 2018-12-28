# ----------------------- Hero Class ------------------------------------------
class Hero():
    """Class to create Hero for Game"""
    def __init__(self, name, level, race):
        """Initiation our here"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
        self.loc_x = 0
        self.loc_y = 0

    def show_hero(self):
        """ Print all parameters of this hero """
        description = ("Name is: " + self.name + " Level: " + str(self.level) + " Race is: " + self.race + " Health is: " + str(self.health)).title()
        print(description)

    def level_up(self):
        """ Upgrade level of here """
        self.level = self.level + 1

    def move(self):
        """ Start moving of hero """
        self.loc_x = self.loc_x + 1
        self.loc_y = self.loc_y + 1
        print("Position: " + str(self.loc_x) + " " + str(self.loc_y))

    def set_health(self, health):
        self.health = health
        print(self.health)


# ----------------------- SuperHero Class ---------------------------------------
class SuperHero(Hero):
    """ Class to create SuperHero """
    def __init__(self, name, level, race, magiclevel):
        """ Initiate SuperHero """
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.__magic = 100

    def make_magic(self):
        """ Use magic """
        self.__magic -= 10

    def show_hero(self):
        """ Pring all parameters of this SuperHero """
        description = ("Name is: " + self.name + " Level: " + str(self.level) + " Race is: " + self.race + " Health is: " + str(self.health) +
                       " Magic is: " + str(self.__magic)).title()
        print(description)

