from supprimer_livre import Ui_Form as supp_liv
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from class_livre import Livre


class Supprimer_livre :
    def __init__(self,bib) -> None:
        self.window = QWidget()
        self.ui = supp_liv()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.pushButton.clicked.connect(self.supprimer)
        self.ui.pushButton_2.clicked.connect(self.supprimer_tous)
        self.bib=bib

    def showDialog(self,str):
        msgBox = QMessageBox()

        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText(str)
        msgBox.setWindowTitle("Msg Warning")
        msgBox.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        msgBox.buttonClicked.connect(self.Dialog_button)
        msgBox.exec()
    def showDialog1(self,str):
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

    def Dialog_button(self,i):
        self.sure= i.text()

    def verif_reference(self,reference):
        if len(reference)==3 and reference[0].isalpha() and reference[1:].isdigit():
            return True
        return False

    def supprimer(self) :
        reference=self.ui.reference.text()
        titre=self.ui.titre.text()
        nom=self.ui.nom.text()
        date=str(self.ui.dateEdit.date())[19:-1]  #  2000, 1, 1
        self.ui.label_10.setText("")
        if ( reference=="" or self.verif_reference(reference)==False ):
            self.ui.label_5.setText("*")
        else :
            self.ui.label_5.setText("") 
        if (titre=="") :
            self.ui.label_6.setText("*")
        else :
            self.ui.label_6.setText("")
        if (nom=="") :
            self.ui.label_8.setText("*")
        else :
            self.ui.label_8.setText("")
        if (date=="2000, 1, 1") :
            self.ui.label_9.setText("*")
        else :
            self.ui.label_9.setText("")

        if ( (reference=="" or self.verif_reference(reference)==False) and nom=="" and titre=="") :
            self.showDialog2("Remplir Au Moin Une Casse")
            return 0  # Erreur 
        else :
            self.showDialog("Est-Tu Sure De La Suppression !")
            if self.sure=="&Yes" :
                self.ui.label_5.setText("")
                self.ui.label_6.setText("")
                self.ui.label_8.setText("")
                self.ui.label_9.setText("")
                self.ui.label_10.setText("Done")
                self.bib.supprimer_livre(reference,titre,nom,date)  #date 2000, 1, 1
                self.showDialog1("Suppression Terminer")
                print(self.bib.livres)

    def supprimer_tous(self) :
        self.ui.label_10.setText("")
        self.showDialog("Est-Tu Sure De La Suppression !")
        if self.sure=="&Yes" :
            self.ui.label_5.setText("")
            self.ui.label_6.setText("")
            self.ui.label_8.setText("")
            self.ui.label_9.setText("")
            self.ui.label_10.setText("Done")
            self.bib.supprimer_tous_liv()
            self.showDialog1("Suppression Terminer")
            print(self.bib.livres)

