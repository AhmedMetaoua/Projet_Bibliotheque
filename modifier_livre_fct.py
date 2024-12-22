from modifier_livre import Ui_Form as modif_liv
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from class_livre import Livre


class Modifier_livre :
    def __init__(self,bib) -> None:
        self.window = QWidget()
        self.ui = modif_liv()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.pushButton_2.clicked.connect(self.verifier)
        self.ui.pushButton.clicked.connect(self.modifier)
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

    def verifier(self) :
        reference=self.ui.reference.text()
        livre=self.bib.recherche_liv(reference)
        if livre!=None :
            self.ui.message_f.setText("")
            self.ui.message_v.setText("Trouver")
            self.ui.nbr.setText(livre.nbr)
        else :
            self.ui.message_v.setText("")
            self.ui.nbr.setText("")
            self.ui.message_f.setText("Non Trouver")
        

    def modifier(self) :
        reference=self.ui.reference.text()
        nbr=self.ui.nbr.text()

        if ( self.bib.recherche_liv(reference)==None or nbr=="") :
            self.ui.message_3.setText("Erreur!!")
            self.showDialog2("Verifier La Reference Ou Verifier Le Nombre Donner !")
        else :
            self.bib.modifier_livre(reference,nbr)
            self.ui.message_v.setText("Done")
            self.ui.message_3.setText("")
            print(self.bib.livres)
            self.showDialog("Livre Modifier Avec Succés")
