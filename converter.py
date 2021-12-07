hexaDictio = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f",
}

def base10to2(n):
    """
    Convertit base 10 en base 2
    """
    assert type(n)==int, "n doit être un nombre entier"
    assert n>=0, "n doit être positif"
    s = ""
    if n==0:
        return "0"
    else:
        while n !=0:
            if n%2 == 0:
                s = "0" + s
                n/=2
            else:
                s = "1" + s
                n = (n-1)/2
        return s

def base2to10(chaine):
    """
    convertit base 2 en base 10
    """
    longueur=len(chaine)
    n=0
    for indice in range(0,longueur):
        n=n+int(chaine[indice])*2**(longueur-(indice+1))
    return n

def base10to16(n):
    """
    convertir de la base 10 en base 16
    """
    s=""
    while n!= 0:
        reste = n%16
        s = hexaDictio[reste] + s
        n = n//16
    return s

def base16to10(n):
    """
    convertir de la base 16 à la base 10
    """
    st=""
    while n!= 0:
        reste = n%16
        s = hexaDictio[reste] + s
        n = n//16
    return s
    
        

def somme(ch1, ch2):
    """
    additione deux nombre binaires
    """
    assert len(ch1) == len(ch2), "les chaînes doivent être de même longueur"
    ch1 = str(ch1)
    ch2 = str(ch2)
    resultat = ""
    retenue = 0
    for i in range (len(ch1)-1, -1, -1):
        if ch1[i] == "0" and ch2[i] == "0":
            if retenue == 1:
                resultat = "1" + resultat
            else:
                resultat = "0" + resultat
            
        if ch1[i] != ch2[i]:
            if retenue == 0:
                resultat = "1" + resultat
            else:
                resultat = "0" + resultat

        if ch1[i] == "1" and ch2[i] == "1":
            resultat = str(retenue) + resultat
            retenue = 1
    if retenue == 1:
        resultat = "1" + resultat
hexaDictio = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f",
}

def base10to2(n):
    """
    Convertit base 10 en base 2
    """
    assert type(n)==int, "n doit être un nombre entier"
    assert n>=0, "n doit être positif"
    s = ""
    if n==0:
        return "0"
    else:
        while n !=0:
            if n%2 == 0:
                s = "0" + s
                n/=2
            else:
                s = "1" + s
                n = (n-1)/2
        return s

def base2to10(chaine):
    """
    convertit base 2 en base 10
    """
    longueur=len(chaine)
    n=0
    for indice in range(0,longueur):
        n=n+int(chaine[indice])*2**(longueur-(indice+1))
    return n

def base10to16(n):
    """
    convertir de la base 10 en base 16
    """
    s=""
    while n!= 0:
        reste = n%16
        s = hexaDictio[reste] + s
        n = n//16
    return s

def base16to10(n):
    """
    convertir de la base 16 à la base 10
    """
    st=""
    HEX="0123456789abcdef"
    n=input()
  
    v=0
    for c in n:
        v *= 16
        v += HEX.find(c)
 
    print(v)
        

def somme(ch1, ch2):
    """
    additione deux nombre binaires
    """
    assert len(ch1) == len(ch2), "les chaînes doivent être de même longueur"
    ch1 = str(ch1)
    ch2 = str(ch2)
    resultat = ""
    retenue = 0
    for i in range (len(ch1)-1, -1, -1):
        if ch1[i] == "0" and ch2[i] == "0":
            if retenue == 1:
                resultat = "1" + resultat
            else:
                resultat = "0" + resultat
            
        if ch1[i] != ch2[i]:
            if retenue == 0:
                resultat = "1" + resultat
            else:
                resultat = "0" + resultat

        if ch1[i] == "1" and ch2[i] == "1":
            resultat = str(retenue) + resultat
            retenue = 1
    if retenue == 1:
        resultat = "1" + resultat
    return resultat



#HEX="0123456789abcdef"
#n= input("nombre ?")
# 
#p=1
#v=0
#while n>0:
#    v+=HEX.find(n[-1])*p
#    p*=16
#    n=n[:-1]
#print(v)