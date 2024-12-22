from supprimer_emprunt import Ui_Form as supp_emp
from PyQt5.QtWidgets import *
from class_emprunt import Emprunt
from class_livre import Livre


class Supprimer_emprunt :
    def __init__(self,bib) -> None:
        self.window = QWidget()
        self.ui = supp_emp()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.pushButton.clicked.connect(self.supprimer)
        self.ui.pushButton_2.clicked.connect(self.supprimer_tous)
        self.bib=bib

    def verif_reference(self,reference):
        if len(reference)==3 and reference[0].isalpha() and reference[1:].isdigit():
            return True
        return False
    
    def showDialog1(self,str):
        msgBox = QMessageBox()

        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(str)
        msgBox.setWindowTitle("Msg Erreur")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
    def showDialog2(self,str):
        msgBox = QMessageBox()

        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(str)
        msgBox.setWindowTitle("Msg Erreur")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
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

    def supprimer(self) :
        reference=self.ui.reference.text()
        num_insc=self.ui.num_insc.text()
        if ( self.verif_reference(reference)==False and len(num_insc)!=6):
            self.ui.label_2.setText("*")
            self.ui.label_5.setText("*")
        else :
            self.ui.label_2.setText("") 
            self.ui.label_5.setText("")
            
        if ( reference!="" and len(num_insc)==6 and self.verif_reference(reference) ) :
            self.showDialog("Est-Tu Sure De La Suppression !")
            if self.sure=="&Yes" :
                self.bib.supprimer_emprunt_ref_insc(reference,num_insc)
                self.ui.label_2.setText("")
                self.ui.label_5.setText("")
                self.ui.label_7.setText("Done")
                self.ui.label_6.setText("")
                self.showDialog1("Suppression Terminer")
                print(self.bib.emprunts)
        elif reference!="" and self.verif_reference(reference) and len(num_insc)==0 :
            self.showDialog("Est-Tu Sure De La Suppression !")
            if self.sure=="&Yes" :
                self.bib.supprimer_emprunt_ref(reference)
                self.ui.label_2.setText("")
                self.ui.label_5.setText("")
                self.ui.label_7.setText("Done")
                self.ui.label_6.setText("")
                self.showDialog1("Suppression Terminer")
                print(self.bib.emprunts)
        elif len(num_insc)==6 and  reference=="":
            self.showDialog("Est-Tu Sure De La Suppression !")
            if self.sure=="&Yes" :
                self.bib.supprimer_emprunt_insc(num_insc)
                self.ui.label_2.setText("")
                self.ui.label_5.setText("")
                self.ui.label_7.setText("Done")
                self.ui.label_6.setText("")
                self.showDialog1("Suppression Terminer")
                print(self.bib.emprunts)
        else :
            self.ui.label_6.setText("Erreur")
            self.ui.label_7.setText("")
            self.showDialog2("Verifier Le Num D'inscription Ou La Reference Donner")
            
    def supprimer_tous(self) :
        self.showDialog("Est-Tu Sure De La Suppression !")
        if self.sure=="&Yes" :
            self.ui.label_2.setText("")
            self.ui.label_5.setText("")
            self.ui.label_7.setText("Done")
            self.ui.label_6.setText("")
            self.bib.supprimer_tous_emp()
            self.showDialog1("Suppression Terminer")
            print(self.bib.emprunts)
            

