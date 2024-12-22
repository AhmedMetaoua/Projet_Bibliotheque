from ajouter_etudiant import Ui_Form as ajout_etud
from PyQt5.QtWidgets import *
from class_etudiant import Etudiant
from PyQt5.QtWidgets import QMessageBox
import re


class Ajouter_etudiant :
    def __init__(self,bib) -> None:
        self.window = QWidget()
        self.ui = ajout_etud()
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

    def verif_nom(self,name):
        if 3<=len(name)<=20 and name.isalpha():
            return True
        return False
    def verif_adresse(self,adress):
        if 3<len(adress)<50:
            return True
        return False
    def verif_mail(self,email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex,email)):   
            return True
        return False
    

    def ajout(self) :
        num_insc=self.ui.num_insc.text()
        nom=self.ui.nom.text()
        prenom=self.ui.prenom.text()
        date=str(self.ui.dateEdit.date())[19:-1]
        addresse=self.ui.adresse.text()
        mail=self.ui.mail.text()
        phone=self.ui.phone.text()
        section=self.ui.section.currentText()
        niv_etude=self.ui.niveau.currentText()
        self.ui.label_11.setText("")

        if ( len(num_insc)!=6 ):
            self.ui.label_11.setText("*")
        else :
            self.ui.label_11.setText("")
        if (nom=="" or self.verif_nom(nom)==False ) :
            self.ui.label_12.setText("*")
        else :
            self.ui.label_12.setText("")
        if (prenom=="" or self.verif_nom(prenom)==False) :
            self.ui.label_13.setText("*")
        else :
            self.ui.label_13.setText("")
        if (date=="") :
            self.ui.label_14.setText("*")
        else :
            self.ui.label_14.setText("")
        if (addresse=="" or self.verif_adresse(addresse)==False ) :
            self.ui.label_15.setText("*")
        else :
            self.ui.label_15.setText("")
        if (mail=="" or self.verif_mail(mail)==False ) :
            self.ui.label_16.setText("*")
        else :
            self.ui.label_16.setText("")
        if (len(phone)!=8) :
            self.ui.label_17.setText("*")
        else :
            self.ui.label_17.setText("")
        if (section=="None") :
            self.ui.label_18.setText("*")
        else :
            self.ui.label_18.setText("")
        if (niv_etude=="None") :
            self.ui.label_19.setText("*")
        else :
            self.ui.label_19.setText("")

        if (( len(str(num_insc))!=6 or nom=="" or self.verif_nom(nom)==False or prenom=="" or self.verif_nom(prenom)==False or addresse=="" or self.verif_adresse(addresse)==False  or mail=="" or self.verif_mail(mail)==False or len(str(phone))!=8 or section=="None" or niv_etude=="None")) :
            #erreur
            self.showDialog2("Il Faut Remplir Toutes Les Cases")
            self.ui.label_11.setText("erreur")
        elif (self.bib.recherche(num_insc)!=None) :
            self.ui.label_11.setText("Deja Existe")
            self.showDialog2("Numero D'inscrit Deja Existe")
        else :
            self.ui.label_11.setText("")
            new_etudiant=Etudiant(num_insc,nom,prenom,date,addresse,mail,phone,section,niv_etude)
            self.bib.ajouter_etudiant(new_etudiant)
            print(self.bib.etudiants)
            self.showDialog("Ajout D'un Etudiant Avec Succés")