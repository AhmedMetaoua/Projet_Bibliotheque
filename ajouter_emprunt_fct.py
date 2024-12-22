from ajouter_emprunt import Ui_Form as ajout_emp
from PyQt5.QtWidgets import *
from class_emprunt import Emprunt
from class_livre import Livre
from PyQt5.QtWidgets import QMessageBox
from datetime import date

class Ajouter_emprunt :
    def __init__(self,bib) -> None:
        
        self.window = QWidget()
        self.ui = ajout_emp()
        self.ui.setupUi(self.window)
        self.window.show()

        self.ui.pushButton.clicked.connect(self.ajout)
        self.bib=bib


    def showDialog(self,str):
        msgBox = QMessageBox()

        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(str)
        msgBox.setWindowTitle("Msg Validation")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
    def showDialog1(self,str):
        msgBox = QMessageBox()

        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(str)
        msgBox.setWindowTitle("Msg Erreur")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    
    def ajout(self) :
        num_insc=self.ui.num_insc.text()
        reference=self.ui.reference.text()
        livre=self.bib.recherche_liv(reference)
        if livre :
            nbr=livre.nbr
            if ( len(str(num_insc))!=6 ) :
                self.ui.label_11.setText("Invalide")
                self.ui.label_4.setText("*")
                self.showDialog1("Verifier Le Numero D'Inscription")
                return 0  # Erreur 
            elif (self.bib.recherche_emp1(num_insc,reference)!=None) :
                self.ui.label_11.setText("Deja Existe")
                self.ui.label_4.setText("")
                self.showDialog("Cette Emprunt Deja Existe !")
            else :
                self.ui.label_4.setText("")
                if (self.bib.recherche(num_insc)!=None):
                    if ( str(nbr) != "0" ) :
                        self.ui.label_11.setText("")
                        new_emprunt=Emprunt(reference,num_insc,str(date.today()),'0') 
                        self.bib.ajouter_emprunt(new_emprunt)
                        self.showDialog("Ajout D'un Emprunt Avec Succés")
                        print(self.bib.emprunts)
                    else : 
                        self.ui.label_11.setText("Stocke Epuisée")
                        self.showDialog1("Stocke Epuisée, Pas D'exemplaire Pour Ce Livre")
                else :
                    self.ui.label_11.setText("Etudiant Non Existant")
                    self.showDialog1("Verifier Le Numero D'Inscription")
        else :
            self.ui.label_11.setText("Livre Non Existant")
            self.showDialog1("Ce Livre N'Existe Pas")
