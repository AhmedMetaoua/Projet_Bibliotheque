class Etudiant :
    def __init__(self,num_insc,nom,prenom,date,addresse,mail,phone,section,niv_etude) -> None:
        self.num_insc=num_insc
        self.nom=nom
        self.prenom=prenom
        self.date=date
        self.addresse=addresse
        self.mail=mail
        self.phone=phone
        self.section=section
        self.niv_etude=niv_etude
        
    def __str__(self) -> str:
        return str(self.num_insc)+self.prenom+self.nom