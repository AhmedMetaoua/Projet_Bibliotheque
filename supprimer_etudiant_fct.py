from supprimer_etudiant import Ui_Form as supp_etud
from PyQt5.QtWidgets import *
from class_etudiant import Etudiant


class Supprimer_etudiant :
    def __init__(self,bib) -> None:
        self.window = QWidget()
        self.ui = supp_etud()
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
    def Dialog_button(self,i):
        self.sure= i.text()

    def showDialog2(self,str):
        msgBox = QMessageBox()

        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(str)
        msgBox.setWindowTitle("Msg Erreur")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
    def showDialog3(self,str):
        msgBox = QMessageBox()

        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(str)
        msgBox.setWindowTitle("Msg VAlidation")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()


    def supprimer(self) :
        num_insc=self.ui.num_insc.text()
        nom=self.ui.nom.text()
        prenom=self.ui.prenom.text()
        section=self.ui.section.currentText()
        niv_etude=self.ui.niveau.currentText()
        if ( len(num_insc)!=6 and nom=="" and prenom=="" and section=="None" and niv_etude=="None") :
            self.ui.label_5.setText("erreur")
            self.showDialog2("Il Faut Remplir Les Cases")
            return 0  # Erreur 
        elif len(str(num_insc))!=6 and nom=="" and prenom=="" and section!="None" and niv_etude=="None":
            self.showDialog("Est-Tu Sure De La Suppression !")
            if self.sure=="&Yes" :
                self.ui.label_5.setText("")
                self.bib.supprimer_etudiant("","","",section,"")
                self.showDialog3("Suppression Terminer")
                print(self.bib.etudiants)
            """
            self.ui.label_5.setText("erreur")
            self.showDialog2("Verifier Le Numero D'inscription")
            """
        elif len(str(num_insc))!=6 and nom=="" and prenom=="" and section=="None" and niv_etude!="None":
            self.showDialog("Est-Tu Sure De La Suppression !")
            if self.sure=="&Yes" :
                self.ui.label_5.setText("")
                self.bib.supprimer_etudiant("","","","",niv_etude)
                self.showDialog3("Suppression Terminer")
                print(self.bib.etudiants)
        elif len(str(num_insc))!=6 and nom=="" and prenom=="" and section!="None" and niv_etude!="None":
            self.showDialog("Est-Tu Sure De La Suppression !")
            if self.sure=="&Yes" :
                self.ui.label_5.setText("")
                self.bib.supprimer_etudiant("","","",section,niv_etude)
                self.showDialog3("Suppression Terminer")
                print(self.bib.etudiants)
        else :
            self.showDialog("Est-Tu Sure De La Suppression !")
            if self.sure=="&Yes" :
                self.ui.label_5.setText("")
                self.bib.supprimer_etudiant(num_insc,nom,prenom,section,niv_etude)
                self.showDialog3("Suppression Terminer")
                print(self.bib.etudiants)

    def supprimer_tous(self) :
        self.showDialog("Est-Tu Sure De La Suppression !")
        if self.sure=="&Yes" :
            self.ui.label_5.setText("")
            self.bib.supprimer_tous_etud()
            self.showDialog3("Suppression Terminer")
            print(self.bib.etudiants)
