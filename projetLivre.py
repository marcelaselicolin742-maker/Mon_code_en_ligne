from datetime import date
print("\n\tDeclinez votre identité svp !, Votre nom , prenom , sexe :")


#fonction d'affichage des livres dans la bibliotheque
def afficher():
    print("Voici les livres disponible dans la bibliotheque")
    print("--"*50)
    for livre, info in bibliotheque.items():
        print(f"titre : '{livre}' écrit par '{info['auteur']}'  nombre de pages : {info['page']}  quantité restante : {info['quantite']}")
    print("--"*50)


dico_emprunter = {}
#fonction qui rend les livres emprunter
def emprunter():
    titre = input('le titre : ').strip().lower()
    if titre not in bibliotheque:
        print("Le livre est introuvable")
        return

    if bibliotheque[titre]["quantite"] <= 0:
        print('Livre indisponible')
        return

    # diminuer le stock si les deux conditions précédentes sont fausses
    bibliotheque[titre]["quantite"] -= 1
    
    #si le livre n'est pas encore dans la liste des emprunts alors :
    if titre not in dico_emprunter:
        dico_emprunter[titre] = {
            "auteur": bibliotheque[titre]["auteur"],
            "page": bibliotheque[titre]["page"],
            "quantite": 1,
            "liste emprunteur": [{
                "nom": f"{nom} {prenom}",
                "date": str(date.today())
            }]
        }
        print("Livre emprunter avec succès")
        for livre, info in dico_emprunter.items():
            print(f"le livre {livre} ecrit par {info['auteur']} a ete emprunter par {info['liste emprunteur'][0]['nom']} le {info['liste emprunteur'][0]['date']}")
        return dico_emprunter
    else:
        dico_emprunter[titre]["quantite"] += 1
        print("Emprunt effectué !! ")
        return dico_emprunter


# fonction pour rendre un livre
def rendre():
    titre = input('le titre a rendre : ').strip().lower()
    if titre not in bibliotheque:
        print("Ce livre n'appartient pas à la bibliothèque")
        return

    # augmenter le stock
    bibliotheque[titre]["quantite"] += 1
    # mettre à jour les emprunts si présents
    if titre in dico_emprunter:
        if dico_emprunter[titre].get("quantite", 0) > 1:
            dico_emprunter[titre]["quantite"] -= 1
            # enlever le dernier emprunteur de la liste
            if dico_emprunter[titre].get("liste emprunteur"):
                dico_emprunter[titre]["liste emprunteur"].pop()
            print("Livre rendu, emprunt décrémenté.")
        else:
            # supprimer l'entrée si plus d'emprunts
            dico_emprunter.pop(titre, None)
            print("Livre rendu et retiré de la liste des emprunts.")
    else:
        print("Livre rendu.")


# fonction pour ajouter un livre dans la bibliotheque
def ajouter():
    titre_raw = input('Titre (clé) : ').strip()
    titre = titre_raw.lower()
    auteur = input('Auteur : ').strip()
    try:
        pages = int(input('Nombre de pages : ').strip())
    except ValueError:
        print("Nombre de pages invalide, annulation de l'ajout.")
        return
    try:
        quant = int(input("Quantité : ").strip())
    except ValueError:
        print("Quantité invalide, annulation de l'ajout.")
        return

    if titre in bibliotheque:
        bibliotheque[titre]["quantite"] += quant
        print(f"Livre existant : quantité augmentée de {quant}.")
    else:
        bibliotheque[titre] = {"auteur": auteur, "page": pages, "quantite": quant}
        print("Nouveau livre ajouté à la bibliothèque.")


#les structures conditionnelles pour le sexe et l'affichage 
while True:
    #on entre les informations du visiteur 
    identité = input("\tséparer par un virgule : ").split(",")
    if len(identité) == 3:
        nom = identité[0].strip()       
        prenom = identité[1].strip()   
        sexe = identité[2].strip()   
        if sexe == "homme":
            print("--"*30)
            print(f"\n\tBonjour Mr {nom} {prenom} \n\tQue voulez-vous faire maintenant !!")
            print("--"*30)
            break
        else:
            print("--"*30)
            print(f"Bonjour Mme {nom} {prenom} \n\tQue voulez-vous faire maintenant !!")
            print("--"*30)
            break

    elif len(identité) != 3:
        print("Les informations donné est inferieur aux infos demeander !!")
        print("Veuillez reessayer : ")
        identité = input(': ').split(',')
        nom = identité[0].strip()       
        prenom = identité[1].strip()   
        sexe = identité[2].strip() 
        if sexe == "homme":
            print("--"*30)
            print(f"\n\tBonjour Mr {nom} {prenom}")
            print(" \n\tQue voulez-vous faire maintenant !!")
            print("--"*30)

            break
        else:
            print("--"*30)
            print(f"\n\tBonjour Mme {nom} {prenom} \n\tQue voulez-vous faire maintenant !!")
            print("--"*30)
            break
        
#liste des livres en stocke
bibliotheque = {"livre1":{"auteur":"wells harrigthon", "page":200 , "quantite":10 },
                "livre2":{"auteur":"Cisco ramon", "page":250 , "quantite":8 },
                "livre3":{"auteur":"Catline snow", "page":300,"quantite":6},
                "livre4":{"auteur":"Ralfi dicline","page":400, "quantite":4 }
                }

while True:
    print("\n\t1 : Afficher les livres dans la bibliotheque")
    print("\t2 : Rendre un livre dans la bibliotheque ")
    print("\t3 : Ajouter un livre dans la bibliotheque")
    print("\t4 : Emprunter un livre dans la bibliotheque")
    print("\t5 : Quitter le programme")

    #choix de l'utilisateur
    print("\n","--"*30)
    choix = input("Votre choix : ")

    if choix == "1":
        afficher()
    elif choix == "2":
        rendre()
    elif choix == "3":
        ajouter()
    elif choix == "4":
        emprunter()
    elif choix == "5":
        print("Au revoir !")
        break
    else:
        print("Choix invalide, veuillez réessayer.")