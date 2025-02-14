import math
def addition(a,b):
    return a+b

def soustraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b==0:
        print("erreur : division par zero.")
    return a/b

def puissance(a,b):
    return a**b

def Racine_carrée(a):
    if a<0:
        print("erreur : racine carrée d'un nombre negatif non autorisée ")
    return math.sqrt(a)

def logarithme(a):
    if a<=0:
        print("erreur: logarithm d'un nombre negatif ou nul non défini.")
    return math.log10(a)

def factorial(a):
    if a<0:
        print("erreur: factorial d'un nombre negatif")
    return math.factorial(a)

def calculatrice():
    print("Bienvenue dans la caculatrice.")
    print("chosissez une opperation.")
    print("1-addition.")
    print("2-sustraction.")
    print("3-multiplication.")
    print("4-division.")
    print("5-puissance.")
    print("6-racine carrée.")
    print("7-logarithm.")
    print("8-factorial.")
    print("8-quité.")
    
    choix=input("entrez votre choix: ")

    if choix in ['1','2','3','4','5']:
        a =float(input("Entrez la premier nombre : "))
        b =float(input("Entrez la deuxième nombre : "))
        if choix=="1":
            print("résultat :",addition(a,b))
        elif choix=="2":
            print("résultat :",soustraction(a,b))
        elif choix=="3":
            print("résultat :",multiplication(a,b))
        elif choix=="4":
            print("résultat :",division(a,b))
        elif choix=="5":
            print("résultat :",puissance(a,b))
    elif choix in ['6','7','8','9']:
        a =float(input("Entrez un nombre : "))
        if choix=="6":
            print("résultat :",Racine_carrée(a))
        elif choix=="7":
            a=int(a)
            print("résultat :",factorial(a))
        elif choix=="8":
            print("résultat :",logarithme(a))

    else:
        print("erreur:choix invalide.")

calculatrice()
