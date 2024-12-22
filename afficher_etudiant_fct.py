from afficher_etudiant import Ui_Form as aff_etud
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from PyQt5 import QtCore, QtGui, QtWidgets


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.columns=["Num","N inscription","Nom","Prénom","Date de Naissance","Adresse","Mail","Telephone","Section","Niveau"]
        

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.columns[section])
    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]
    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return 10


class Afficher_etudiant :
    def __init__(self,bib) -> None:
        self.window = QWidget()
        self.ui = aff_etud()
        self.ui.setupUi(self.window)
        self.window.show()
        self.bib=bib

        self.ui.pushButton_2.clicked.connect(self.affiche_tous)
        self.ui.pushButton.clicked.connect(self.affiche)
        self.ui.pushButton_3.clicked.connect(self.affiche_ord)

    def affiche(self) :

        num_insc=self.ui.num_insc.text()
        section=self.ui.section.currentText()
        niv_etude=self.ui.niveau.currentText()
        
        alternative=[]
        i=1
        
        if len(num_insc)==6 and num_insc.isdigit() and  section!="None" and niv_etude!="None":
            for etudiant in self.bib.etudiants:
                if etudiant.num_insc==num_insc and  etudiant.section==section and etudiant.niv_etude==niv_etude:
                    alternative.append([i,etudiant.num_insc,etudiant.nom,etudiant.prenom,etudiant.date,etudiant.addresse,etudiant.mail,etudiant.phone,etudiant.section,etudiant.niv_etude])
                    i+=1
        elif len(num_insc)==6 and num_insc.isdigit() and  section=="None" and niv_etude=="None" :
            for etudiant in self.bib.etudiants:
                if etudiant.num_insc==num_insc : 
                    alternative.append([i,etudiant.num_insc,etudiant.nom,etudiant.prenom,etudiant.date,etudiant.addresse,etudiant.mail,etudiant.phone,etudiant.section,etudiant.niv_etude])
                    i+=1
        elif len(num_insc)==6 and num_insc.isdigit() and  section!="None" and niv_etude=="None" :
            for etudiant in self.bib.etudiants:
                if etudiant.num_insc==num_insc and  etudiant.section==section : 
                    alternative.append([i,etudiant.num_insc,etudiant.nom,etudiant.prenom,etudiant.date,etudiant.addresse,etudiant.mail,etudiant.phone,etudiant.section,etudiant.niv_etude])
                    i+=1
        elif len(num_insc)==6 and num_insc.isdigit() and  section=="None" and niv_etude!="None" :
            for etudiant in self.bib.etudiants:
                if etudiant.num_insc==num_insc and  etudiant.niv_etude==niv_etude : 
                    alternative.append([i,etudiant.num_insc,etudiant.nom,etudiant.prenom,etudiant.date,etudiant.addresse,etudiant.mail,etudiant.phone,etudiant.section,etudiant.niv_etude])
                    i+=1
        elif num_insc==""  and  section!="None" and niv_etude=="None" :
            for etudiant in self.bib.etudiants:
                if  etudiant.section==section : 
                    alternative.append([i,etudiant.num_insc,etudiant.nom,etudiant.prenom,etudiant.date,etudiant.addresse,etudiant.mail,etudiant.phone,etudiant.section,etudiant.niv_etude])
                    i+=1
        elif num_insc=="" and  section!="None" and niv_etude!="None" :
            for etudiant in self.bib.etudiants:
                if  etudiant.section==section and  etudiant.niv_etude==niv_etude : 
                    alternative.append([i,etudiant.num_insc,etudiant.nom,etudiant.prenom,etudiant.date,etudiant.addresse,etudiant.mail,etudiant.phone,etudiant.section,etudiant.niv_etude])
                    i+=1
        elif num_insc=="" and  section=="None" and niv_etude!="None" :
            for etudiant in self.bib.etudiants:
                if  etudiant.niv_etude==niv_etude : 
                    alternative.append([i,etudiant.num_insc,etudiant.nom,etudiant.prenom,etudiant.date,etudiant.addresse,etudiant.mail,etudiant.phone,etudiant.section,etudiant.niv_etude])
                    i+=1
        else :
            alternative=[]

        self.modal=TableModel(alternative)
        
        self.ui.tableView.setModel(self.modal)
        self.horizontal_header = self.ui.tableView.horizontalHeader()
        self.horizontal_header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(9, QtWidgets.QHeaderView.ResizeToContents)
        



    def affiche_tous(self) :
        alternative=[]
        i=1
        for etudiant in self.bib.etudiants:
            alternative.append([i,etudiant.num_insc,etudiant.nom,etudiant.prenom,etudiant.date,etudiant.addresse,etudiant.mail,etudiant.phone,etudiant.section,etudiant.niv_etude])
            i+=1
        self.modal=TableModel(alternative)  # il remplie automatiquement le tableau avec la liste des etudiants de 'alternative'
        
        self.ui.tableView.setModel(self.modal)
        self.horizontal_header = self.ui.tableView.horizontalHeader()
        self.horizontal_header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(9, QtWidgets.QHeaderView.ResizeToContents)


    def affiche_ord(self) :
        alternative=[]
        i=0
        for etudiant in self.bib.etudiants:
            alternative.append([i,etudiant.num_insc,etudiant.nom,etudiant.prenom,etudiant.date,etudiant.addresse,etudiant.mail,etudiant.phone,etudiant.section,etudiant.niv_etude])
            i+=1

        alternative=sorted(alternative, key=lambda x: x[2],reverse=False)
        self.modal=TableModel(alternative)
        
        self.ui.tableView.setModel(self.modal)
        self.horizontal_header = self.ui.tableView.horizontalHeader()
        self.horizontal_header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(9, QtWidgets.QHeaderView.ResizeToContents)
    
