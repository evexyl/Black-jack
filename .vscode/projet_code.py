import tkinter as tk
from tkinter import PhotoImage

#FENETRE 1:
#config de fenetre + canvas
fenetre1 = tk.Tk()
fenetre1.title("Black Jack MENU")
fenetre1.geometry("650x800")
#fenetre1.configure(bg='#006400')


#Label
bj = tk.Label(fenetre1, text="Black Jack", bg = "#006400", fg = "white", font = ("Impact", 54))
bj.place(x=300,y=165)

image_path="d:/LDDBI/L1/Semestre 2/Informatique/IN200/Projet/Black-jack/.vscode/casino.png"
image= PhotoImage(file=image_path)

image_bj=tk.Label(fenetre1,image=image)
image_bj.image=image
image_bj.pack()


#Bouttons
start = tk.Button(fenetre1, text = " START ", bg = '#42529c', fg = 'white')
start.configure(height=5, width=30)
start.place(x=200,y=400)

regles = tk.Button(fenetre1,text = " REGLES ",bg = '#42529c',fg = 'white')
regles.configure(height=5, width=30)
regles.place(x=200,y=500)

hist = tk.Button(fenetre1,text = " HISTORIQUE ",bg = '#42529c',fg = 'white')
hist.configure(height=5, width=30)
hist.place(x=200,y=600)

bouton_quit = tk.Button(fenetre1,text = " QUIT ",bg = 'indian red',command = fenetre1.destroy)
bouton_quit.configure(height=5, width=30)
bouton_quit.place(x=200,y=700)

#mets fenetre
fenetre1.mainloop()