# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Menu_principale.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuGestion_Des_Etudiants = QtWidgets.QMenu(self.menubar)
        self.menuGestion_Des_Etudiants.setObjectName("menuGestion_Des_Etudiants")
        self.menuMise_A_Jour_Des_Etudiants = QtWidgets.QMenu(self.menuGestion_Des_Etudiants)
        self.menuMise_A_Jour_Des_Etudiants.setObjectName("menuMise_A_Jour_Des_Etudiants")
        self.menuCherche_Affichage_Trie = QtWidgets.QMenu(self.menuGestion_Des_Etudiants)
        self.menuCherche_Affichage_Trie.setObjectName("menuCherche_Affichage_Trie")
        self.menuGestion_Des_Livres = QtWidgets.QMenu(self.menubar)
        self.menuGestion_Des_Livres.setObjectName("menuGestion_Des_Livres")
        self.menuGestion_Des_Emprunts = QtWidgets.QMenu(self.menubar)
        self.menuGestion_Des_Emprunts.setObjectName("menuGestion_Des_Emprunts")
        self.menuEnregistrement_et_Recuperation = QtWidgets.QMenu(self.menubar)
        self.menuEnregistrement_et_Recuperation.setObjectName("menuEnregistrement_et_Recuperation")
        self.menuEnregistrement = QtWidgets.QMenu(self.menuEnregistrement_et_Recuperation)
        self.menuEnregistrement.setObjectName("menuEnregistrement")
        self.menuRecuperation = QtWidgets.QMenu(self.menuEnregistrement_et_Recuperation)
        self.menuRecuperation.setObjectName("menuRecuperation")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAjouter_Un_Etudiant = QtWidgets.QAction(MainWindow)
        self.actionAjouter_Un_Etudiant.setObjectName("actionAjouter_Un_Etudiant")
        self.actionSupprimer_Un_Etudiant = QtWidgets.QAction(MainWindow)
        self.actionSupprimer_Un_Etudiant.setObjectName("actionSupprimer_Un_Etudiant")
        self.actionChareche = QtWidgets.QAction(MainWindow)
        self.actionChareche.setObjectName("actionChareche")
        self.actionAffiche = QtWidgets.QAction(MainWindow)
        self.actionAffiche.setObjectName("actionAffiche")
        self.actionModifier_Etudiant = QtWidgets.QAction(MainWindow)
        self.actionModifier_Etudiant.setObjectName("actionModifier_Etudiant")
        self.actionMise_A_Jour = QtWidgets.QAction(MainWindow)
        self.actionMise_A_Jour.setObjectName("actionMise_A_Jour")
        self.actionRecherche_Affichage = QtWidgets.QAction(MainWindow)
        self.actionRecherche_Affichage.setObjectName("actionRecherche_Affichage")
        self.actionMise_Ajour = QtWidgets.QAction(MainWindow)
        self.actionMise_Ajour.setObjectName("actionMise_Ajour")
        self.actionRecherche_Affichage_2 = QtWidgets.QAction(MainWindow)
        self.actionRecherche_Affichage_2.setObjectName("actionRecherche_Affichage_2")
        self.actionEnregistrer_Tous_2 = QtWidgets.QAction(MainWindow)
        self.actionEnregistrer_Tous_2.setObjectName("actionEnregistrer_Tous_2")
        self.actionRecuperer_Tous = QtWidgets.QAction(MainWindow)
        self.actionRecuperer_Tous.setObjectName("actionRecuperer_Tous")
        self.actionEnregistrement_Des_Etudiants = QtWidgets.QAction(MainWindow)
        self.actionEnregistrement_Des_Etudiants.setObjectName("actionEnregistrement_Des_Etudiants")
        self.actionEnregistrement_Des_Livres = QtWidgets.QAction(MainWindow)
        self.actionEnregistrement_Des_Livres.setObjectName("actionEnregistrement_Des_Livres")
        self.actionEnregistrement_Des_Emprunts = QtWidgets.QAction(MainWindow)
        self.actionEnregistrement_Des_Emprunts.setObjectName("actionEnregistrement_Des_Emprunts")
        self.actionRecuperation_Des_Etudiants = QtWidgets.QAction(MainWindow)
        self.actionRecuperation_Des_Etudiants.setObjectName("actionRecuperation_Des_Etudiants")
        self.actionRecuperation_Des_Livres = QtWidgets.QAction(MainWindow)
        self.actionRecuperation_Des_Livres.setObjectName("actionRecuperation_Des_Livres")
        self.actionRecuperation_Des_Emprunts = QtWidgets.QAction(MainWindow)
        self.actionRecuperation_Des_Emprunts.setObjectName("actionRecuperation_Des_Emprunts")
        self.menuMise_A_Jour_Des_Etudiants.addSeparator()
        self.menuMise_A_Jour_Des_Etudiants.addAction(self.actionAjouter_Un_Etudiant)
        self.menuMise_A_Jour_Des_Etudiants.addSeparator()
        self.menuMise_A_Jour_Des_Etudiants.addAction(self.actionSupprimer_Un_Etudiant)
        self.menuMise_A_Jour_Des_Etudiants.addSeparator()
        self.menuMise_A_Jour_Des_Etudiants.addAction(self.actionModifier_Etudiant)
        self.menuCherche_Affichage_Trie.addAction(self.actionChareche)
        self.menuCherche_Affichage_Trie.addSeparator()
        self.menuCherche_Affichage_Trie.addAction(self.actionAffiche)
        self.menuGestion_Des_Etudiants.addAction(self.menuMise_A_Jour_Des_Etudiants.menuAction())
        self.menuGestion_Des_Etudiants.addSeparator()
        self.menuGestion_Des_Etudiants.addAction(self.menuCherche_Affichage_Trie.menuAction())
        self.menuGestion_Des_Livres.addAction(self.actionMise_A_Jour)
        self.menuGestion_Des_Livres.addSeparator()
        self.menuGestion_Des_Livres.addAction(self.actionRecherche_Affichage)
        self.menuGestion_Des_Emprunts.addAction(self.actionMise_Ajour)
        self.menuGestion_Des_Emprunts.addSeparator()
        self.menuGestion_Des_Emprunts.addAction(self.actionRecherche_Affichage_2)
        self.menuEnregistrement.addAction(self.actionEnregistrement_Des_Etudiants)
        self.menuEnregistrement.addSeparator()
        self.menuEnregistrement.addAction(self.actionEnregistrement_Des_Livres)
        self.menuEnregistrement.addSeparator()
        self.menuEnregistrement.addAction(self.actionEnregistrement_Des_Emprunts)
        self.menuRecuperation.addAction(self.actionRecuperation_Des_Etudiants)
        self.menuRecuperation.addSeparator()
        self.menuRecuperation.addAction(self.actionRecuperation_Des_Livres)
        self.menuRecuperation.addSeparator()
        self.menuRecuperation.addAction(self.actionRecuperation_Des_Emprunts)
        self.menuEnregistrement_et_Recuperation.addAction(self.menuEnregistrement.menuAction())
        self.menuEnregistrement_et_Recuperation.addSeparator()
        self.menuEnregistrement_et_Recuperation.addSeparator()
        self.menuEnregistrement_et_Recuperation.addAction(self.actionEnregistrer_Tous_2)
        self.menuEnregistrement_et_Recuperation.addSeparator()
        self.menuEnregistrement_et_Recuperation.addAction(self.menuRecuperation.menuAction())
        self.menuEnregistrement_et_Recuperation.addSeparator()
        self.menuEnregistrement_et_Recuperation.addAction(self.actionRecuperer_Tous)
        self.menuEnregistrement_et_Recuperation.addSeparator()
        self.menubar.addAction(self.menuGestion_Des_Etudiants.menuAction())
        self.menubar.addAction(self.menuGestion_Des_Livres.menuAction())
        self.menubar.addAction(self.menuGestion_Des_Emprunts.menuAction())
        self.menubar.addAction(self.menuEnregistrement_et_Recuperation.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuGestion_Des_Etudiants.setTitle(_translate("MainWindow", "Gestion Des Etudiants"))
        self.menuMise_A_Jour_Des_Etudiants.setTitle(_translate("MainWindow", "Mise A Jour Des Etudiants"))
        self.menuCherche_Affichage_Trie.setTitle(_translate("MainWindow", "Cherche , Affichage ,Trie"))
        self.menuGestion_Des_Livres.setTitle(_translate("MainWindow", "Gestion Des Livres"))
        self.menuGestion_Des_Emprunts.setTitle(_translate("MainWindow", "Gestion Des Emprunts"))
        self.menuEnregistrement_et_Recuperation.setTitle(_translate("MainWindow", "Enregistrement et Recuperation"))
        self.menuEnregistrement.setTitle(_translate("MainWindow", "Enregistrement"))
        self.menuRecuperation.setTitle(_translate("MainWindow", "Recuperation"))
        self.actionAjouter_Un_Etudiant.setText(_translate("MainWindow", "Ajouter Etudiant"))
        self.actionSupprimer_Un_Etudiant.setText(_translate("MainWindow", "Supprimer Etudiant"))
        self.actionChareche.setText(_translate("MainWindow", "Recherche"))
        self.actionAffiche.setText(_translate("MainWindow", "Affiche"))
        self.actionModifier_Etudiant.setText(_translate("MainWindow", "Modifier Etudiant"))
        self.actionMise_A_Jour.setText(_translate("MainWindow", "Mise A Jour "))
        self.actionRecherche_Affichage.setText(_translate("MainWindow", "Recherche , Affichage"))
        self.actionMise_Ajour.setText(_translate("MainWindow", "Mise Ajour"))
        self.actionRecherche_Affichage_2.setText(_translate("MainWindow", "Recherche , Affichage"))
        self.actionEnregistrer_Tous_2.setText(_translate("MainWindow", "Enregistrer Tous"))
        self.actionRecuperer_Tous.setText(_translate("MainWindow", "Recuperer Tous"))
        self.actionEnregistrement_Des_Etudiants.setText(_translate("MainWindow", "Enregistrement Des Etudiants"))
        self.actionEnregistrement_Des_Livres.setText(_translate("MainWindow", "Enregistrement Des Livres "))
        self.actionEnregistrement_Des_Emprunts.setText(_translate("MainWindow", "Enregistrement Des Emprunts"))
        self.actionRecuperation_Des_Etudiants.setText(_translate("MainWindow", "Recuperation Des Etudiants"))
        self.actionRecuperation_Des_Livres.setText(_translate("MainWindow", "Recuperation Des Livres"))
        self.actionRecuperation_Des_Emprunts.setText(_translate("MainWindow", "Recuperation Des Emprunts"))