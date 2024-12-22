from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
import sys
from Menu_principale import Ui_MainWindow 



class MainUI:
    def __init__(self) :
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

        self.ui.actionAjouter_Un_Etudiant.triggered.connect(self.ajoute)
        self.ui.actionSupprimer_Un_Etudiant.triggered.connect(self.supprime)
        self.ui.actionModifier_Etudiant.triggered.connect(self.modifier)
        self.ui.actionCherche.triggered.connect(self.recherche)
        self.ui.actionAffiche.triggered.connect(self.affiche)
        self.ui.actionAjouter_Nouveau_Livre.triggered.connect(self.ajout_livre)
        self.ui.actionSupprimer_Un_Livre.triggered.connect(self.supp_livre)
        self.ui.actionModifier_Nbr_D_Exemplaires.triggered.connect(self.modif_exemplaire)
        self.ui.actionRecherche_Affichage.triggered.connect(self.cherche_affiche)

    def ajoute(self) :
        print("ajouter un Etudiant")

    def supprime(self) :
        print("supprimer un Etudiant")
    def modifier(self) :
        print("modifier un Etudiant")
    def recherche(self) :
        print("rechercher un Etudiant")
    def affiche(self) :
        print("afficher un Etudiant")
    def ajout_livre(self) :
        print("ajouter un Livre")
    def supp_livre(self) :
        print("supprimer un Livre")
    def modif_exemplaire(self) :
        print("modifier un Livre")
    def cherche_affiche(self) :
        print("cherche et affiche un Livre")




if __name__ == '__main__' :
    app=QApplication(sys.argv)
    ui=MainUI()
    app.exec_()




    
