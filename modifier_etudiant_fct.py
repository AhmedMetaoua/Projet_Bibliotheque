from modifier_etudiant import Ui_Form as modif
from PyQt5.QtWidgets import *
from class_etudiant import Etudiant
from PyQt5.QtWidgets import QMessageBox
import re

class Modifier_etudiant :
    def __init__(self,bib) -> None:
        self.window = QWidget()
        self.ui = modif()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.verife.clicked.connect(self.verifier)
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
        msgBox.setWindowTitle("Msg Validation")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    def verif_mail(self,email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex,email)):   
            return True
        return False


    def verifier(self) :
        self.ui.message_3.setText("")
        num_insc=str(self.ui.num_insc.text())
        etudiant=self.bib.recherche(num_insc)
        if len(num_insc)==6 :
            self.ui.label_3.setText("")
            if etudiant != None:
                self.ui.message_f.setText("")
                self.ui.message_v.setText("Trouver")
                self.ui.adresse.setText(etudiant.addresse)
                self.ui.phone.setText(etudiant.phone)
                self.ui.mail.setText(etudiant.mail)
            else :
                self.ui.adresse.setText("")
                self.ui.phone.setText("")
                self.ui.mail.setText("")
                self.ui.message_v.setText("")
                self.ui.message_f.setText("Non Trouver")
        else :
            self.ui.label_3.setText("*") 
            self.ui.message_f.setText("")
            self.ui.message_v.setText("")
            self.ui.message_3.setText("Erreur!!")
            self.showDialog2("Verifier Le Numero D'Inscription")

    def modifier(self) :
        num_insc=self.ui.num_insc.text()
        addresse=self.ui.adresse.text()
        mail=self.ui.mail.text()
        phone=self.ui.phone.text()
        if (self.ui.message_v.text()=="" and self.ui.message_f.text()=="Non Trouver" or (addresse=="" or (mail=="" or self.verif_mail(mail)==False) or len(phone)!=8 )) :
            self.ui.message_3.setText("Erreur!!")
            self.ui.adresse.setText("")
            self.ui.phone.setText("")
            self.ui.mail.setText("")
            self.showDialog2("Verifier Toutes Les Cases")
        else :
            self.bib.modifier_etudiant(num_insc,addresse,mail,phone)
            self.ui.message_3.setText("")
            self.ui.message_v.setText("Done")
            print(self.bib.etudiants)
            self.showDialog("Etudiant Modifier Avec Succés")
