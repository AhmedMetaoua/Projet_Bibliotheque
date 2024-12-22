from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtWidgets
import sys
from Menu_principale import Ui_MainWindow 
from PyQt5.QtWidgets import QMessageBox

from ajouter_etudiant_fct import Ajouter_etudiant
from supprimer_etudiant_fct import Supprimer_etudiant
from modifier_etudiant_fct import Modifier_etudiant
from afficher_etudiant_fct import Afficher_etudiant

from ajouter_livre_fct import Ajouter_livre
from modifier_livre_fct import Modifier_livre
from supprimer_livre_fct import Supprimer_livre
from afficher_livre_fct import Afficher_livre

from ajouter_emprunt_fct import Ajouter_emprunt
from retour_emprunt_fct import Retour_emprunt
from modifier_emprunt_fct import Modifier_emprunt
from supprimer_emprunt_fct import Supprimer_emprunt
from afficher_emprunt_fct import Afficher_emprunt

from class_bibliotheque import Bibliotheque
from class_etudiant import Etudiant
from class_emprunt import Emprunt
from class_livre import Livre

class MainUI:
    def __init__(self) :
        self.done = False
        #creation de la fenetre principale
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.bib=Bibliotheque()

        #les action pour chaque boutton de la barre
        self.ui.actionAjouter_Un_Etudiant.triggered.connect(self.ajoute)
        self.ui.actionSupprimer_Un_Etudiant.triggered.connect(self.supprime)
        self.ui.actionModifier_Etudiant.triggered.connect(self.modifier)
        self.ui.actionRecherche_Affichage_Trie.triggered.connect(self.affiche)

        self.ui.actionAjouter_Nouveau_Livre.triggered.connect(self.ajout_livre)
        self.ui.actionSupprimer_Un_Livre.triggered.connect(self.supp_livre)
        self.ui.actionModifier_Nbr_D_Exemplaires.triggered.connect(self.modif_livre)
        self.ui.actionRecherche_Affichage.triggered.connect(self.recherche_affiche)

        self.ui.actionAjouter_Un_Nouvel_Emprunt.triggered.connect(self.ajout_emprunt)
        self.ui.actionRetour_D_un_Emprunt.triggered.connect(self.retour_emp)
        self.ui.actionSupprimer_Un_Emprunt.triggered.connect(self.supp_emp)
        self.ui.actionModifier_Emprunt.triggered.connect(self.modif_emp)
        self.ui.actionRecherche_Affichage_2.triggered.connect(self.afficher_emprunt)

        # Recuperation et Enregistrement
        self.ui.actionEnregistrement_Des_Etudiants.triggered.connect(self.enregistrerEtudiant)
        self.ui.actionRecuperation_Des_Etudiants.triggered.connect(self.recupererEtudiant)
        self.ui.actionEnregistrement_Des_Livres.triggered.connect(self.enregistrerLivre)
        self.ui.actionRecuperation_Des_Livres.triggered.connect(self.recupererLivre)
        self.ui.actionEnregistrement_Des_Emprunts.triggered.connect(self.enregistrerEmprunt)
        self.ui.actionRecuperation_Des_Emprunts.triggered.connect(self.recupererEmprunt)
        # Recuperation et Enregistrement De Tous Fichiers
        self.ui.actionRecuperer_Tous.triggered.connect(self.recupererEtudiant)
        self.ui.actionRecuperer_Tous.triggered.connect(self.recupererLivre)
        self.ui.actionRecuperer_Tous.triggered.connect(self.recupererEmprunt)
        self.ui.actionEnregistrer_Tous_2.triggered.connect(self.enregistrerEtudiant)
        self.ui.actionEnregistrer_Tous_2.triggered.connect(self.enregistrerLivre)
        self.ui.actionEnregistrer_Tous_2.triggered.connect(self.enregistrerEmprunt)



    def showDialog(self,str,bool):
        msgBox = QMessageBox()
        if bool==False:
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(str)
            msgBox.setWindowTitle("Msg Error")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setDetailedText("Il Faut Récuperer Les Données Pour Pouvoire Continuer")
            msgBox.exec()
         
    #les fct pour ouvrir les fenetres
    def ajoute(self) :
        if(self.done==False):
            self.showDialog("Il faut faire le chargement",False)
        else:
            self.Ajouter=Ajouter_etudiant(self.bib)

    def supprime(self) :
        if(self.done==False):
            self.showDialog("Il faut faire le chargement",False)
        else:
            self.Supprimer=Supprimer_etudiant(self.bib)

    def modifier(self) :
        if(self.done==False):
            self.showDialog("Il faut faire le chargement",False)
        else:
            self.Modifier=Modifier_etudiant(self.bib)

    def affiche(self) :
        if(self.done==False):
            self.showDialog("Il faut faire le chargement",False)
        else:
            self.Modifier=Afficher_etudiant(self.bib)

    def ajout_livre(self) :
        if(self.done==False):
            self.showDialog("Il faut faire le chargement",False)
        else:
            self.Ajouter=Ajouter_livre(self.bib)
    def modif_livre(self) :
        if(self.done==False):
            self.showDialog("Il faut faire le chargement",False)
        else:
            self.Modifier=Modifier_livre(self.bib)
    def supp_livre(self) :
        if(self.done==False):
            self.showDialog("Il faut faire le chargement",False)
        else:
            self.Supprimer=Supprimer_livre(self.bib)

    def recherche_affiche(self) :
        if(self.done==False):
            self.showDialog("Il faut faire le chargement",False)
        else:
            self.Afficher=Afficher_livre(self.bib)

    def ajout_emprunt(self) :
        if(self.done==False):
            self.showDialoúg("Il faut faire le chargement",False)
        else:
            self.Ajouter=Ajouter_emprunt(self.bib)
    def retour_emp(self) :
        if(self.done==False):
            self.showDialog("Il faut faire le chargement",False)
        else:
            self.Retouner=Retour_emprunt(self.bib)
    def modif_emp(self) :
        if(self.done==False):
            self.showDialog("Il faut faire le chargement",False)
        else:
            self.Retouner=Modifier_emprunt(self.bib)
    def supp_emp(self) :
        if(self.done==False):
            self.showDialog("Il faut faire le chargement",False)
        else:
            self.Supprimer=Supprimer_emprunt(self.bib)
    def afficher_emprunt(self) :
        if(self.done==False):
            self.showDialog("Il faut faire le chargement",False)
        else:
            self.Retouner=Afficher_emprunt(self.bib)

    # Etudiants :
    def parseStudent(self,line):
        lis=line.split(";")
        lis[8]=lis[8].replace("\n","")
        return Etudiant(lis[0],lis[1],lis[2],lis[3],lis[4],lis[5],lis[6],lis[7],lis[8])   
    def enregistrerEtudiant(self):
        if(self.done==False):
            self.showDialog("Il n'y a pas des données à enregistrer",False)
        else:
            F=open("./Save/saveEtudiant.csv","w+")
            F.seek(0)
            F.write("Numero d'inscription,Nom,Prenom,Date de naissance,Adresse,Mail,Telephone,Section,Niveau d'etude\n")
            for i in self.bib.etudiants:
                F.write(i.num_insc+";"+i.nom+";"+i.prenom+";"+i.date+";"+i.addresse+";"+i.mail+";"+i.phone+";"+i.section+";"+i.niv_etude+"\n")          
            F.close()
    def recupererEtudiant(self):
        self.done=True
        self.bib.etudiants.clear()
        F=open("./save/SaveEtudiant.csv","r")
        count=-1
        for line in F:
            count+=1
            if(count==0):
                continue
            self.bib.etudiants.append(self.parseStudent(line))      
        F.close()

    # Livres :
    def parseLivre(self,line):
        lis=line.split(";")
        lis[4]=lis[4].replace("\n","")
        return Livre(lis[0],lis[1],lis[2],lis[3],lis[4])   
    def enregistrerLivre(self):
        if(self.done==False):
            return
        else:
            F=open("./Save/saveLivre.csv","w+")
            F.seek(0)
            F.write("Reférence,Titre,Nom,Date,Nombre D'Exemplaire\n")
            for i in self.bib.livres:
                F.write(i.reference+";"+i.titre+";"+i.nom+";"+i.date+";"+i.nbr+"\n")      
            F.close()

    def recupererLivre(self):
        self.done=True
        self.bib.livres.clear()
        F=open("./save/saveLivre.csv","r")
        count=-1
        for line in F:
            count+=1
            if(count==0):
                continue
            self.bib.livres.append(self.parseLivre(line))
        F.close()

    # Emprunts :
    def parseEmprunt(self,line):
        lis=line.split(";")
        lis[3]=lis[3].replace("\n","")
        return Emprunt(lis[0],lis[1],lis[2],lis[3])   
    def enregistrerEmprunt(self):
        if(self.done==False):
            return
        else:
            F=open("./Save/saveEmprunt.csv","w+")
            F.seek(0)
            F.write("Reférence,Numero d'inscription,Date D'Emprunt,Date De Retour\n")
            for i in self.bib.emprunts:
                F.write(i.reference+";"+i.num_insc+";"+i.date_debut+";"+i.date_fin+"\n")      
            F.close()
    def recupererEmprunt(self):
        self.done=True
        self.bib.emprunts.clear()
        F=open("./save/saveEmprunt.csv","r")
        count=-1
        for line in F:
            count+=1
            if(count==0):
                continue
            self.bib.emprunts.append(self.parseEmprunt(line))
        F.close()



if __name__ == '__main__' :
    app=QApplication(sys.argv)
    ui=MainUI()
    app.exec_()


    
