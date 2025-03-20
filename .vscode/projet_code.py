import tkinter as tk
from tkinter import PhotoImage
import os


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

bj = tk.Label(fenetre1, text="Black Jack",bg = "#006400", fg = "white", font=("Impact",54))
bj.place(x=150,y=165)

#Bouttons
start = tk.Button(fenetre1, text = " START ", bg = '#42529c', fg = 'white')
start.configure(height=5, width=30)
start.place(x=200,y=300)

regles = tk.Button(fenetre1,text = " REGLES ",bg = '#42529c',fg = 'white')
regles.configure(height=5, width=30)
regles.place(x=200,y=400)



hist = tk.Button(fenetre1,text = " HISTORIQUE ",bg = '#42529c',fg = 'white')#A enlever
hist.configure(height=5, width=30)
hist.place(x=200,y=500)

bouton_quit = tk.Button(fenetre1,text = " QUIT ",bg = 'indian red',command = fenetre1.destroy)
bouton_quit.configure(height=5, width=30)
bouton_quit.place(x=200,y=600)

#mets fenetre1
fenetre1.mainloop()

import tkinter as tk

#Fenetre règle:
#config de fenetre + canvas
fentre_regle= tk.Tk()
fentre_regle.title("Black Jack REGLE")
fentre_regle.config(bg="black")
fentre_regle.geometry("650x800")

#Label
rule=tk.Label(fentre_regle,fg="green", font=('Arial',14),wraplength=600,
              text="But du jeu : Atteindre un total de points le plus proche de 21 sans dépasser "
              "ce nombre.\n"
              
              "Valeurs des cartes : les cartes de 2 à 10 valent leur valeur.Les "
              "figures (Roi, Dame, Valet) valent 10 points. L'As vaut 1 ou 11 points (selon "
              "ce qui vous avantage).\n "

              "Déroulement :Chaque joueur reçoit 2 cartes face visible, "
              "et le croupier a une carte visible et une face cachée. Vous pouvez demander "
              "d’autres cartes (tirer), ou garder votre total actuel (rester). Si vos cartes"
              " dépassent 21, vous perdez (on appelle cela 'sauter'). \n "

              "Gagner : Vous gagnez si votre total est égal à 21 ou le plus proche possible sans dépasser cette valeur. "
              "Un Blackjack (21 avec deux cartes seulement, As + 10 ou figure) est la meilleure main possible.")  #\n permet le retour a la ligne
rule.pack()


#affichage fenetre regle
fentre_regle.mainloop()