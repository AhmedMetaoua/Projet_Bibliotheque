from ajouter_livre import Ui_Form as ajout_liv
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from class_livre import Livre


class Ajouter_livre :
    def __init__(self,bib) -> None:
        self.window = QWidget()
        self.ui = ajout_liv()
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
    def verif_nom(self,name):
        if 3<=len(name)<=20 and name.isalpha():
            return True
        return False
    
    def ajout(self) :
        reference=self.ui.reference.text()  #[A-Z]99
        titre=self.ui.titre.text()
        nom=self.ui.nom.text()
        date=str(self.ui.dateEdit.date())[19:-1]
        nbr=self.ui.nbr.text()
        if ( reference=="" or self.verif_reference(reference)==False ) :
            self.ui.label_5.setText("*")
        else :
            self.ui.label_5.setText("")
        if ( titre=="" or self.verif_nom(titre)==False ) :
            self.ui.label_6.setText("*")
        else :
            self.ui.label_6.setText("")
        if ( nom=="" or self.verif_nom(nom)==False ) :
            self.ui.label_9.setText("*")
        else :
            self.ui.label_9.setText("")
        if ( nbr=="" ) :
            self.ui.label_11.setText("*")
        else :
            self.ui.label_11.setText("")

        if (reference=="" or self.verif_reference(reference)==False or self.verif_nom(titre)==False or self.verif_nom(nom)==False or date=="" or nbr=="") :
            self.showDialog2("Verifier Toutes Les Cases")
            return 0 #erreur
        elif (self.bib.recherche_liv(reference)!=None) :
            self.ui.label_5.setText("Deja Existe")
        else :
            self.ui.label_5.setText("")
            new_livre=Livre(reference,titre,nom,date,nbr)
            self.bib.ajouter_livre(new_livre)
            print(self.bib.livres)
            self.showDialog("Ajout D'un Livre Avec Succés")
            
