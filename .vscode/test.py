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

    def revenir_accueil():
        fenetre2.destroy()

    # Variables de jeu
    y_position = 300
    overlap_offset = 30
    score_joueur = 0
    as_valeur = None
    boutons_choix_as = []
    cartes_tirees = []
    cartes_labels = []
    result_label = None
    recommencer_button = None

    def afficher_boutons_choix_as():
        def choisir(val):
            nonlocal as_valeur
            as_valeur = val
            mise_a_jour_score()
            cacher_boutons_choix_as()
            verifier_score()

        bouton_1 = tk.Button(fenetre2, text="1", command=lambda: choisir(1), bg='#a6c9ff', fg='white')
        bouton_11 = tk.Button(fenetre2, text="11", command=lambda: choisir(11), bg='#a6c9ff', fg='white')
        bouton_1.place(x=600, y=500)
        bouton_11.place(x=650, y=500)
        boutons_choix_as.extend([bouton_1, bouton_11])

    def cacher_boutons_choix_as():
        for bouton in boutons_choix_as:
            bouton.destroy()
        boutons_choix_as.clear()

    def mise_a_jour_score():
        nonlocal score_joueur
        if as_valeur is not None:
            score_joueur += as_valeur
            joueur.config(text=f"Joueur ({score_joueur})")

    def verifier_score():
        nonlocal result_label, recommencer_button
        if score_joueur == 21:
            texte = "Black Jack - Super gagné 🥳" if len(cartes_tirees) == 2 else "Gagné ! 🎉"
            result_label = tk.Label(fenetre2, text=texte, fg='green', bg='#c9ffa6', font=("Arial", 20, "bold"))
            result_label.place(x=800, y=200)
            fin_de_jeu()
        elif score_joueur > 21:
            result_label = tk.Label(fenetre2, text="Perdu, bouh 😢", fg='red', bg='#c9ffa6', font=("Arial", 20, "bold"))
            result_label.place(x=800, y=200)
            fin_de_jeu()

    def fin_de_jeu():
        deal_button.config(state=DISABLED)
        stand_button.config(state=DISABLED)
        if recommencer_button is None:
            creer_bouton_recommencer()

    def creer_bouton_recommencer():
        nonlocal recommencer_button
        recommencer_button = tk.Button(fenetre2, text="Recommencer", command=recommencer, bg='#a6c9ff', fg='black')
        recommencer_button.place(x=800, y=250)

    def recommencer():
        nonlocal y_position, score_joueur, as_valeur, cartes_tirees, result_label, recommencer_button
        for label in cartes_labels:
            label.destroy()
        cartes_labels.clear()
        cartes_tirees.clear()
        y_position = 300
        score_joueur = 0
        as_valeur = None
        joueur.config(text="Joueur (0)")
        cacher_boutons_choix_as()
        if result_label:
            result_label.destroy()
            result_label = None
        if recommencer_button:
            recommencer_button.destroy()
            recommencer_button = None
        deal_button.config(state=NORMAL)
        stand_button.config(state=NORMAL)
        melanger()

    def distribution():
        nonlocal y_position, score_joueur, as_valeur
        if cartes_photos:
            carte_tiree = cartes_photos.pop()
            cartes_tirees.append(carte_tiree)
            path = os.path.join(current_dir, carte_tiree)
            image = PhotoImage(file=path).subsample(4, 4)
            carte_label = tk.Label(fenetre2, image=image)
            carte_label.image = image
            carte_label.place(x=600, y=y_position)
            cartes_labels.append(carte_label)
            

            nom_carte = carte_tiree.split('_')[0]
            valeur = get_valeur(carte_tiree)

            if nom_carte == "ace":
                afficher_boutons_choix_as()
            else:
                score_joueur += valeur
                joueur.config(text=f"Joueur ({score_joueur})")
                verifier_score()

    def deal():
        distribution()

    def stand():
        fin_de_jeu()

    # UI
    dealer = tk.Label(fenetre2, text="Croupier", bg='#c9ffa6', fg="black")
    dealer.place(x=150, y=165)
    joueur = tk.Label(fenetre2, text="Joueur (0)", bg='#c9ffa6', fg="black")
    joueur.place(x=350, y=165)

    deal_button = tk.Button(fenetre2, text=" CARTE ! ", bg='#a6c9ff', fg='black', command=deal)
    deal_button.configure(height=3, width=10)
    deal_button.place(x=200, y=300)

    stand_button = tk.Button(fenetre2, text=" RESTER ", bg='#a6c9ff', fg='black', command=stand)
    stand_button.configure(height=3, width=10)
    stand_button.place(x=300, y=300)

    accueil_button = tk.Button(fenetre2, text="🏠", font=("Arial", 12), bg='white', fg='black', command=revenir_accueil)
    accueil_button.configure(height=1, width=2)
    accueil_button.place(x=20, y=20)

    melanger()

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
