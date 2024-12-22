def afffiche_num_insc(dic,num) :
    for key,value in dic.items() :
        print(key,value)

def afffiche_section(dic,sec) :
    for key,value in dic.items() :
        for i in value :
            if i==sec :
                print(key,value)

def afffiche_niveau(dic,niv) :
    for key,value in dic.items() :
        for i in value :
            if i==niv :
                print(key,value)

def afffiche_num_insc_et_section(dic,num,sec) :
    l=[]
    for key,k in dic.items():
        if key==num :
            for j in k:
                if j==sec :
                    l+=[key]
    if l!=[]:
        for i in l:
            print(key,dic[key])
    else :
        return False

def afffiche_num_insc_et_niveau(dic,num,niv) :
    l=[]
    for key,k in dic.items():
        if key==num :
            for j in k:
                if j==niv :
                    l+=[key]
    if l!=[]:
        for i in l:
            print(key,dic[key])
    else :
        return False
    
def afffiche_section_et_niveau(dic,sec,niv) :
    l=[]
    for key,k in dic.items():
        for i in k:
            if i==sec:
                for j in k:
                    if j==niv :
                        l+=[key]
    if l!=[]:
        for i in l:
            print(key,dic[key])
    else :
        return False
    
def afffiche_num_insc_et_section_et_niveau(dic,num,sec,niv) :
    l=[]
    for key,value in dic.items():
        for i in value:
            if i==num:
                for j in value:
                    if j==sec :
                        for k in value:
                            if k==niv :
                                l+=[key]
    if l!=[]:
        for i in l:
            print(key,dic[key])
    else :
        return False
