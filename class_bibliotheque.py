from PyQt5 import QtCore, QtGui, QtWidgets

class Bibliotheque :
    def __init__(self) -> None:
        self.etudiants=[]
        self.livres=[]
        self.emprunts=[]

    #gestion Etudiant
    def ajouter_etudiant(self,e) :
        self.etudiants.append(e)

    def supprimer_tous_etud(self) :    
        self.etudiants=[]
    def supprimer_etudiant(self,num_insc,nom,prenom,section,niv_etude) :
        if (num_insc!="" and nom=="" and prenom=="" and section=="None" and niv_etude=="None" ) :
            self.etudiants=[e for e in self.etudiants if e.num_insc!=num_insc]
        if (num_insc=="" and nom!="" and prenom=="" and section=="None" and niv_etude=="None" ) :
            self.etudiants=[e for e in self.etudiants if e.nom!=nom]
        if (num_insc=="" and nom=="" and prenom!="" and section=="None" and niv_etude=="None" ) :
            self.etudiants=[e for e in self.etudiants if e.prenom!=prenom]
        if (num_insc=="" and nom=="" and prenom=="" and section!="None" and niv_etude=="None" ) :
            self.etudiants=[e for e in self.etudiants if e.section!=section]
        if (num_insc=="" and nom=="" and prenom=="" and section=="None" and niv_etude!="None" ) :
            self.etudiants=[e for e in self.etudiants if e.niv_etude!=niv_etude]

        if (num_insc!="" and nom!="" and prenom=="" and section=="None" and niv_etude=="None" ) :
            self.etudiants=[e for e in self.etudiants if e.num_insc!=num_insc and e.nom!=nom]
        if (num_insc!="" and nom=="" and prenom!="" and section=="None" and niv_etude=="None" ) :
            self.etudiants=[e for e in self.etudiants if e.num_insc!=num_insc and e.prenom!=prenom]
        if (num_insc!="" and nom!="" and prenom!="" and section=="None" and niv_etude=="None" ) :
            self.etudiants=[e for e in self.etudiants if e.num_insc!=num_insc and e.prenom!=prenom and e.nom!=nom]
        if (num_insc!="" and nom!="" and prenom!="" and section!="None" and niv_etude=="None" ) :
            self.etudiants=[e for e in self.etudiants if e.section!=section and e.prenom!=prenom and e.nom!=nom]
        if (num_insc!="" and nom!="" and prenom!="" and section=="None" and niv_etude!="None" ) :
            self.etudiants=[e for e in self.etudiants if e.niv_etude!=niv_etude and e.prenom!=prenom and e.nom!=nom]   
        if (num_insc!="" and nom!="" and prenom!="" and section!="None" and niv_etude!="None" ) :
            self.etudiants=[e for e in self.etudiants if e.niv_etude!=niv_etude and e.prenom!=prenom and e.nom!=nom and e.section!=section]
        if (num_insc!="" and nom=="" and prenom=="" and section!="None" and niv_etude=="None" ) :
            self.etudiants=[e for e in self.etudiants if e.num_insc!=num_insc and e.section!=section]
        if (num_insc!="" and nom=="" and prenom=="" and section=="None" and niv_etude!="None" ) :
            self.etudiants=[e for e in self.etudiants if e.num_insc!=num_insc and e.niv_etude!=niv_etude]

        if (num_insc=="" and nom!="" and prenom!="" and section=="None" and niv_etude=="None" ) :
            self.etudiants=[e for e in self.etudiants if e.prenom!=prenom and e.nom!=nom]
        if (num_insc=="" and nom!="" and prenom!="" and section!="None" and niv_etude=="None" ) :
            self.etudiants=[e for e in self.etudiants if e.section!=section and e.prenom!=prenom and e.nom!=nom]
        if (num_insc=="" and nom!="" and prenom!="" and section=="None" and niv_etude!="None" ) :
            self.etudiants=[e for e in self.etudiants if e.niv_etude!=niv_etude and e.prenom!=prenom and e.nom!=nom]
        if (num_insc=="" and nom!="" and prenom!="" and section!="None" and niv_etude!="None" ) :
            self.etudiants=[e for e in self.etudiants if e.niv_etude!=niv_etude and e.prenom!=prenom and e.nom!=nom and e.section!=section]

        if (num_insc=="" and nom=="" and prenom=="" and section!="None" and niv_etude!="None" ) :
            self.etudiants=[e for e in self.etudiants if e.niv_etude!=niv_etude and e.section!=section]
        if (num_insc!="" and nom!="" and prenom!="" and section!="None" and niv_etude!="None" ) :
            self.etudiants=[e for e in self.etudiants if e.niv_etude!=niv_etude and prenom!=prenom and nom!=nom and e.section!=section and e.num_insc!=num_insc]


    def recherche(self,num_insc) :
        for e in self.etudiants :
            if e.num_insc==num_insc:
                return e
        return None

    def modifier_etudiant(self,num_insc,addresse,mail,phone) :
        for e in self.etudiants :
            if e.num_insc==num_insc :
                if addresse!="" :
                    e.addresse=addresse
                if mail!="" :
                    e.mail=mail
                if len(phone)==8 :
                    e.phone=phone


    def ajouter_livre(self,l) :
        self.livres.append(l)
        
    def recherche_liv(self,reference) :
        for l in self.livres :
            if l.reference==reference:
                return l
        return None
    def modifier_livre(self,reference,nbr) :
        for l in self.livres :
            if l.reference==reference :
                if nbr!="" :
                    l.nbr=nbr
    def supprimer_tous_liv(self) :    
        self.livres=[]
    def supprimer_livre(self,reference,titre,nom,date) :

        if (reference!="" and nom=="" and titre=="" and date=="2000, 1, 1" ) :  #
            self.livres=[l for l in self.livres if l.reference!=reference]
        if (reference!="" and nom!="" and titre=="" and date=="2000, 1, 1" ) :  #
            self.livres=[l for l in self.livres if l.nom!=nom and l.reference!=reference]
        if (reference!="" and nom=="" and titre!="" and date=="2000, 1, 1" ) :  #
            self.livres=[l for l in self.livres if l.reference!=reference and l.titre!=titre]
        if (reference!="" and nom=="" and titre=="" and date!="2000, 1, 1" ) :  #
            self.livres=[l for l in self.livres if l.reference!=reference and l.date!=date]
        
        if (reference=="" and nom!="" and titre=="" and date=="2000, 1, 1" ) :  #
            self.livres=[l for l in self.livres if l.nom!=nom]
        if (reference=="" and nom=="" and titre!="" and date=="2000, 1, 1" ) :  #
            self.livres=[l for l in self.livres if l.titre!=titre]
        if (reference=="" and nom=="" and titre=="" and date!="2000, 1, 1" ) :  #
            self.livres=[l for l in self.livres if l.date!=date]

        if (reference=="" and nom!="" and titre!="" and date=="2000, 1, 1" ) :  #
            self.livres=[l for l in self.livres if l.nom!=nom and l.titre!=titre]
        if (reference=="" and nom!="" and titre=="" and date!="2000, 1, 1" ) :  #
            self.livres=[l for l in self.livres if l.nom!=nom and l.date!=date]
        if (reference=="" and nom!="" and titre!="" and date!="2000, 1, 1" ) :  #
            self.livres=[l for l in self.livres if l.nom!=nom and l.date!=date and l.titre!=titre] 
        if (reference=="" and nom=="" and titre!="" and date!="2000, 1, 1" ) :  #
            self.livres=[l for l in self.livres if l.date!=date and l.titre!=titre]       


    def recherche_emp1(self,num_insc,reference) :
        for e in self.emprunts :
            if e.reference==reference and e.num_insc==num_insc and e.date_fin=='0':
                return e
        return None
    def ajouter_emprunt(self,e) :
        self.emprunts.append(e)
        for l in self.livres :
            if l.reference==e.reference :
                l.nbr=str(int(l.nbr)-1)

    def recherche_emp(self,num_insc) :
        for e in self.emprunts :
            if e.num_insc==num_insc:
                if e.date_fin=='0':
                    return e
                else :
                    return None
        return None
    def retourner_emprunt(self,num_insc,date) :
        for e in self.emprunts :
            if e.num_insc==num_insc :
                e.date_fin=date
                reference=e.reference
        for l in self.livres :
            if l.reference==reference :
                l.nbr=str(int(l.nbr)+1)

    def recherche_emp2(self,num_insc,reference) :
        for e in self.emprunts :
            if e.reference==reference and e.num_insc==num_insc and e.date_fin!='0':
                return e
        return None
    
    def supprimer_emprunt_ref_insc(self,reference,num_insc) :
        self.emprunts=[e for e in self.emprunts if e.reference!=reference and e.num_insc!=num_insc]
    def supprimer_emprunt_ref(self,reference) :
        self.emprunts=[e for e in self.emprunts if e.reference!=reference]
    def supprimer_emprunt_insc(self,num_insc) :
        self.emprunts=[e for e in self.emprunts if e.num_insc!=num_insc]
    def supprimer_tous_emp(self) :
        self.emprunts=[]

    def etudiant(self) :
        return self.etudiants
    def load_data(self) :
        etud=[]
        for e in self.etudiants :
            l=[]
            l.append(e.num_insc)
            l.append(e.nom)
            l.append(e.prenom)
            l.append(e.date)
            l.append(e.addresse)
            l.append(e.mail)
            l.append(e.phone)
            l.append(e.section)
            l.append(e.niv_etude)
            etud.append(l)
        
        row=0
        self.tableWidget.setRowCount(len(etud))
        for person in etud :
            for i in range (len(etud[0])) :
                self.tableWidget.setItem(row,i,QtWidgets.QTableWidgetItem(person[0][i]))
            row+=1




        
        
                        

            