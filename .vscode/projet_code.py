from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import os
from random import shuffle, choice

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
    fenetre2.config(bg = '#c9ffa6')
    pp = tk.Canvas(fenetre2, width = 1200, height = 300, bg = '#ffa6c9')
    pp.place(x = 0, y = 400)

    def melanger():# #mélanger les cartes
        shuffle(cartes_photos) 

    #Variables du jeu
    y_position=300
    y_position_croupier=200
    overlap_offset=30
    score_joueur=0
    score_croupier=0
    valeur_as=None
    cartes_labels=[]
    cartes_tirees=[]
    boutons_choix_as = []
    resultat=None

    def choix_as():
        def choisir (val):
            nonlocal valeur_as
            valeur_as=val
            compteur()#met à jour le score du joueur
            cacher_boutons_choix_as()
            #permet d'afficher si c'est perdu ou gagné selon le score
        deal.config(state=tk.disabled)#désactive les boutons le temps du choix
        stand.config(state=tk.disabled)
        bouton_1 = tk.Button(fenetre2, text = '1', command=lambda:choisir(1), bg = '#a6c9ff', fg = "black")#définitions des boutons
        bouton_11 = tk.Button(fenetre2, text = '11', command=lambda:choisir(11), bg = '#a6c9ff', fg = "black")
        bouton_1.place(x=600, y=500) #placement des boutons
        bouton_11.place(x=650, y=500)
        boutons_choix_as.append(bouton_1) #créer une liste pour que les boutons disparaissent après
        boutons_choix_as.append(bouton_11)
    
    def cacher_boutons_choix_as():#disparition des boutons
        for boutons in boutons_choix_as:
            boutons.destroy()
    
     #CARTES + leurs labels (sauvez moi) 
    cartes_photos = ["ace_of_clubs.png", "two_of_clubs.png", "three_of_clubs.png", "four_of_clubs.png", "five_of_clubs.png", "six_of_clubs.png", "seven_of_clubs.png", "eight_of_clubs.png", "nine_of_clubs.png", "ten_of_clubs.png", "jack_of_clubs.png", "queen_of_clubs.png", "king_of_clubs.png",
    "ace_of_diamonds.png", "two_of_diamonds.png", "three_of_diamonds.png", "four_of_diamonds.png", "five_of_diamonds.png", "six_of_diamonds.png", "seven_of_diamonds.png", "eight_of_diamonds.png", "nine_of_diamonds.png", "ten_of_diamonds.png", "jack_of_diamonds.png", "queen_of_diamonds.png", "king_of_diamonds.png",
    "ace_of_hearts.png", "two_of_hearts.png", "three_of_hearts.png", "four_of_hearts.png", "five_of_hearts.png", "six_of_hearts.png", "seven_of_hearts.png", "eight_of_hearts.png", "nine_of_hearts.png", "ten_of_hearts.png", "jack_of_hearts.png", "queen_of_hearts.png", "king_of_hearts.png",
    "ace_of_spades.png", "two_of_spades.png", "three_of_spades.png", "four_of_spades.png", "five_of_spades.png", "six_of_spades.png", "seven_of_spades.png", "eight_of_spades.png", "nine_of_spades.png", "ten_of_spades.png", "jack_of_spades.png", "queen_of_spades.png", "king_of_spades.png"]

    melanger() #melange les cartes directement apres que la fenetre s'ouvre IA

    cartes_valeur = {"ace": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, 
                     "eight": 8, "nine": 9, "ten": 10, "jack": 10, "queen": 10, "king": 10}
    
    def get_valeur(carte_filename):
        nom=carte_filename.split("_of_")[0]
        return cartes_valeur[nom]  



    def donner_2_cartes(playeur):
        nonlocal y_position, y_position_croupier, score_joueur, score_croupier
        for i in range(2):
            if cartes_photos:
                carte_tiree=cartes_photos.pop()
                cartes_tirees.append(carte_tiree)
                path=os.path.join(current_dir, carte_tiree)
                image=PhotoImage(file=path).subsample(4,4)
                carte_label=tk.Label(fenetre2, image=image)
                carte_label.image=image
                
                if playeur:
                    carte_label.place(x=600, y=y_position)
                    y_position+=30
                else:
                    carte_label.place(x=400, y=y_position_croupier)
                    y_position_croupier+=30
                    
                cartes_labels.append(carte_label)
                nom_carte=carte_tiree.split('_')[0]
                valeur=get_valeur(carte_tiree)

                if nom_carte=="ace":
                    if playeur:
                        choix_as()
                    else:
                        valeur=11 if score_croupier+11<=21 else 1
                if playeur:
                    score_joueur+=valeur
                    joueur.config(text=f"Joueur({score_joueur})")
                else:
                    score_croupier+=valeur
                    dealer.config(text=f"Croupier({score_croupier})")
            y_position+=30

    def distribution (): #distribuer les cartes
        nonlocal y_position, score_joueur, valeur_as
        if cartes_photos: #vérifie qu'il rest des cartes dans le paquet
            carte_tiree = cartes_photos.pop() #prend la dernièere carte du paquet
            cartes_tirees.append(carte_tiree) #rajoute à la liste des cartes tirées (mémoire)
            path = os.path.join(current_dir, carte_tiree) #affichage des cartes
            image = PhotoImage(file=path).subsample(4,4)
            carte_label = tk.Label(fenetre2, image=image)
            carte_label.image = image
            carte_label.place (x=600, y = y_position)
            cartes_labels.append(carte_label)    
            nom_carte = carte_tiree.split('_')[0]#nom de la carte avec sa vealeur associée
            valeur = get_valeur(carte_tiree)    
            if nom_carte == 'ace': #choix 1 ou 11 + relier au compteur
                choix_as()
            else:
                score_joueur += valeur #ajout valeur de la carte au score
                joueur.config(text = f'Joueur({score_joueur})')
                compteur() #est-ce que le joueur a gagné ou perdu ?
    
    def distribution_croupier():
        nonlocal score_croupier
        while score_croupier<17:
            if cartes_photos:
                carte_tiree=cartes_photos.pop()
                cartes_tirees.append(carte_tiree)
                path=os.path.join(current_dir, carte_tiree)
                image=PhotoImage(file=path).subsample(4,4)
                carte_label=tk.Label(fenetre2, image=image)
                carte_label.image=image
                carte_label.place(x=600, y=y_position)
                cartes_labels.append(carte_label)
                nom_carte=carte_tiree.split('_')[0]
                valeur=get_valeur(carte_tiree)
                
                if nom_carte=="ace":    #prend la valeur la plus benefique pour le croupier
                    valeur=11 if score_croupier+11<=21 else 1

                score_croupier+=valeur
                dealer.config(text=f"Croupier({score_croupier})")

    resultat=tk.Label(fenetre2, fg='green', bg='#c9ffa6', font=("Arial", 20, "bold"))
    resultat.place(x=800, y=200)    #on peut pas la mettre direct dans les iteration car elle chanfe a chaque fois et donc ca bug

    def compteur():   #verifie les scores et les mets a jour durant la partie
        nonlocal score_croupier, score_joueur, resultat

        if score_joueur==21 and len(cartes_tirees)==2:
            blabla1="Black Jack - Bravo vous avez gagné 🥳"
            resultat.config(text=blabla1)           #met a jour la variable resultat
        
        elif (score_croupier<score_joueur and score_joueur==21) or score_croupier>21:
            blabla2="Bravo vous venez de remporter la partie"
            resultat.config(text=blabla2)

        elif score_croupier==21 and len(cartes_tirees)==2:
            blabla3="Bouh, vous avez perdu 🤣"
            resultat.config(text=blabla3)
                              
        elif (17<=score_croupier<=21 and score_joueur<score_croupier) or score_joueur>21:
            blabla3="Bouh, vous avez perdu 🤣"
            resultat.config(text=blabla3)
        
        elif (score_croupier==score_joueur and len(cartes_tirees)==2) or (score_joueur==21 and score_croupier==21):
            blabla4="Egalité, c'est bien joué 👍"
            resultat.config(text=blabla4)

        else:
            resultat.config(text="")

    def deal ():
        distribution()

    def stand():
        # Fonction pour rester
        distribution_croupier()
        compteur()

    def piocher2():
        donner_2_cartes(playeur=True)
        donner_2_cartes(playeur=False)
        compteur()

    #LABELS
    dealer = tk.Label(fenetre2, text ="Croupier", bg = '#c9ffa6', fg = "black",font = ("16"))
    dealer.place(x=150,y=165)

    joueur = tk.Label(fenetre2, text ="Joueur", bg = '#c9ffa6', fg = "black",font = ("16"))
    joueur.place(x=350,y=165)

    #cmpt_d = tk.Label(fenetre2, text ="N", bg = '#c9ffa6', fg = "black",font = ("16"))
    #cmpt_d.place(x=250,y=165)
