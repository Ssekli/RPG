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
import os


class Ecran(Frame) :
    def __init__(self, master = None):
        Frame.__init__(self, master, bg="violet")
        self.master.title("RPG")
        self.master.geometry("900x900")
        self.Map()
        self.CadreAction()
        self.CadreConsole()



    def Map(self) :
        self.cadre_Map = LabelFrame(self.master, text = "Map", bg = "grey", width = 600, height = 700)
        self.cadre_Map.place(x = 0, y = 0)

        img = Image.open("carte.png")
        bgimg = ImageTk.PhotoImage(img)
        panel = Canvas(self.cadre_Map, width = 590, height = 680)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        panel.create_image(10, 10, image = bgimg)


    def CadreAction(self) :
        self.cadre_Action = LabelFrame(self.master, text = "Action", bg = "blue", width = 300, height = 700)
        self.cadre_Action.place(x = 600, y = 0)
        self.bouttonAtk = Button(self.cadre_Action, text = "Attaque", fg = "red", command = self.Map)
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

    def TexteConsole(self) :
        self.texte_cons = Text(self.cadre_Console, width=850, height=190)
        self.texte_cons.grid(row=1, column=1)

'''    def Action(self) :
        '''


monrpg = Tk()
monrpg.title("Matrices")
monrpg["bg"] = "gray"
Ecran(master=monrpg)
monrpg.mainloop()
