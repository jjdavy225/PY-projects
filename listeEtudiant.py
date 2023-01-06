class listEtudiant:
    def __init__(self) -> None:
        self.racine = None
    
    def ajout(self):
        element = self.racine
        while element != None:
            element = element.suiv
        print("------------------------------Informations nouvel étudiant---------------------------------")
        nom = input("Nom : ")
        prenoms = input("Prénoms : ")
        mat = input("Matricule : ")
        moy = input("Moyenne : ")
        self.racine = etudiant(nom,prenoms,mat,moy)
        print('Etudiant ajouté avec succès :)')
        print("-------------------------------------------------------------------------------------------")
    
    def supprimer(self):
        print("----------------------------------Etudiant à supprimer-------------------------------------")
        mat = input("Entrer le matricule : ")
        element = self.racine
        while element.mat != mat:
            element = element.suiv
            if element == None:
                print(f"Le matricule entré ne correspond à aucun étudiant dans la liste. Veuillez vérifier et recommencer !!")
                return None
        ans = input(f"Voulez-vous supprimer l'étudiant {element.nom} {element.prenoms} ? (o/n)")
        
        
        print("-------------------------------------------------------------------------------------------")
    
        
class etudiant:
    def __init__(self,nom,prenoms,mat,moy) -> None:
        self.nom = nom
        self.prenoms = prenoms
        self.mat = mat
        self.moy = moy
        self.suiv = None
            
        
listEtudiant1 = listEtudiant()
listEtudiant1.ajout()
listEtudiant1.supprimer()