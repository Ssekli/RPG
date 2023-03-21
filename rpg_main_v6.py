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
        message = []

    def Affiche_Caractéristiques(self) :
        '''affiche les stats du personnage'''
        global message
        message.append(f"{self.nom} a une force de {self.force}, une endurance de {self.endurance}, une rapidité de {self.rapidite}, une intelligende de {self.intelligence} et un charisme de {self.charisme}. BG !")
        message.append(f"{self.nom} est de race : {self.Race} et de classe {self.Role}")
        if self.Role == magicien :
            message.append(f"son nb de pt de magie est : {self.pointdemagie}")

        print(msg1)
        print(msg4)
        print(msg5)


    def Est_mort(self) :
        '''vérifie si le personnage est vivant'''
        if self.vie > 0 :
            self.mort = False #c'est l'objet est mort que est False ou True
        else : #si je veux que ce soit hérité je doit l'appeler et lui donner la
            self.mort = True #valeur True ou False

    def Affiche_etat(self) :
        '''affiche l'état du personnage'''
        self.Est_mort()
        if self.mort == False :
            message.append(f"{self.nom} a  {self.vie} HP")
        else :
            message.append(f"{self.nom} est mort. RIP")

    def Perd_vie(self, nb_pv_perdu) :
        '''gère la perte de pv du pers'''
        self.Est_mort()
        if nb_pv_perdu >= self.vie :
            message.append(f"{self.nom} succombe des blessures")
            self.mort = True
        else :
            self.vie -= nb_pv_perdu
            message.append(f"{self.nom} perd {nb_pv_perdu} HP")

    def Gain_vie(self, nb_pv_gagne) :
        '''gère le gain de pv'''
        self.Est_mort()
        if self.mort == False :
            self.vie += nb_pv_gagne
            message.append(f"{self.nom} récupère {nb_pv_gagne} HP.")
        else :
            message.append(f"{self.nom} ne peut pas être soigné car il est mort.")

    def Soin(self, autre_personnage, Point_de_soin) :
        '''soin d'un perso sur l'autre'''
        self.Est_mort()
        autre_personnage.Est_mort()
        if self.mort == False and autre_personnage.mort == False :
            message.append(f"{self.nom} soigne {autre_personnage.nom} de {Point_de_soin}.")
            autre_personnage.Gain_vie(Point_de_soin)
        elif self.mort == True and autre_personnage.mort == False :
            message.append(f"{self.nom} ne peut pas soigner {autre_personnage.nom} car {self.nom} est mort")
        elif self.mort == False and autre_personnage.mort == True :
            message.append("{self.nom} ne peut pas soigner {autre_personnage.nom} car {autre_personnage.nom} est mort")
        else :
            message.append(f"{self.nom} et {autre_personnage.nom} sont morts ! Pas de soin possible")

    def Esquive_attaque(self, autre_personnage) :
        '''On lance l'attaque on veut savoir si ça touche'''
        if round(self.rapidite * 1.2) > autre_personnage.force :
            self.esquive = True
            message.append(f"{autre_personnage.nom} rate son attaque sur {self.nom}")
            print(msg7)
        else :
            self.esquive = False
            message.append(f"{autre_personnage.nom} attaque {self.nom}")
            print(msg7)

    def Attaque(self, autre_personnage) :
        ''' On lance l'attaque, si les personnages sont en vie'''
        self.Est_mort()
        autre_personnage.Est_mort()
        if self.mort == False and autre_personnage.mort == False :
            autre_personnage.Esquive_attaque(self)
            if autre_personnage.esquive == False :
                Degat = round((self.force) * 0.6)
                autre_personnage.vie -= Degat
        else :
            message.append("Attaque impossible un des deux personnages est mort.")

# elif en dernier car else ne reconnais pas le nombre de proba de combi ds Est mort

    def se_deplace(self, points_de_deplacement) :
        pass

