from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
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
    cartes_photos = ["ace_of_clubs.png", "two_of_clubs.png", "three_of_clubs.png", "four_of_clubs.png", "five_of_clubs.png", "six_of_clubs.png", "seven_of_clubs.png", "eight_of_clubs.png", "nine_of_clubs.png", "ten_of_clubs.png", "jack_of_clubs.png", "queen_of_clubs.png", "king_of_clubs.png",
    "ace_of_diamonds.png", "two_of_diamonds.png", "three_of_diamonds.png", "four_of_diamonds.png", "five_of_diamonds.png", "six_of_diamonds.png", "seven_of_diamonds.png", "eight_of_diamonds.png", "nine_of_diamonds.png", "ten_of_diamonds.png", "jack_of_diamonds.png", "queen_of_diamonds.png", "king_of_diamonds.png",
    "ace_of_hearts.png", "two_of_hearts.png", "three_of_hearts.png", "four_of_hearts.png", "five_of_hearts.png", "six_of_hearts.png", "seven_of_hearts.png", "eight_of_hearts.png", "nine_of_hearts.png", "ten_of_hearts.png", "jack_of_hearts.png", "queen_of_hearts.png", "king_of_hearts.png",
    "ace_of_spade.png", "two_of_spade.png", "three_of_spade.png", "four_of_spade.png", "five_of_spade.png", "six_of_spade.png", "seven_of_spade.png", "eight_of_spade.png", "nine_of_spade.png", "ten_of_spade.png", "jack_of_spade.png", "queen_of_spade.png", "king_of_spade.png"]

    cartes = [ace_of_clubs, two_of_clubs, three_of_clubs, four_of_clubs, five_of_clubs, six_of_clubs, seven_of_clubs, eight_of_clubs, nine_of_clubs, ten_of_clubs, jack_of_clubs, queen_of_clubs, king_of_clubs,
                ace_of_diamonds, two_of_diamonds, three_of_diamonds, four_of_diamonds, five_of_diamonds, six_of_diamonds, seven_of_diamonds, eight_of_diamonds, nine_of_diamonds, ten_of_diamonds, jack_of_diamonds, queen_of_diamonds, king_of_diamonds,
                 ace_of_hearts, two_of_hearts, three_of_hearts, four_of_hearts, five_of_hearts, six_of_hearts, seven_of_hearts, eight_of_hearts, nine_of_hearts, ten_of_hearts, jack_of_hearts, queen_of_hearts, king_of_hearts,
                 ace_of_spade, two_of_spade, three_of_spade, four_of_spade, five_of_spade, six_of_spade, seven_of_spade, eight_of_spade, nine_of_spade, ten_of_spade, jack_of_spade, queen_of_spade, king_of_spade]
    #dimension cartes: 500 x 726
    current_dir = os.path.dirname(__file__)

    for i in range (len(cartes)):
        diamant_path=os.path.join(current_dir, "cartes_photos") 
        diam= PhotoImage(file=diamant_path)
        diam=diam.subsample(4,4)
        diama=tk.Label(fenetre2,image=diam)
        diama.image=diam
        diama.place(x=600,y=300) 

    #clubs
    image_path = os.path.join(current_dir, "ace_of_clubs.png")
    ace_of_clubs = image_path.resize((125, 182))
    ac = tk.PhotoImage(file = image_path)
    #ace_of_clubs = tk.resizeImage(ac, 125, 182)
    ace_of_clubs_l = tk.Label(fenetre2, image = ac)
    ace_of_clubs_l.place(x=400,y=200)
    
    #diamonds
    diamant_path=os.path.join(current_dir, "ace_of_diamonds.png")
    diam= PhotoImage(file=diamant_path)
    diam=diam.subsample(4,4)
    diama=tk.Label(fenetre2,image=diam)
    diama.image=diam
    diama.place(x=600,y=300)
    
    
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
