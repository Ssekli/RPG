#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     17/02/2023
# Copyright:   (c) Administrateur 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Personnage() :
    def __init__(self, vie, nom, force, endurance, rapidite, intelligence, charisme) :
        self.vie = int(vie)
        self.nom = str(nom)
        self.force = int(force)
        self.endurance = int(endurance)
        self.rapidite = int(rapidite)
        self.intelligence = int(intelligence)
        self.charisme = int(charisme)
        self.Est_mort()

    def Affiche_Caractéristiques(self) :
        '''affiche les stats du personnage'''
        print(f"{self.nom} a une force de {self.force}, une endurance de {self.endurance}, une rapidité de {self.rapidite}, une intelligende de {self.intelligence} et un charisme de {self.charisme}. BG !")

    def Est_mort(self) :
        '''vérifie si le personnage est vivant'''
        if self.vie > 0 :
            self.Est_mort = False #c'est l'objet est mort que est False ou True
        else : #si je veux que ce soit hérité je doit l'appeler et lui donner la
            self.Est_mort = True #valeur True ou False

    def Affiche_etat(self) :
        '''affiche l'état du personnage'''
        if self.Est_mort is False :
            print(f"{self.nom} a  {self.vie} HP")
        else :
            print(f"{self.nom} est mort. RIP")

    def Perd_vie(self, nb_pv_perdu) :
        '''gère la perte de pv du pers'''
        print(f"{self.nom} perd {nb_pv_perdu} HP")
        if nb_pv_perdu >= self.vie :
            print(f"{self.nom} succombe des blessures")
            self.Est_mort = True
        else :
            self.vie -= nb_pv_perdu

    def Gain_vie(self, nb_pv_gagne) :
        '''gère le gain de pv'''
        if self.Est_mort is False :
            self.vie += nb_pv_gagne
            print(f"{self.nom} récupère {nb_pv_gagne} HP.")
        else :
            print(f"{self.nom} ne peut pas être soigné car il est mort.")

    def Soin(self, autre_personnage, Point_de_soin) :
        '''soin d'un perso sur l'autre'''
        if self.Est_mort is False and autre_personnage.Est_mort is False :
            print(f"{self.nom} soigne {autre_personnage.nom} de {Point_de_soin}.")
            autre_personnage.Gain_vie(Point_de_soin)
        elif self.Est_mort is True and autre_personnage.Est_mort is False :
            print(f"{self.nom} ne peut pas soigner {autre_personnage.nom} car {self.nom} est mort")
        elif self.Est_mort is False and autre_personnage.Est_mort is True :
            print(f"{self.nom} ne peut pas soigner {autre_personnage.nom} car {autre_personnage.nom} est mort")
        else :
            print(f"{self.nom} et {autre_personnage.nom} sont morts ! Pas de soin possible")



    def Esquive_attaque(self, autre_personnage) :
        '''On lance l'attaque on veut savoir si ça touche'''
        if self.Est_mort is False and autre_personnage.Est_mort is False :
            if round(self.rapidite * 1.2) > autre_personnage.force :
                self.Esquive_attaque = True
                print(f"{autre_personnage.nom} rate son attaque sur {self.nom}")
            else :
                self.Esquive_attaque = False
                print("{autre_personnage.nom} attaque {self.nom}")
        elif self.Est_mort is True and autre_personnage.Est_mort is False :
            print(f"{self.nom} ne peut pas attaquer {autre_personnage.nom} car {self.nom} est mort")
        elif self.Est_mort is False and autre_personnage.Est_mort is True :
            print(f"{self.nom} ne peut pas attaquer {autre_personnage.nom} car {autre_personnage.nom} est mort")
        else :
            print(f"{self.nom} et {autre_personnage.nom} sont morts ! Pas de d'attaque possible")



def main():
    pass

Bilbon = Personnage(25, "Bilbon", 11, 12, 8, 29, 17)
Gandalf = Personnage(30, "Gandalf", 15, 8, 10, 35, 25)

if __name__ == '__main__':
    main()
