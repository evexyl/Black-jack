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
    fentre_regle.config(bg="Black")
    fentre_regle.geometry("650x800")

#Label
    current_dir = os.path.dirname(__file__)   #recupere le dossier
    blabla_path = os.path.join(current_dir, "regle python.txt")  #cree le chemin complet
    with open(blabla_path, "r", encoding="utf-8") as file:   #ouvre  et lis le fichier en utf-8 
        blablacar=file.read()
    rule=tk.Text(fentre_regle, wrap=tk.WORD,fg="#469735", bg="Black", font=("Helvetica",14), borderwidth=0, highlightthickness=0) #texte revient a la ligne apres un mot (sans couper de mot ou quoi que ce soit), pas de bordure ni de contour de focus
    rule.insert(tk.END, blablacar)  #insere le texte lu dans le widget Text
    rule.config(state=tk.DISABLED)   #empeche la modif du texte

    rule.pack()    #affiche le widget Text dans la fenetre 

#############################################################################################################################
#FENETRE 2
#FONCTIONS
def on_open_fenetre2():
    fenetre2 = tk.Toplevel()
    fenetre2.title("Black Jack JEU")
    fenetre2.geometry("943x700")
    fenetre2.config(bg = '#13563B')
    pp = tk.Canvas(fenetre2, width = 950, height = 350, bg = '#13563B')
    pp.place(x = -2, y = 350)

    def melanger():# #mélanger les cartes
        shuffle(cartes_photos) 

    def accueil():
        fenetre2.destroy()

    #VARIABLES
    #Positions
    y_position=300
    x_position=100
    y_position_croupier=50
    x_position_croupier=100

    overlap_offset=30
    score_joueur=0
    score_croupier=0
    valeur_as=None
    cartes_labels=[]
    cartes_tirees=[]
    boutons_choix_as = []
    resultat=None

    #Move
    nbcarte_j = 0
    espcarte_j = 0 
    nbcarte_c = 0
    espcarte_c = 0 

    def choix_as():
        def choisir (val):
            nonlocal valeur_as, score_joueur
            valeur_as=val
            score_joueur+=valeur_as
            joueur.config(text=f"Joueur({score_joueur})")#IA
            choix_as_disparus()
            compteur()#met à jour le score du joueur
            tirer.config(state=tk.NORMAL)
            rester.config(state=tk.NORMAL)
            
        tirer.config(state=tk.DISABLED)#désactive les boutons le temps du choix
        rester.config(state=tk.DISABLED)
        cartes2.config(state=tk.DISABLED)
        bouton_1 = tk.Button(fenetre2, text = '1', command=lambda:choisir(1), bg = '#000000', fg = "white")#définitions des boutons
        bouton_11 = tk.Button(fenetre2, text = '11', command=lambda:choisir(11), bg = '#000000', fg = "white")
        bouton_1.place(x=775, y=471) #placement des boutons
        bouton_11.place(x=830, y=471)
        boutons_choix_as.append(bouton_1) #créer une liste pour que les boutons disparaissent après
        boutons_choix_as.append(bouton_11)
    
    def choix_as_disparus():#disparition des boutons
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

    def donner_2_cartes(playeur):  #la fonction sert a distribuer 2 cartes au joueur (palyeur=True) et au croupier (playeur=False)
        nonlocal x_position, x_position_croupier, score_joueur, score_croupier
        for i in range(2):
            if cartes_photos:
                carte_tiree=cartes_photos.pop()
                cartes_tirees.append(carte_tiree)
                path=os.path.join(current_dir, carte_tiree)
                image=PhotoImage(file=path).subsample(4,4)
                carte_label=tk.Label(fenetre2, image=image)
                carte_label.image=image
                
                if playeur:
                    carte_label.place(x = x_position, y = 450)
                    x_position += 30
                else:
                    carte_label.place(x = x_position_croupier, y = 100)
                    x_position_croupier += 30
                    
                cartes_labels.append(carte_label)
                nom_carte=carte_tiree.split('_')[0]  #recupere le nom de la carte
                valeur=get_valeur(carte_tiree)   #calcul valeur de la carte

                if nom_carte=="ace":
                    if playeur:
                        choix_as()
                    else:
                        valeur=11 if score_croupier+11<=21 else 1
                if playeur:     #cette iiteration c'est pour la mise a jour du score
                    score_joueur+=valeur
                    joueur.config(text=f"Joueur({score_joueur})")
                else:
                    score_croupier+=valeur
                    dealer.config(text=f"Croupier({score_croupier})")
           

    def distribution (): #distribuer les cartes
        nonlocal y_position, score_joueur, valeur_as, nbcarte_j, espcarte_j
        if cartes_photos: #vérifie qu'il rest des cartes dans le paquet
            carte_tiree = cartes_photos.pop() #prend la dernièere carte du paquet
            cartes_tirees.append(carte_tiree) #rajoute à la liste des cartes tirées (mémoire)
            path = os.path.join(current_dir, carte_tiree) #affichage des cartes
            image = PhotoImage(file=path).subsample(4,4)
            carte_label = tk.Label(fenetre2, image=image)
            carte_label.image = image
            carte_label.place(x=750, y = 259)
            cartes_labels.append(carte_label)    
            nom_carte = carte_tiree.split('_')[0]#nom de la carte avec sa vealeur associée
            valeur = get_valeur(carte_tiree)    
            if nom_carte == 'ace': #choix 1 ou 11 + relier au compteur
                choix_as()
            else:
                score_joueur += valeur #ajout valeur de la carte au score
                joueur.config(text = f'Joueur({score_joueur})')
                compteur() #est-ce que le joueur a gagné ou perdu ?

            target_x, target_y = 160 + espcarte_j, 450
            def move_j(speed = 20):    #mix entre IA et inspiration de video regarde
                x = carte_label.winfo_x()
                y = carte_label.winfo_y()

                dx = target_x - x
                dy = target_y - y
                distance = (dx**2 + dy**2)**0.5

                if distance < speed:
                    for i in range(nbcarte_j):
                        carte_label.place(x = target_x, y = target_y) 
                        x += 150
                else:
                    step_x = dx / distance * speed
                    step_y = dy / distance * speed
                    carte_label.place(x=x + step_x, y=y + step_y)
                    carte_label.after(16, move_j)  

            carte_label.after(50, move_j)
            
    
    def distribution_croupier():
        nonlocal score_croupier, y_position_croupier
        if cartes_photos:
            carte_tiree=cartes_photos.pop()
            cartes_tirees.append(carte_tiree)
            path=os.path.join(current_dir, carte_tiree)
            image=PhotoImage(file=path).subsample(4,4)
            carte_label=tk.Label(fenetre2, image=image)
            carte_label.image=image
            carte_label.place(x=750, y = 259)
            cartes_labels.append(carte_label)
            nom_carte=carte_tiree.split('_')[0]
            valeur=get_valeur(carte_tiree)
            
            if nom_carte=="ace":    #prend la valeur la plus benefique pour le croupier ia
                valeur=11 if score_croupier+11<=21 else 1  #si le score du croupier+11 est <21, on prend 11 comme valeur pour l'as, sinon c'est 1
        score_croupier+=valeur
        dealer.config(text=f"Croupier({score_croupier})")   #met a jour le texte affiche dans le label pour montrer le score actuel

        target_x, target_y = 160 + espcarte_c, 100
        def move_c(speed = 20): 
            x = carte_label.winfo_x()
            y = carte_label.winfo_y()

            dx = target_x - x
            dy = target_y - y
            distance = (dx**2 + dy**2)**0.5

            if distance < speed:
                for i in range(nbcarte_c):
                    carte_label.place(x = target_x, y = target_y) 
                    x += 150
            else:
                step_x = dx / distance * speed
                step_y = dy / distance * speed
                carte_label.place(x=x + step_x, y=y + step_y)
                carte_label.after(16, move_c)  

        carte_label.after(50, move_c)

    resultat=tk.Label(fenetre2, fg='green', bg='#13563B', font=("Arial", 20, "bold"))
    resultat.place(x=400, y=200)    #on peut pas la mettre direct dans les iteration car elle chanfe a chaque fois et donc ca bug

    def compteur():   #verifie les scores et les mets a jour durant la partie
        nonlocal score_croupier, score_joueur, resultat

        if score_joueur==21 and len(cartes_tirees)==2:
            blabla1="Black Jack - Bravo vous avez gagné 🥳"
            resultat.config(text=blabla1)   #met a jour la variable resultat
            tirer.config(state=tk.DISABLED)
            rester.config(state=tk.DISABLED)        

        elif (score_croupier==21 and len(cartes_tirees)==2):
            blabla3="Bouh, vous avez perdu 🤣"
            resultat.config(text=blabla3)
            tirer.config(state=tk.DISABLED)
            rester.config(state=tk.DISABLED)
        
        elif (score_croupier<score_joueur and score_joueur==21) or score_croupier>21:
            blabla2="Bravo, vous venez de remporter la partie"
            resultat.config(text=blabla2)
            tirer.config(state=tk.DISABLED)
            rester.config(state=tk.DISABLED) 
        
        elif (score_croupier>score_joueur and score_croupier==21) or score_joueur>21:
            blabla3="Blast - Bouh vous avez perdu 🤣"
            resultat.config(text=blabla3)
            tirer.config(state=tk.DISABLED)
            rester.config(state=tk.DISABLED)
        
        elif (score_croupier==score_joueur and len(cartes_tirees)==2) or (score_joueur==21 and score_croupier==21):
            blabla4="Egalité, c'est bien joué 👍"
            resultat.config(text=blabla4)
            tirer.config(state=tk.DISABLED)
            rester.config(state=tk.DISABLED)

        else:
            resultat.config(text="")

    

    def deal ():    #Fonction pour avoir une carte
        nonlocal nbcarte_j, espcarte_j
        distribution()
        nbcarte_j += 1
        espcarte_j += 30

    def stand():    # Fonction pour rester
        nonlocal nbcarte_c, espcarte_c
        distribution_croupier()
        compteur()
        nbcarte_c += 1
        espcarte_c += 30
        tirer.config(state=tk.DISABLED)

    def piocher2():
        donner_2_cartes(playeur=True)  #donne 2cartes au joueur et au croupier
        donner_2_cartes(playeur=False)
        compteur()
        cartes2.place_forget() #fait disparaitre le boutton ia

    #LABELS
    dealer = tk.Label(fenetre2, text ="Croupier", bg = '#13563B', fg = "white",font = ("Helvetica",25))
    dealer.place(x=20)

    joueur = tk.Label(fenetre2, text ="Joueur", bg = '#13563B', fg = "white",font = ("Helvetica",25))
    joueur.place(x=20,y=353)

    def bouton_recommencer():
        nonlocal cartes_photos, cartes_labels, cartes_tirees, score_joueur, score_croupier, y_position, y_position_croupier
        for label in cartes_labels:
            label.destroy()   #enleve les cartes piochées 
        cartes_tirees.clear() #vide la liste des cartes déjà piochées (mémoire)
        melanger()  #remélage les cartes
        score_joueur = 0 #remet les scores à 0
        score_croupier = 0
        y_position = 300 #remet les cartes à la bonne position
        y_position_croupier = 200
        joueur.config(text="Joueur(0)")#les scores sont reécris
        dealer.config(text="Croupier(0)")
        tirer.config(state=NORMAL)#récative les boutons
        rester.config(state=NORMAL)
        cartes2.config(state=NORMAL)
        cartes2.place(x=470, y=325)
        choix_as_disparus()#fait disparaitre les boutons 1 ou 11
        resultat.config(text="") #efface gagné ou perdu

    recommencer_bouton = tk.Button(fenetre2, text="Recommencer", bg="#FFFFFF", fg="black", command=bouton_recommencer)
    recommencer_bouton.place(x=843, y=35) #création du bouton

    #BOUTONS
    tirer = tk.Button(fenetre2, text = " CARTE ! ", bg = '#000000', fg = 'white',command = deal)
    tirer.configure(height=3, width=10)
    tirer.place(x=610,y=280)

    rester = tk.Button(fenetre2, text = " RESTER ", bg = '#000000', fg = 'white', command= stand)
    rester.configure(height=3, width=10)
    rester.place(x=610,y=366)

    cartes2= tk.Button(fenetre2, text = " Commencer ", bg = '#000000', fg = 'white', command= piocher2)
    cartes2.configure(height=3, width=10)
    cartes2.place(x=470,y=325)

    bouton_accueil= tk.Button(fenetre2, text="Accueil", bg = "#FF0000", fg="black", command = accueil)
    bouton_accueil.configure(height=1, width=6)
    bouton_accueil.place(x=843, y=0)


#ca a servi au debut de la creation du jeu et on s'est appuyé dessu ducoup pour certaines fonctions
    #dimension cartes: 500 x 726
 #   current_dir = os.path.dirname(__file__)

   # image_refs=[]
    y_position = 300
    overlap_offset=1
    for i in range (len(cartes_photos)):
        path = os.path.join(current_dir, cartes_photos[i]) 
        image=PhotoImage(file=path)
        image=image.subsample(4,4)
        iage=tk.Label(fenetre2, image=image)
        iage.image=image
        iage.place(x=750, y=259)
        #y_position+=overlap_offset

    
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
