from retour_emprunt import Ui_Form as retour_emp
from PyQt5.QtWidgets import *
from class_emprunt import Emprunt
from class_livre import Livre
from PyQt5.QtWidgets import QMessageBox
from datetime import date

class Retour_emprunt :
    def __init__(self,bib) -> None:
        self.window = QWidget()
        self.ui = retour_emp()
        self.ui.setupUi(self.window)
        self.window.show()

        self.ui.pushButton.clicked.connect(self.retourne)
        self.bib=bib

    def showDialog(self,str):
        msgBox = QMessageBox()

        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(str)
        msgBox.setWindowTitle("Msg Validation")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
    def showDialog2(self,str):
        msgBox = QMessageBox()

        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(str)
        msgBox.setWindowTitle("Msg Erreur")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()


    def verif_reference(self,reference):
        if len(reference)==3 and reference[0].isalpha() and reference[1:].isdigit():
            return True
        return False

    def retourne(self) :
        num_insc=self.ui.num_insc.text()
        reference=self.ui.reference.text()

        if ( len(num_insc)!=6 ) :
            self.ui.label_2.setText("*")
            self.ui.label_4.setText("")
            self.showDialog2("Verifier Le Numero D'Inscription")
        elif (self.verif_reference(reference)==False) :
            self.ui.label_2.setText("")
            self.ui.label_4.setText("")
            self.ui.label_6.setText("*")
            self.showDialog2("Verifier La Reference De Livre")
        elif (self.bib.recherche_emp1(num_insc,reference)!=None) :
            self.ui.label_2.setText("")
            self.ui.label_4.setText("")
            self.ui.label_6.setText("")
            self.bib.retourner_emprunt(num_insc,str(date.today()))  # date ==> aaaa-mm-dd
            print(self.bib.emprunts)
            self.showDialog("Emprunt Retourner Avec Succés")
        else :
            self.ui.label_2.setText("")
            self.ui.label_6.setText("")
            self.ui.label_4.setText("Emprunt Non Trouver")
            self.showDialog2("Emprunt Non Existante")
        