from afficher_emprunt import Ui_Form as aff_emp
from PyQt5.QtWidgets import *
from class_etudiant import Etudiant
from PyQt5.QtCore import Qt
import datetime
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.columns=["Num","Reférence","Numero d'inscription","Date D'Emprunt","Date De Retour"]
        
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
        return 5


class Afficher_emprunt :
    def __init__(self,bib) -> None:
        self.window = QWidget()
        self.ui = aff_emp()
        self.ui.setupUi(self.window)
        self.window.show()
        self.bib=bib

        self.ui.pushButton_2.clicked.connect(self.affiche_tous)
        self.ui.pushButton.clicked.connect(self.affiche)
        

    def affiche(self) :

        reference=self.ui.reference.text()
        num_insc=self.ui.num_insc.text()

        date_str = str(self.ui.dateEdit.date())[19:-1]
        date_obj = datetime.datetime.strptime(date_str, "%Y, %m, %d")
        date_emp = date_obj.strftime("%Y-%m-%d")

        date_str_2 = str(self.ui.dateEdit_2.date())[19:-1]
        date_obj_2 = datetime.datetime.strptime(date_str_2, "%Y, %m, %d")
        date_retour = date_obj_2.strftime("%Y-%m-%d")


        alternative=[]
        i=1
        
        if len(reference)==3 and reference[0].isalpha() and len(num_insc)==6 and  date_emp!="9999-12-31" and date_retour!="9999-12-31":
            for emprunt in self.bib.emprunts:
                if emprunt.num_insc==num_insc and  emprunt.reference!=reference and emprunt.date_debut>=date_emp and emprunt.date_fin!="0" and emprunt.date_fin<=date_retour:
                    alternative.append([i,emprunt.reference,emprunt.num_insc,emprunt.date_debut,emprunt.date_fin])
                    i+=1

        elif len(reference)==3 and reference[0].isalpha() and num_insc=="" and  date_emp=="9999-12-31" and date_retour=="9999-12-31":
            for emprunt in self.bib.emprunts:
                if  emprunt.reference==reference :
                    alternative.append([i,emprunt.reference,emprunt.num_insc,emprunt.date_debut,emprunt.date_fin])
                    i+=1
        elif  reference==""  and len(num_insc)==6 and  date_emp=="9999-12-31" and date_retour=="9999-12-31":
            for emprunt in self.bib.emprunts:
                if emprunt.num_insc==num_insc :
                    alternative.append([i,emprunt.reference,emprunt.num_insc,emprunt.date_debut,emprunt.date_fin])
                    i+=1
        elif reference=="" and num_insc=="" and  date_emp!="9999-12-31" and date_retour=="9999-12-31":
            for emprunt in self.bib.emprunts:
                if  emprunt.date_debut==date_emp :
                    alternative.append([i,emprunt.reference,emprunt.num_insc,emprunt.date_debut,emprunt.date_fin])
                    i+=1
        elif reference=="" and num_insc=="" and  date_emp=="9999-12-31" and date_retour!="9999-12-31":
            for emprunt in self.bib.emprunts:
                if  emprunt.date_fin==date_retour :
                    alternative.append([i,emprunt.reference,emprunt.num_insc,emprunt.date_debut,emprunt.date_fin])
                    i+=1
        elif len(reference)==3 and reference[0].isalpha() and len(num_insc)==6 and  date_emp=="9999-12-31" and date_retour=="9999-12-31":
            for emprunt in self.bib.emprunts:
                if emprunt.num_insc==num_insc and  emprunt.reference==reference :
                    alternative.append([i,emprunt.reference,emprunt.num_insc,emprunt.date_debut,emprunt.date_fin])
                    i+=1
        elif len(reference)==3 and reference[0].isalpha() and num_insc=="" and  date_emp!="9999-12-31" and date_retour=="9999-12-31":
            for emprunt in self.bib.emprunts:
                if  emprunt.reference==reference and emprunt.date_debut==date_emp :
                    alternative.append([i,emprunt.reference,emprunt.num_insc,emprunt.date_debut,emprunt.date_fin])
                    i+=1
        elif len(reference)==3 and reference[0].isalpha() and num_insc=="" and  date_emp=="9999-12-31" and date_retour!="9999-12-31":
            for emprunt in self.bib.emprunts:
                if  emprunt.reference==reference and  emprunt.date_fin==date_retour:
                    alternative.append([i,emprunt.reference,emprunt.num_insc,emprunt.date_debut,emprunt.date_fin])
                    i+=1
        elif len(reference)==3 and reference[0].isalpha() and num_insc=="" and  date_emp!="9999-12-31" and date_retour!="9999-12-31":
            for emprunt in self.bib.emprunts:
                if  emprunt.reference==reference and emprunt.date_debut>=date_emp and emprunt.date_fin<=date_retour and emprunt.date_fin!="0":
                    alternative.append([i,emprunt.reference,emprunt.num_insc,emprunt.date_debut,emprunt.date_fin])
                    i+=1
        elif len(reference)==3 and reference[0].isalpha() and len(num_insc)==6 and  date_emp!="9999-12-31" and date_retour=="9999-12-31":
            for emprunt in self.bib.emprunts:
                if emprunt.num_insc==num_insc and  emprunt.reference==reference and emprunt.date_debut==date_emp :
                    alternative.append([i,emprunt.reference,emprunt.num_insc,emprunt.date_debut,emprunt.date_fin])
                    i+=1
        elif len(reference)==3 and reference[0].isalpha() and len(num_insc)==6 and  date_emp=="9999-12-31" and date_retour!="9999-12-31":
            for emprunt in self.bib.emprunts:
                if emprunt.num_insc==num_insc and  emprunt.reference==reference and emprunt.date_fin==date_retour :
                    alternative.append([i,emprunt.reference,emprunt.num_insc,emprunt.date_debut,emprunt.date_fin])
                    i+=1
        elif len(reference)==3 and reference[0].isalpha() and len(num_insc)==6 and  date_emp!="9999-12-31" and date_retour!="9999-12-31":
            for emprunt in self.bib.emprunts:
                if emprunt.num_insc==num_insc and  emprunt.reference==reference and emprunt.date_fin<=date_retour and emprunt.debut>=date_emp and date_retour!="0":
                    alternative.append([i,emprunt.reference,emprunt.num_insc,emprunt.date_debut,emprunt.date_fin])
                    i+=1
        elif reference=="" and len(num_insc)==6 and  date_emp!="9999-12-31" and date_retour=="9999-12-31":
            for emprunt in self.bib.emprunts:
                if emprunt.num_insc==num_insc and  emprunt.date_debut==date_emp :
                    alternative.append([i,emprunt.reference,emprunt.num_insc,emprunt.date_debut,emprunt.date_fin])
                    i+=1
        elif reference=="" and len(num_insc)==6 and  date_emp=="9999-12-31" and date_retour!="9999-12-31":
            for emprunt in self.bib.emprunts:
                if emprunt.num_insc==num_insc and  emprunt.date_fin==date_retour :
                    alternative.append([i,emprunt.reference,emprunt.num_insc,emprunt.date_debut,emprunt.date_fin])
                    i+=1
        elif reference=="" and len(num_insc)==6 and  date_emp!="9999-12-31" and date_retour!="9999-12-31":
            for emprunt in self.bib.emprunts:
                if emprunt.num_insc==num_insc and  emprunt.date_debut>=date_emp and  emprunt.date_fin<=date_retour and emprunt.date_fin!="0":
                    alternative.append([i,emprunt.reference,emprunt.num_insc,emprunt.date_debut,emprunt.date_fin])
                    i+=1
        elif reference=="" and num_insc=="" and  date_emp!="9999-12-31" and date_retour!="9999-12-31":
            for emprunt in self.bib.emprunts:
                if  emprunt.date_debut>=date_emp and  emprunt.date_fin<=date_retour and emprunt.date_fin!="0":
                    alternative.append([i,emprunt.reference,emprunt.num_insc,emprunt.date_debut,emprunt.date_fin])
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


    def affiche_tous(self) :
        alternative=[]
        i=1
        for emprunt in self.bib.emprunts:
            alternative.append([i,emprunt.reference,emprunt.num_insc,emprunt.date_debut,emprunt.date_fin])
            i+=1
        self.modal=TableModel(alternative)
        
        self.ui.tableView.setModel(self.modal)
        self.horizontal_header = self.ui.tableView.horizontalHeader()
        self.horizontal_header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
