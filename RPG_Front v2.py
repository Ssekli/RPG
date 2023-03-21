#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     20/03/2023
# Copyright:   (c) Administrateur 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from PIL import ImageTk, Image
from rpg_main_v5 import *
from Classe_races_rpg_v2 import *
from PIL.Image import Resampling
import os


class Ecran(Frame) :
    def __init__(self, master = None):
        Frame.__init__(self, master, bg="violet")
        self.master.title("RPG")
        self.master.geometry("900x900")
        self.Map()
        self.CadreAction()
        self.CadreConsole()

    def add_photo(self, cadre, file_name, w, h, px, py):
        image = Image.open(file_name).resize((w, h), Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        self.cadrePhoto = Label(cadre, image=photo)
        self.cadrePhoto.image = photo
        self.cadrePhoto.place(x=px, y=py)

    def Map(self) :
        self.cadre_Map = LabelFrame(self.master, text = "Map", bg = "grey", width = 600, height = 700)
        self.cadre_Map.place(x = 0, y = 0)
        self.add_photo(self.cadre_Map, f"carte.png", 680, 780, 0, 0)
        self.add_photo(self.cadre_Map, f"Gandalf.png", 50, 50, 50, 550)
        self.add_photo(self.cadre_Map, f"Hobbit.png", 50, 50, 100, 550)

    def CadreAction(self) :
        self.cadre_Action = LabelFrame(self.master, text = "Action", bg = "blue", width = 300, height = 700)
        self.cadre_Action.place(x = 600, y = 0)
        self.bouttonAtk = Button(self.cadre_Action, text = "Attaque", fg = "red", command = self.Attaque_Front)
        self.bouttonAtk.grid_propagate(False)
        self.bouttonAtk.place(x = 135, y = 20)
        self.bouttonSoin = Button(self.cadre_Action, text = "Soin", fg = "red", command = self.Map)
        self.bouttonSoin.grid_propagate(False)
        self.bouttonSoin.place(x = 145, y = 80)
        self.bouttonCarac = Button(self.cadre_Action, text = "Caracteristique", fg = "red", command = self.Map)
        self.bouttonCarac.grid_propagate(False)
        self.bouttonCarac.place(x = 115, y = 140)

    def CadreConsole(self) :
        self.cadre_Console = LabelFrame(self.master, text = "Console", bg = "white", width = 900, height = 200)
        self.cadre_Console.place(x = 0, y = 700)
        self.texte_res = Text(self.cadre_Console, width=900, height=15)
        self.texte_res.grid(row = 0, column = 0)

    def TexteConsole(self) :
        self.texte_cons = Text(self.cadre_Console, width=850, height=190)
        self.texte_cons.grid(row=1, column=1)

    def insertResultat(self, resultat):
        self.texte_res.insert(END, "- " + str(resultat) + "\n")

    def Attaque_Front(self) :
        Sauron.Attaque(Gandalf)
        self.Res_Attaque()

    def Res_Attaque(self) :
        self.insertResultat(msg7)


monrpg = Tk()
monrpg.title("Matrices")
monrpg["bg"] = "gray"
Ecran(master=monrpg)
monrpg.mainloop()
