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
    fenetre2.config(bg = '#a6ffb0')

    def distribution():
        if cartes_photos: 
            carte_tiree = cartes_photos.pop()  
            path = os.path.join(current_dir, carte_tiree) 
            image = PhotoImage(file=path).subsample(4, 4)  
            carte_label = tk.Label(fenetre2, image=image) 
            carte_label.image = image  
            carte_label.place(x=600, y=y_position)  
            compteur()  

            target_x, target_y = 400, 600
            def move(speed = 15): #ne marche pas encore dont push
                x = carte_label.winfo_x()
                y = carte_label.winfo_y()

                dx = target_x - x
                dy = target_y - y
                distance = (dx**2 + dy**2)**0.5

                if distance < speed:
                    carte_label.place(x=target_x, y=target_y)  # Snap to position
                else:
                    step_x = dx / distance * speed
                    step_y = dy / distance * speed
                    carte_label.place(x=x + step_x, y=y + step_y)
                    carte_label.after(16, move)  

            carte_label.after(50, move)

    def deal():
        distribution()  # Distribution appelée depuis le bouton

    def stand():
        # Fonction pour rester
        pass

    def melanger():
        global cartes_photos
        shuffle(cartes_photos) 


    def compteur():
        global cmpt
        global joueur_score
        global croupier_score

        carte_joueur 

        joueur_score+=carte_joueur
        croupier_score+=carte_croupier

        if joueur_score<=21 and joueur_score>croupier_score:
            return "Joueur vainqueur"
        elif joueur_score==croupier_score:
            return "Egalité"
        elif croupier_score<=21 and joueur_score<croupier_score:
            return "Joueur loseur"
    
    #LABELS
    dealer = tk.Label(fenetre2, text ="Croupier", bg = '#a6ffb0', fg = "black",)
    dealer.place(x=150,y=165)

    joueur = tk.Label(fenetre2, text ="Joueur", bg = '#a6ffb0', fg = "black",)
    joueur.place(x=350,y=165)

    cmpt_d = tk.Label(fenetre2, text ="N", bg = '#a6ffb0', fg = "black",)
    cmpt_d.place(x=250,y=165)

    cmpt_j = tk.Label(fenetre2, text ="N", bg = '#a6ffb0', fg = "black",)
    cmpt_j.place(x=450,y=165)

    #BOUTONS
    deal = tk.Button(fenetre2, text = " CARTE ! ", bg = '#a6f6ff', fg = 'black', command = distribution)
    deal.configure(height=3, width=10)
    deal.place(x=200,y=300)

    stand = tk.Button(fenetre2, text = " RESTER ", bg = '#a6f6ff', fg = 'black', command= stand)
    stand.configure(height=3, width=10)
    stand.place(x=300,y=300)

    #CANVAS
    pp = tk.Canvas(fenetre2, width = 1200, height = 300, bg = '#ffa6c9')
    pp.place(x = 0, y = 400)

   
   # Générer un dictionnaire associant les noms des cartes à leurs fichiers image
    cartes_def= {carte.replace(".png", ""): carte for carte in cartes_photos}

    #CARTES + leurs labels (sauvez moi) 
    cartes_photos = ["ace_of_clubs.png", "two_of_clubs.png", "three_of_clubs.png", "four_of_clubs.png", "five_of_clubs.png", "six_of_clubs.png", "seven_of_clubs.png", "eight_of_clubs.png", "nine_of_clubs.png", "ten_of_clubs.png", "jack_of_clubs.png", "queen_of_clubs.png", "king_of_clubs.png",
    "ace_of_diamonds.png", "two_of_diamonds.png", "three_of_diamonds.png", "four_of_diamonds.png", "five_of_diamonds.png", "six_of_diamonds.png", "seven_of_diamonds.png", "eight_of_diamonds.png", "nine_of_diamonds.png", "ten_of_diamonds.png", "jack_of_diamonds.png", "queen_of_diamonds.png", "king_of_diamonds.png",
    "ace_of_hearts.png", "two_of_hearts.png", "three_of_hearts.png", "four_of_hearts.png", "five_of_hearts.png", "six_of_hearts.png", "seven_of_hearts.png", "eight_of_hearts.png", "nine_of_hearts.png", "ten_of_hearts.png", "jack_of_hearts.png", "queen_of_hearts.png", "king_of_hearts.png",
    "ace_of_spades.png", "two_of_spades.png", "three_of_spades.png", "four_of_spades.png", "five_of_spades.png", "six_of_spades.png", "seven_of_spades.png", "eight_of_spades.png", "nine_of_spades.png", "ten_of_spades.png", "jack_of_spades.png", "queen_of_spades.png", "king_of_spades.png"]

    

    #dimension cartes: 500 x 726
    current_dir = os.path.dirname(__file__)

   # image_refs=[]
    y_position = 300
    overlap_offset=1
    for i in range (len(cartes_photos)):
        path = os.path.join(current_dir, cartes_photos[i])
        #nom = cartes_photos[i]   
        #base_name = nom.replace(".png", "")      
        #mot = PhotoImage(file = path).subsample(4, 4)
        ##mot = mot.subsample(4,4) 
        ##nom = mot + "s"
        ##image_refs.append(mot)
        #carte = tk.Label(fenetre2, image = mot)
        #carte.image = mot
        #cartes_photos[base_name] = carte  
        image=PhotoImage(file=path)
        image=image.subsample(4,4)
        iage=tk.Label(fenetre2, image=image)
        iage.image=image
        iage.place(x=600, y=y_position)
        y_position+=overlap_offset
         #carte.place(x=600,y=300) 

  
    # Position the cards dynamically (13 per row)
   # x_position = 50 + (i % 13) * 50  # 13 cards per row
    #y_position = 50 + (i // 13) * 100  # Move to next row after 13 cards
    #label.place(x=x_position, y=y_position)

    #clubs
    #image_path = os.path.join(current_dir, "ace_of_clubs.png")
    #ace_of_clubs = image_path.resize((125, 182))
    #ac = tk.PhotoImage(file = image_path)
    ##ace_of_clubs = tk.resizeImage(ac, 125, 182)
    #ace_of_clubs_l = tk.Label(fenetre2, image = ac)
    #ace_of_clubs_l.place(x=400,y=200)
    #
    ##diamonds
    #diamant_path=os.path.join(current_dir, "ace_of_diamonds.png")
    #diam= PhotoImage(file=diamant_path)
    #diam=diam.subsample(4,4)
    #diama=tk.Label(fenetre2,image=diam)
    #diama.image=diam
    #diama.place(x=600,y=300)
    
    
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
