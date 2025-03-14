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
image=PhotoImage(file="casino.png")
<<<<<<< HEAD
image_bj=tk.Label(fenetre1,image)
=======
image_bj=tk.Label(fenetre1,image=image)
>>>>>>> 2e59bac6f0ebc2969d412b5abf5965ea00062fc9
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