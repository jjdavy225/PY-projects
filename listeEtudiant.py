class etudiant:
    def __init__(self,nom,prenoms,mat,moy) -> None:
        self.nom = nom
        self.prenoms = prenoms
        self.mat = mat
        self.moy = moy
        self.suiv = None
        
    def setSuiv(self,obj):
        self.suiv = obj
class listEtudiant:
    def __init__(self) -> None:
        self.racine = None
    
    def setRacine(self,obj):
        self.racine = obj
        
    @staticmethod
    def sortedTest(elt,suiv)->bool:
        if elt.nom.lower() < suiv.nom.lower():
            return True
        elif elt.nom.lower() == suiv.nom.lower() and elt.prenoms.lower() <= suiv.prenoms.lower():
            return True
        else:
            return False
    
    def fusion(self,list2):
        element1 = self.racine
        while element1.suiv != None:
            element1 = element1.suiv
        element1.setSuiv(list2.racine)
        self.triList()
        
    def triList(self):
        triee = False
        while not triee:
            triee = True
            element = self.racine
            suiv = element.suiv
            if self.sortedTest(element,suiv):
                while suiv.suiv != None:
                    prec = element
                    element = suiv
                    suiv = suiv.suiv
                    if not self.sortedTest(element,suiv):
                        element.setSuiv(suiv.suiv)
                        prec.setSuiv(suiv)
                        suiv.setSuiv(element)
                        triee = False
            else:
                element.setSuiv(suiv.suiv)
                suiv.setSuiv(element)
                self.setRacine(suiv)
                triee = False
        
    def inverseList(self):
        listE = []
        element = self.racine
        while element != None:
            listE.append(element)
            element = element.suiv
        rev = listE[::-1]
        for i in range(len(rev)):
            if i == 0:
                self.setRacine(rev[i])
            if i+1 <= len(rev)-1:
                rev[i].setSuiv(rev[i+1])
            else:
                rev[i].setSuiv(None)
            
    def promoFinale(self,moy):
        element = self.racine
        while element.moy < moy:
            self.setRacine(element.suiv)
            del element
            element = self.racine
        while element.suiv != None:
            prec = element
            element = element.suiv
            if element.moy < moy:
                prec.setSuiv(element.suiv)
                del element
                element = prec
        print("---------------------Mise à jour de la promo éffectuée avec succès-------------------------")
                
    def ajout(self):
        print("------------------------------Informations nouvel étudiant---------------------------------")
        nom = input("Nom : ")
        prenoms = input("Prénoms : ")
        mat = input("Matricule : ")
        moy = int(input("Moyenne : "))
        student = etudiant(nom,prenoms,mat,moy)
        element = self.racine
        if element == None:
            self.setRacine(student)
        else:
            while element.suiv != None:
                element = element.suiv
            element.setSuiv(student)
        print('Etudiant ajouté avec succès :)')
        print()
        
    def ajoutM(self):
        print("------------------------------Informations nouvel étudiant---------------------------------")
        nom = input("Nom : ")
        prenoms = input("Prénoms : ")
        mat = input("Matricule : ")
        moy = input("Moyenne : ")
        student = etudiant(nom,prenoms,mat,moy)
        element = self.racine
        if element == None or self.sortedTest(student,element):
            self.setRacine(student)
            student.setSuiv(element)
        else:
            while element.suiv != None and not self.sortedTest(student,element.suiv):
                element = element.suiv
            student.setSuiv(element.suiv)
            element.setSuiv(student)
        print('Etudiant ajouté avec succès :)')
        print()
    
    def supprimer(self):
        print("----------------------------------Etudiant à supprimer-------------------------------------")
        mat = input("Entrer le matricule : ")
        prec = None
        element = self.racine
        while element.mat != mat:
            prec = element
            element = element.suiv
            if element == None:
                print(f"Le matricule entré ne correspond à aucun étudiant dans la liste. Veuillez vérifier et recommencer !!")
                return None
        ans = input(f"Voulez-vous supprimer l'étudiant {element.nom} {element.prenoms} ? (o/n) : ")
        if ans.lower() == 'o' or ans.lower() == 'oui':
            if prec == None: 
                self.setRacine(element.suiv)
                del element
            else:
                prec.setSuiv(element.suiv)
                del element
        print("Etudiant supprimé avec succès :)")
        print()
        
    def __str__(self):
        print("----------------------------------Liste des étudiants--------------------------------------")
        element = self.racine
        nb = 0
        while element != None:
            nb+=1
            print(f"---Etudiant [{nb}]---")
            print(f"-Matricule : {element.mat}")
            print(f"-Nom et prénoms : {element.nom} {element.prenoms}")
            print(f"-Moyenne : {element.moy}")
            print()
            element = element.suiv
            
        
listEtudiant1 = listEtudiant()
listEtudiant1.ajout()
listEtudiant1.ajout()
listEtudiant1.ajout()
listEtudiant1.__str__()
listEtudiant2 = listEtudiant()
listEtudiant2.ajout()
listEtudiant2.ajout()
listEtudiant2.__str__()
# listEtudiant1.__str__()
# listEtudiant1.triList()
# listEtudiant1.__str__()
# listEtudiant1.inverseList()
# listEtudiant1.__str__()
# listEtudiant1.ajoutM()
# listEtudiant1.__str__()
# listEtudiant1.promoFinale(2)
# listEtudiant1.__str__()
listEtudiant1.fusion(listEtudiant2)
listEtudiant1.__str__()
