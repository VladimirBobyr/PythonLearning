
class Hero():
    """Class to create Hero for Game"""
    def __init__(self, name, level, race):
        """Initiation our here"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """ Pring all parameters of this here """
        description = "Name is: " + name + " Level: " + level + " Race is: " + race + " Health is: "