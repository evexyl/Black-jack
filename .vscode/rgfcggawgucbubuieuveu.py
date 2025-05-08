from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import os
from random import shuffle

# Fenetre règle:
def on_open_fenetre():
    fentre_regle = tk.Toplevel()
    fentre_regle.title("Black Jack REGLE")
    fentre_regle.config(bg="black")
    fentre_regle.geometry("650x800")

    current_dir = os.path.dirname(__file__)
    blabla_path = os.path.join(current_dir, "regle python.txt")
    with open(blabla_path, "r", encoding="utf-8") as file:
        blablacar = file.read()

    rule = tk.Text(fentre_regle, wrap=tk.WORD, fg="green", bg="Black", font=("Arial", 14), borderwidth=0, highlightthickness=0)
    rule.insert(tk.END, blablacar)
    rule.config(state=tk.DISABLED)
    rule.pack()

# Fenetre de jeu
def on_open_fenetre2():
    fenetre2 = tk.Toplevel()
    fenetre2.title("Black Jack JEU")
    fenetre2.geometry("1200x700")
    fenetre2.config(bg='#c9ffa6')

    current_dir = os.path.dirname(__file__)

    cartes_photos = [
        "ace_of_clubs.png", "two_of_clubs.png", "three_of_clubs.png", "four_of_clubs.png", "five_of_clubs.png", "six_of_clubs.png", "seven_of_clubs.png", "eight_of_clubs.png", "nine_of_clubs.png", "ten_of_clubs.png", "jack_of_clubs.png", "queen_of_clubs.png", "king_of_clubs.png",
        "ace_of_diamonds.png", "two_of_diamonds.png", "three_of_diamonds.png", "four_of_diamonds.png", "five_of_diamonds.png", "six_of_diamonds.png", "seven_of_diamonds.png", "eight_of_diamonds.png", "nine_of_diamonds.png", "ten_of_diamonds.png", "jack_of_diamonds.png", "queen_of_diamonds.png", "king_of_diamonds.png",
        "ace_of_hearts.png", "two_of_hearts.png", "three_of_hearts.png", "four_of_hearts.png", "five_of_hearts.png", "six_of_hearts.png", "seven_of_hearts.png", "eight_of_hearts.png", "nine_of_hearts.png", "ten_of_hearts.png", "jack_of_hearts.png", "queen_of_hearts.png", "king_of_hearts.png",
        "ace_of_spades.png", "two_of_spades.png", "three_of_spades.png", "four_of_spades.png", "five_of_spades.png", "six_of_spades.png", "seven_of_spades.png", "eight_of_spades.png", "nine_of_spades.png", "ten_of_spades.png", "jack_of_spades.png", "queen_of_spades.png", "king_of_spades.png"
    ]

    valeur_cartes = {
        'ace': 11,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'jack': 10,
        'queen': 10,
        'king': 10
    }

    def get_valeur(carte_filename):
        nom = carte_filename.split('_of_')[0]
        return valeur_cartes[nom]

    def melanger():
        shuffle(cartes_photos)

    melanger()

    y_position = 300
    overlap_offset = 1
    score_joueur = 0
    boutons_choix_as = []
    nbcarte = 0

    def distribution():
        nonlocal y_position, score_joueur, boutons_choix_as, nbcarte

        if cartes_photos:
            carte_tiree = cartes_photos.pop()
            path = os.path.join(current_dir, carte_tiree)
            image = PhotoImage(file = path).subsample(4, 4)
            carte_label = tk.Label(fenetre2, image = image)
            carte_label.image = image
            carte_label.place(x = 600, y = y_position)
            

            nom_carte = carte_tiree.split('_')[0]
            valeur = get_valeur(carte_tiree)

            if nom_carte == "ace":
                afficher_boutons_choix_as()
            else:
                score_joueur += valeur
                joueur.config(text = f"Joueur ({score_joueur})")

            target_x, target_y = 100, 450
            def move(speed = 20): #ne marche pas encore dont push
                x = carte_label.winfo_x()
                y = carte_label.winfo_y()

                dx = target_x - x
                dy = target_y - y
                distance = (dx**2 + dy**2)**0.5

                if distance < speed:
                    for i in range(nbcarte):
                        carte_label.place(x = target_x, y = target_y) 
                        x += 150
                else:
                    step_x = dx / distance * speed
                    step_y = dy / distance * speed
                    carte_label.place(x=x + step_x, y=y + step_y)
                    carte_label.after(16, move)  

            carte_label.after(50, move)

    def afficher_boutons_choix_as():
        nonlocal boutons_choix_as, score_joueur

        cacher_boutons_choix_as()

        def choisir(valeur_as):
            nonlocal score_joueur
            score_joueur += valeur_as
            joueur.config(text=f"Joueur ({score_joueur})")
            cacher_boutons_choix_as()

        bouton_1 = tk.Button(fenetre2, text="1", command=lambda: choisir(1), bg='#a6c9ff', fg='white')
        bouton_1.place(x=600, y=500)

        bouton_11 = tk.Button(fenetre2, text="11", command=lambda: choisir(11), bg='#a6c9ff', fg='white')
        bouton_11.place(x=650, y=500)

        boutons_choix_as.append(bouton_1)
        boutons_choix_as.append(bouton_11)

    def cacher_boutons_choix_as():
        nonlocal boutons_choix_as
        for bouton in boutons_choix_as:
            bouton.destroy()
        boutons_choix_as.clear()

    def deal():
        distribution()
        nbcarte += 1

    def stand():
        pass

    def compteur():
        pass

    def revenir_accueil():
        fenetre2.destroy()

    # Labels
    dealer = tk.Label(fenetre2, text="Croupier", bg='#c9ffa6', fg="black")
    dealer.place(x=150, y=165)

    joueur = tk.Label(fenetre2, text="Joueur (0)", bg='#c9ffa6', fg="black")
    joueur.place(x=350, y=165)

    cmpt_d = tk.Label(fenetre2, text="N", bg='#c9ffa6', fg="black")
    cmpt_d.place(x=250, y=165)

    cmpt_j = tk.Label(fenetre2, text="", bg='#c9ffa6', fg="black")
    cmpt_j.place(x=450, y=165)

    # Boutons
    deal_button = tk.Button(fenetre2, text=" CARTE ! ", bg='#a6c9ff', fg='black', command=deal)
    deal_button.configure(height=3, width=10)
    deal_button.place(x=200, y=300)

    stand_button = tk.Button(fenetre2, text=" RESTER ", bg='#a6c9ff', fg='black', command=stand)
    stand_button.configure(height=3, width=10)
    stand_button.place(x=300, y=300)

    accueil_button = tk.Button(fenetre2, text="🏠", bg='white', fg='black', command=revenir_accueil)
    accueil_button.configure(height=1, width=2)
    accueil_button.place(x=20, y=20)

    #CANVAS
    pp = tk.Canvas(fenetre2, width = 1200, height = 300, bg = '#ffa6c9')
    pp.place(x = 0, y = 400)

# Fenetre principale
fenetre1 = tk.Tk()
fenetre1.title("Black Jack MENU")
fenetre1.geometry("650x800")

current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "casino.png")
image = PhotoImage(file=image_path)

image_bj = tk.Label(fenetre1, image=image)
image_bj.image = image
image_bj.pack()

bj = tk.Label(fenetre1, text="Black Jack", bg="Black", fg="white", font=("Impact", 54))
bj.place(x=150, y=165)

start = tk.Button(fenetre1, text=" START ", bg='Black', fg='white', command=on_open_fenetre2)
start.configure(height=5, width=30)
start.place(x=200, y=350)

regles = tk.Button(fenetre1, text=" REGLES ", bg='White', fg='Black', command=on_open_fenetre)
regles.configure(height=5, width=30)
regles.place(x=200, y=450)

bouton_quit = tk.Button(fenetre1, text=" QUIT ", bg='#ff0000', command=fenetre1.destroy)
bouton_quit.configure(height=5, width=30)
bouton_quit.place(x=200, y=550)

fenetre1.mainloop()