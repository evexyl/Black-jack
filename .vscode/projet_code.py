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

bj = tk.Label(fenetre1, text="Black Jack",bg = "#006400", fg = "white", font=("Impact",54))   #fond de black jack en noir et font=Helvetica
bj.place(x=150,y=165)

#Bouttons    #changer couleur bouton 
start = tk.Button(fenetre1, text = " START ", bg = '#42529c', fg = 'white')
start.configure(height=5, width=30)
start.place(x=200,y=350)

regles = tk.Button(fenetre1,text = " REGLES ",bg = '#42529c',fg = 'white')
regles.configure(height=5, width=30)
regles.place(x=200,y=450)

bouton_quit = tk.Button(fenetre1,text = " QUIT ",bg = 'indian red',command = fenetre1.destroy)
bouton_quit.configure(height=5, width=30)
bouton_quit.place(x=200,y=550)

#mets fenetre1
fenetre1.mainloop()

###############################################################################################
#FENETRE 2

###############################################################################################
#FENETRE 3