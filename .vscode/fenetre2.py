import tkinter as tk
from random import *

#FONCTIONS
def distribution():
    #utiliser random
    #slider les cartes
    pass

def deal():
    distribution()
    

def stand():
    #fonct
    pass

#FENETRE 2: JEU
fenetre2 = tk.Tk()
fenetre2.title("Black Jack JEU")
fenetre2.geometry("1200x700")
fenetre2.config(bg = '#007a33')

#LABELS
dealer = tk.Label(fenetre2, text ="Dealer", bg = '#007a33', fg = "black",)
dealer.place(x=150,y=165)

joeur = tk.Label(fenetre2, text ="Joeur", bg = '#007a33', fg = "black",)
joeur.place(x=350,y=165)

cmpt_d = tk.Label(fenetre2, text ="N", bg = '#007a33', fg = "black",)
cmpt_d.place(x=250,y=165)

cmpt_j = tk.Label(fenetre2, text ="N", bg = '#007a33', fg = "black",)
cmpt_j.place(x=450,y=165)

#BOUTONS
deal = tk.Button(fenetre2, text = " DEAL ", bg = '#6cc24a', fg = 'white')
deal.configure(height=3, width=10)
deal.place(x=200,y=300)

stand = tk.Button(fenetre2, text = " STAND ", bg = '#6cc24a', fg = 'white')
stand.configure(height=3, width=10)
stand.place(x=300,y=300)

#mettre fenetre2
fenetre2.mainloop()