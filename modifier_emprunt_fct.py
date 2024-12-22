from modifier_emprunt import Ui_Form as modif_emp
from PyQt5.QtWidgets import *
from class_emprunt import Emprunt
from class_livre import Livre
from datetime import date
from PyQt5.QtWidgets import QMessageBox
import datetime

class Modifier_emprunt :
    def __init__(self,bib) -> None:
        self.window = QWidget()
        self.ui = modif_emp()
        self.ui.setupUi(self.window)
        self.window.show()

        self.ui.pushButton.clicked.connect(self.modifier)
        self.ui.pushButton_2.clicked.connect(self.verifier)

        self.bib=bib


    def verif_reference(self,reference):
        if len(reference)==3 and reference[0].isalpha() and reference[1:].isdigit():
            return True
        return False
    
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
        num_insc=self.ui.num_insc.text()
        emprunt=self.bib.recherche_emp2(num_insc,reference)

        if ( reference=="" ) :
            self.ui.label_4.setText("*")
            self.ui.label_6.setText("")
        elif  len(num_insc)!=6 :
            self.ui.label_5.setText("*")
            self.ui.label_4.setText("")
            self.ui.label_6.setText("")
        elif emprunt!=None :
            self.ui.label_5.setText("")
            self.ui.label_4.setText("")
            self.ui.label_6.setText("")
            self.ui.label_12.setText("Trouver")
            self.ui.label_13.setText("")
            self.ui.label_9.setText("")
            self.ui.label_11.setText(emprunt.date_debut)
            self.ui.label_10.setText(emprunt.date_fin)
        else :
            self.ui.label_5.setText("")
            self.ui.label_4.setText("")
            self.ui.label_11.setText("")
            self.ui.label_10.setText("")
            self.ui.label_12.setText("")
            self.ui.label_9.setText("")
            self.ui.label_13.setText("Emprunt Non Trouver")
            self.ui.label_6.setText("")

    def modifier(self) :
        reference=self.ui.reference.text()
        num_insc=self.ui.num_insc.text()

        date_str = str(self.ui.dateEdit.date())[19:-1]
        date_obj = datetime.datetime.strptime(date_str, "%Y, %m, %d")
        date_debut = date_obj.strftime("%Y-%m-%d")

        date_str_2 = str(self.ui.dateEdit_2.date())[19:-1]
        date_obj_2 = datetime.datetime.strptime(date_str_2, "%Y, %m, %d")
        date_fin = date_obj_2.strftime("%Y-%m-%d")

        emprunt=self.bib.recherche_emp2(num_insc,reference)

        if ( self.verif_reference(reference)==False ) :
            self.ui.label_4.setText("*")
            self.ui.label_6.setText("")
            self.showDialog2("Verifier La Reference")
        elif  (len(num_insc)!=6) :
            self.ui.label_5.setText("*")
            self.ui.label_4.setText("")
            self.ui.label_6.setText("")
            self.showDialog2("Verifier Le Numero D'Inscription")
        elif emprunt!=None :
            self.ui.label_5.setText("")
            self.ui.label_4.setText("")
            self.ui.label_6.setText("")

            if date_debut!="2000-01-01":
                emprunt.date_debut=date_debut
            if date_fin!="2000-01-01" :
                emprunt.date_fin=date_fin
            
            self.ui.label_9.setText("Done")
            self.ui.label_13.setText("")
            print(self.bib.emprunts)
            self.showDialog("Emprunt Modifier Avec Succés")
        else :
            self.ui.label_5.setText("")
            self.ui.label_4.setText("")
            self.ui.label_9.setText("")
            self.ui.label_6.setText("Emprunt Non Trouver/Terminer")
            self.showDialog2("Emprunt Non Existante/Terminer")

            