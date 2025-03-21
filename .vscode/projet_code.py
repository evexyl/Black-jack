import tkinter as tk
from tkinter import PhotoImage
import os
from random import *

#Fenetre règle:
#config de fenetre + canvas
#callback fenetre regle
def on_open_fenetre():
    fentre_regle= tk.Toplevel()
    fentre_regle.title("Black Jack REGLE")
    fentre_regle.config(bg="black")
    fentre_regle.geometry("650x800")

#Label
    #rule=tk.Label(fentre_regle,fg="green", font=('Arial',14),wraplength=600,
    #        text="But du jeu : Atteindre un total de points le plus proche de 21 sans dépasser "
    #          "ce nombre.\n"
    #          
    #          "Valeurs des cartes : les cartes de 2 à 10 valent leur valeur.Les "
    #          "figures (Roi, Dame, Valet) valent 10 points. L'As vaut 1 ou 11 points (selon "
    #          "ce qui vous avantage).\n "
#
    #          "Déroulement :Chaque joueur reçoit 2 cartes face visible, "
    #          "et le croupier a une carte visible et une face cachée. Vous pouvez demander "
    #          "d’autres cartes (tirer), ou garder votre total actuel (rester). Si vos cartes"
    #          " dépassent 21, vous perdez (on appelle cela 'sauter'). \n "
#
    #          "Gagner : Vous gagnez si votre total est égal à 21 ou le plus proche possible sans dépasser cette valeur. "
    #          "Un Blackjack (21 avec deux cartes seulement, As + 10 ou figure) est la meilleure main possible.")  #\n permet le retour a la ligne
    current_dir = os.path.dirname(__file__)
    blabla_path = os.path.join(current_dir, "regle python.txt")
    with open(blabla_path, "r", encoding="utf-8") as file:
        blablacar=file.read()
    rule=tk.Text(fentre_regle, wrap=tk.WORD,fg="green", bg="Black", font=("Arial",14), borderwidth=0, highlightthickness=0)
    rule.insert(tk.END, blablacar)
    rule.config(state=tk.DISABLED)

    rule.pack()

#############################################################################################################################
#FENETRE 2
#FONCTIONS
def on_open_fenetre2():
    fenetre2 = tk.Toplevel()
    fenetre2.title("Black Jack JEU")
    fenetre2.geometry("1200x700")
    fenetre2.config(bg = '#164e0a')

    def distribution():
        #utiliser random
        #slider les cartes
        pass

    def deal():
        distribution()
        

    def stand():
        #fonct
        pass

    #LABELS
    dealer = tk.Label(fenetre2, text ="Croupier", bg = '#164e0a', fg = "white",)
    dealer.place(x=150,y=165)

    joueur = tk.Label(fenetre2, text ="Joueur", bg = '#164e0a', fg = "white",)
    joueur.place(x=350,y=165)

    cmpt_d = tk.Label(fenetre2, text ="N", bg = '#164e0a', fg = "white",)
    cmpt_d.place(x=250,y=165)

    cmpt_j = tk.Label(fenetre2, text ="N", bg = '#164e0a', fg = "white",)
    cmpt_j.place(x=450,y=165)

    #BOUTONS
    deal = tk.Button(fenetre2, text = " CARTE ! ", bg = '#7c0a0a', fg = 'white')
    deal.configure(height=3, width=10)
    deal.place(x=200,y=300)

    stand = tk.Button(fenetre2, text = " RESTER ", bg = '#7c0a0a', fg = 'white')
    stand.configure(height=3, width=10)
    stand.place(x=300,y=300)

    #CARTES + leurs labels (sauvez moi) 
    #dimension cartes: 500 x 726
    current_dir = os.path.dirname(__file__)
    #clubs
    image_path = os.path.join(current_dir, "ace_of_clubs.png")
    ac = tk.PhotoImage(file = image_path)
    #ace_of_clubs = tk.resizeImage(ac, 125, 182)
    ace_of_clubs_l = tk.Label(fenetre2, image = ac)
    ace_of_clubs_l.place(x=600,y=600)
    #ace_of_clubs = tk.resizeImage(ac, 125, 182)
    #diamonds
    #heart
    #spades

##############################################################################################################################
#FENETRE 1:
#config de fenetre + canvas
fenetre1 = tk.Tk()
fenetre1.title("Black Jack MENU")
fenetre1.geometry("650x800")
#fenetre1.configure(bg='#006400')


#Label
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "casino.png")
image = PhotoImage(file=image_path)

image_bj = tk.Label(fenetre1, image=image)
image_bj.image = image
image_bj.pack()

bj = tk.Label(fenetre1, text="Black Jack",bg = "Black", fg = "white", font=("Impact",54))
bj.place(x=150,y=165)

#Bouttons
start = tk.Button(fenetre1, text = " START ", bg = 'Black', fg = 'white', command = on_open_fenetre2)
start.configure(height=5, width=30)
start.place(x=200,y=350)

regles = tk.Button(fenetre1,text = " REGLES ",bg = 'White',fg = 'Black', command= on_open_fenetre)
regles.configure(height=5, width=30)
regles.place(x=200,y=450)

bouton_quit = tk.Button(fenetre1,text = " QUIT ",bg = '#ff0000',command = fenetre1.destroy)
bouton_quit.configure(height=5, width=30)
bouton_quit.place(x=200,y=550)

#mets fenetre1
fenetre1.mainloop()