#
    #cmpt_j = tk.Label(fenetre2, text ="N", bg = '#c9ffa6', fg = "black",font = ("16"))
    #cmpt_j.place(x=450,y=165)

    #BOUTONS
    tirer = tk.Button(fenetre2, text = " CARTE ! ", bg = '#a6c9ff', fg = 'black', command = deal)
    tirer.configure(height=3, width=10)
    tirer.place(x=200,y=300)

    rester = tk.Button(fenetre2, text = " RESTER ", bg = '#a6c9ff', fg = 'black', command= stand)
    rester.configure(height=3, width=10)
    rester.place(x=300,y=300)

    cartes2= tk.Button(fenetre2, text = " 2 cartes ", bg = '#a6c9ff', fg = 'black', command= piocher2)
    cartes2.configure(height=3, width=10)
    cartes2.place(x=300,y=400)

    #dimension cartes: 500 x 726
    current_dir = os.path.dirname(__file__)

   # image_refs=[]
    y_position = 300
    overlap_offset=1
    for i in range (len(cartes_photos)):
        path = os.path.join(current_dir, cartes_photos[i]) 
        image=PhotoImage(file=path)
        image=image.subsample(4,4)
        iage=tk.Label(fenetre2, image=image)
        iage.image=image
        iage.place(x=600, y=y_position)
        y_position+=overlap_offset

    
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
