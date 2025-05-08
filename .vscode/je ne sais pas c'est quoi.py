def distribution():
        if cartes_photos:  # Si il reste des cartes à distribuer
            carte_tiree = cartes_photos.pop()  # Retirer la dernière carte de la liste
            path = os.path.join(current_dir, carte_tiree)  # Récupérer le chemin de la carte
            image = PhotoImage(file=path).subsample(4, 4)  # Charger l'image
            carte_label = tk.Label(fenetre2, image=image)  # Créer un label avec l'image
            carte_label.image = image  # Garder la référence à l'image
            carte_label.place(x=600, y=400)  
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