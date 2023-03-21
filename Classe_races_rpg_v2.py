from rpg_main_v6 import *

class Humain(Personnage):
    """ Création de la classe Humain """
    def __init__(self, vie, nom, force, endurance, rapidite, intelligence, charisme):
        Personnage.__init__(self, vie, nom, force, endurance, rapidite, intelligence, charisme)
        self.Race = "humain"

class Hobbit(Personnage):
    """ Création de la classe Hobbit """
    def __init__(self, vie, nom, force, endurance, rapidite, intelligence, charisme):
        Personnage.__init__(self, vie, nom, force, endurance, rapidite, intelligence, charisme)
        self.Race = "hobbit"

class Elfe(Personnage):
    """ Création de la classe Elfe """
    def __init__(self, vie, nom, force, endurance, rapidite, intelligence, charisme):
        Personnage.__init__(self, vie, nom, force, endurance, rapidite, intelligence, charisme)
        self.Race = "elfe"

class Nain(Personnage):
    """ Création de la classe Nain """
    def __init__(self, vie, nom, force, endurance, rapidite, intelligence, charisme):
        Personnage.__init__(self, vie, nom,force, endurance, rapidite, intelligence, charisme)
        self.Race = "nain"

class Orque(Personnage):
    """ Création de la classe Nain """
    def __init__(self, vie, nom, force, endurance, rapidite, intelligence, charisme):
        Personnage.__init__(self, vie, nom, force, endurance, rapidite, intelligence, charisme)
        self.Race = "orque"

############ Création des classes Magicien ############

class Magicien:
    """ Création de la classe Magicien """
    def __init__(self, pointsdemagie):
        self.Role = "magicien"
        self.pointsdemagie = pointsdemagie

    def faireMagie (self, autrePersonnage, degatmagique) :
        if degatmagique > 0 :
            autrePersonnage.perd_Vie(degatmagique)
        else :
            autrePersonnage.gain_Vie(abs(degatmagique))


class MagicienHumain(Humain, Magicien):
    def __init__(self, vie, nom, force, endurance, rapidite, intelligence, charisme, pointsdemagie):
        Humain.__init__(self, vie, nom, force, endurance, rapidite, intelligence, charisme)
        Magicien.__init__(self, pointsdemagie)

Sauron = MagicienHumain(40, "Sauron",50, 30, 20, 10, 40, 15)
Bilbon = Hobbit(25, "Bilbon", 11, 12, 8, 29, 17)
Gandalf = MagicienHumain(30, "Gandalf", 15, 8, 10, 35, 25, 20)


