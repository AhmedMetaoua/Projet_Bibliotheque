def supp_num_insc(dic,x) :
    for k in dic.keys():
        if k==x:
            dic.pop(k)
            break

def supp_nom_ou_prenom(dic,x) :
    l=[]
    for key,k in dic.items():
        for i in k:
            if i==x:
                l+=[key]
    if l!=[]:
        for i in l:
            dic.pop(i)
    else :
        return False

def supp_nom_et_prenom(dic,x,y) :
    l=[]
    for key,k in dic.items():
        for i in k:
            if i==x:
                for j in k:
                    if j==y :
                        l+=[key]
    if l!=[]:
        for i in l:
            dic.pop(i)
    else :
        return False

def supp_section_ou_niveau(dic,x) :
    l=[]
    for key,k in dic.items():
        for i in k:
            if i==x:
                l+=[key]
    for i in l:
        dic.pop(i)

def supp_section_et_niveau(dic,x,y) :
    l=[]
    for key,k in dic.items():
        for i in k:
            if i==x:
                for j in k:
                    if j==y :
                        l+=[key]
    if l!=[]:
        for i in l:
            dic.pop(i)
    else :
        return False
        


def supp_tout(dic) :
    dic.clear()