from afficher_livre import Ui_Form as aff_liv 
from PyQt5.QtWidgets import *
from class_livre import Livre
from PyQt5.QtCore import Qt
import datetime
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.columns=["Num","reférence","Titre","Nom Auteur","Année D'Edition","Nombre D'Exemplaire"]
        
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
        return 6


class Afficher_livre :
    def __init__(self,bib) -> None:
        self.window = QWidget()
        self.ui = aff_liv()
        self.ui.setupUi(self.window)
        self.window.show()
        self.bib=bib

        self.ui.pushButton_2.clicked.connect(self.affiche_tous)
        self.ui.pushButton.clicked.connect(self.affiche)
        

    def affiche(self) :

        reference=self.ui.reference.text()
        titre=self.ui.titre.text()
        nom=self.ui.nom.text()

        date = str(self.ui.dateEdit.date())[19:-1]
        #date_obj = datetime.datetime.strptime(date_str, "%Y, %m, %d")
        #date = date_obj.strftime("%Y-%m-%d") #2000-01-01
        
        alternative=[]
        i=1
    
        if len(reference)==3 and reference[0].isalpha() and titre!="" and  date!="9999, 12, 31" and nom!="":
            for livre in self.bib.livres:
                if livre.reference==reference and livre.titre==titre and livre.nom==nom and livre.date==date :
                    alternative.append([i,livre.reference,livre.titre,livre.nom,livre.date,livre.nbr])
                    i+=1

        elif  len(reference)==3 and reference[0].isalpha() and titre=="" and nom=="" and  date=="9999, 12, 31" :
            for livre in self.bib.livres:
                if livre.reference==reference :
                    alternative.append([i,livre.reference,livre.titre,livre.nom,livre.date,livre.nbr])
                    i+=1
        elif  reference=="" and titre!="" and nom=="" and  date=="9999, 12, 31" :
            for livre in self.bib.livres:
                if  livre.titre==titre :
                    alternative.append([i,livre.reference,livre.titre,livre.nom,livre.date,livre.nbr])
                    i+=1
        elif reference=="" and titre==""  and nom!="" and  date=="9999, 12, 31":
            for livre in self.bib.livres:
                if  livre.nom==nom :
                    alternative.append([i,livre.reference,livre.titre,livre.nom,livre.date,livre.nbr])
                    i+=1
        elif reference=="" and titre=="" and nom=="" and date!="9999, 12, 31":
            for livre in self.bib.livres:
                if  livre.date==date :
                    alternative.append([i,livre.reference,livre.titre,livre.nom,livre.date,livre.nbr])
                    i+=1
        elif len(reference)==3 and reference[0].isalpha() and titre!="" and nom=="" and  date=="9999, 12, 31" :
            for livre in self.bib.livres:
                if livre.reference!=reference and livre.titre==titre :
                    alternative.append([i,livre.reference,livre.titre,livre.nom,livre.date,livre.nbr])
                    i+=1
        elif len(reference)==3 and reference[0].isalpha() and titre=="" and nom!="" and  date=="9999, 12, 31" :
            for livre in self.bib.livres:
                if livre.reference!=reference and livre.nom==nom :
                    alternative.append([i,livre.reference,livre.titre,livre.nom,livre.date,livre.nbr])
                    i+=1
        elif len(reference)==3 and reference[0].isalpha() and titre=="" and nom=="" and  date!="9999, 12, 31" :
            for livre in self.bib.livres:
                if livre.reference==reference and livre.date==date :
                    alternative.append([i,livre.reference,livre.titre,livre.nom,livre.date,livre.nbr])
                    i+=1
        elif len(reference)==3 and reference[0].isalpha() and titre!=""  and nom!="" and  date=="9999, 12, 31":
            for livre in self.bib.livres:
                if livre.reference==reference and livre.titre==titre and livre.nom==nom :
                    alternative.append([i,livre.reference,livre.titre,livre.nom,livre.date,livre.nbr])
                    i+=1
        elif len(reference)==3 and reference[0].isalpha() and titre!=""  and nom=="" and  date!="9999, 12, 31":
            for livre in self.bib.livres:
                if livre.reference==reference and livre.titre==titre and livre.date==date :
                    alternative.append([i,livre.reference,livre.titre,livre.nom,livre.date,livre.nbr])
                    i+=1
        elif len(reference)==3 and reference[0].isalpha() and titre==""  and nom!="" and  date!="9999, 12, 31":
            for livre in self.bib.livres:
                if livre.reference==reference and livre.nom==nom and livre.date==date :
                    alternative.append([i,livre.reference,livre.titre,livre.nom,livre.date,livre.nbr])
                    i+=1
        elif reference=="" and titre!="" and nom!="" and  date=="9999, 12, 31":
            for livre in self.bib.livres:
                if  livre.titre==titre and livre.nom==nom :
                    alternative.append([i,livre.reference,livre.titre,livre.nom,livre.date,livre.nbr])
                    i+=1
        elif reference=="" and titre!="" and nom=="" and  date!="9999, 12, 31":
            for livre in self.bib.livres:
                if  livre.titre==titre and livre.date==date :
                    alternative.append([i,livre.reference,livre.titre,livre.nom,livre.date,livre.nbr])
                    i+=1
        elif reference=="" and titre!="" and nom!="" and  date!="9999, 12, 31":
            for livre in self.bib.livres:
                if  livre.titre==titre and livre.nom==nom and livre.date==date :
                    alternative.append([i,livre.reference,livre.titre,livre.nom,livre.date,livre.nbr])
                    i+=1
        elif reference=="" and titre=="" and nom!="" and  date!="9999, 12, 31":
            for livre in self.bib.livres:
                if  livre.nom==nom and livre.date==date :
                    alternative.append([i,livre.reference,livre.titre,livre.nom,livre.date,livre.nbr])
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


    def affiche_tous(self) :
        alternative=[]
        i=1
        for livre in self.bib.livres:
            alternative.append([i,livre.reference,livre.titre,livre.nom,livre.date,livre.nbr])
            i+=1

        alternative=sorted(alternative, key=lambda x: x[2],reverse=True)

        self.modal=TableModel(alternative)
        
        self.ui.tableView.setModel(self.modal)
        self.horizontal_header = self.ui.tableView.horizontalHeader()
        self.horizontal_header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)