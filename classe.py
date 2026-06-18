"""la classe qui est a base de tout cette programme"""
class Bibliotheque:
    "la classe bibliotheque initialisé avec un dictionnaire contenant les livres predefini"
    def __init__(self):
        self.dictionnaire = {
          "le soleil":{
              "auteur" : "Jez","page" : 200,"quantité" : 3
          }  ,
          "Ma vie" : {
              "auteur":"Brulebois","page":150,"quantité":2
          },
          "Vivre loin de souçi":{
              "auteur":"Marie","page":196, "quantité":4
          },
          "Ici bas":{
              "auteur":"Françine","page":350,"quantité":10
          }
        }
        self.dico_emprunt = {}
        self.dico_nouveau_ajout  = {}

    """la focntion qui afficher un livre"""
    def Afficher_livre(self, titre):
        "pour afficher qu'une seule livre si existe"
        for livre, carac in self.dictionnaire.items():
            if livre.lower() == titre:
                print("le livre rechercher est :",titre)
                print("\n titre : --",titre,"-- auteur : --",carac["auteur"],"-- nb page : -",carac["page"],"- quantité: -",carac["quantité"],"-.")


    def Afficher_tout(self):
        for titre, info in self.dictionnaire.items():
            print("le titre : --" , titre  ,"-- auteur : -",info["auteur"] , "- nb page : ", info["page"], "-  il reste --", info["quantité"], "-- d'exemplaire.")
        print("le(s) livre(s) emprunter : \n",[caract for caract in self.dico_emprunt])

    """fonction pour emprunter un livre"""
    def Emprunter(self,titre,date_emprunt , nom):
        for livre, caract in self.dictionnaire.items():
            if livre.lower() == titre.lower():
                if caract["quantité"] > 0:
                    print(f"le livre -{titre}- est emprunter avec succèss!")
                    caract["quantité"] -= 1
                    print(f"liste d'emprunt :\n\t titre : -{livre}-\n\tquantité : --{caract["quantité"]}--\n\tdate d'emprunt : -{date_emprunt}-\n\t par -{nom}-")
        
       
objet = Bibliotheque()
#objet.Afficher_livre("le soleil")
objet.Emprunter("ma vie","10/06/2026","manana")
#objet.Afficher_tout()
