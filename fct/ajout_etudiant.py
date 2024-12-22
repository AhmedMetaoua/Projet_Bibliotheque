#  dic={ 'key1':liste1 , 'key2':liste2 , 'key3':liste3 , 'num_insc':['nom','prenom','date','adresse','mail',phone,'section',niveau'] }

def existe(d,x):
    for k in d.keys():
        if k==x:
            return True
    return False

def remplir_dic():
    dic={}    
    while True:
        num_insc=input("Saisit le Num d'inscription :")
        if(existe(dic,num_insc)==True):
            print("le Num Existe deja !")
            continue
        nom=input("Saisit le Nom : ")
        prenom=input("Saisit le Prenom :")
        date=input("Saisit la Date de Naissance : ")
        addresse=input("Saisit l'adresse : ")
        mail=input("Saisit le mail :")
        phone=int(input("Saisit le Num de Telephone : "))
        section=input("Saisie La Section :")
        niv_etude=input("Saisie Le Niveau D'Etude :")
        dic[num_insc]=[nom,prenom,date,addresse,mail,phone,section,niv_etude]
        while True:
            rep=input("Voulez-vous Ajoutez une Voiture (Y/N) : ")
            if (rep=='Y' or rep=='N' or rep=='y' or rep=='n'):
                break
        if rep=='N' or rep=='n':
            break
    return dic