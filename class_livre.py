class Livre :
    def __init__(self,reference,titre,nom,date,nbr) -> None:
        self.reference=reference
        self.titre=titre
        self.nom=nom
        self.date=date
        self.nbr=nbr
        
    def __str__(self) -> str:
        return str(self.reference)+self.titre
    

    
    