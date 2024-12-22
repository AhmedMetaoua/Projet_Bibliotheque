#5 est la position de numero de telephone dans la liste
def modif_phone(dic,id,num) : 
    for key,val in dic.items():
        if key==id:
            val.pop(5)
            val.insert(5,num)
            break

#4 est la position de mail dans la liste
def modif_mail(dic,id,mail) :
    for key,val in dic.items():
        if key==id:
            val.pop(4)
            val.insert(4,mail)
            break

#3 est la position de adresse dans la liste
def modif_mail(dic,id,adresse) :
    for key,val in dic.items():
        if key==id:
            val.pop(4)
            val.insert(4,adresse)
            break
