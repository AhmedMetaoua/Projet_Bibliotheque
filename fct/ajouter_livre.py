#  dic={ 'key1':liste1 , 'key2':liste2 , 'key3':liste3 , 'num_insc':['titre','nom','date',nbr] }


def existe(d,x):
    for k in d.keys():
        if k==x:
            return True
    return False

def remplir_dic():
    dic={}    
    while True:
        reference=input("Saisit le Num d'inscription :")
        if(existe(dic,reference)==True):
            print("le livre Existe deja !")
            continue
        titre=input("Saisit le Titre : ")
        nom=input("Saisit le Nom et le Prenom de L'auteur :")
        date=input("Saisit l'année d'edition': ")
        nbr=int(input("Saisit le nbr d'Examplaire' : "))
        dic[reference]=[titre,nom,date,nbr]
        while True:
            rep=input("Voulez-vous Ajoutez une Voiture (Y/N) : ")
            if (rep=='Y' or rep=='N' or rep=='y' or rep=='n'):
                break
        if rep=='N' or rep=='n':
            break
    return dic


def modifier_livre(dic,ref,nbr) :
    for key,value in dic.items() :
        if key==ref :
            value.pop(3)
            value.insert(3,nbr)


def supprimer_ref (dic,ref) :
    for key,value in dic.items() :
        
