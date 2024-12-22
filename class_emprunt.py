class Emprunt :
    def __init__(self,reference,num_insc,date_debut,date_fin) -> None:
        self.reference=reference
        self.num_insc=num_insc
        self.date_debut=date_debut
        self.date_fin=date_fin
    
    def __str__(self) -> str:
        return str(self.reference)+self.num_insc
    

