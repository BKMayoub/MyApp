ID=[]
nom=[]
modul=[]
anner=[]
prix=[]
def entrer():
    i=int(input("-ID : "))
    n=input("-nom de voiture : ")
    m=input("-module de voiture : ")
    y=int(input("-anner : "))
    p=int(input("-prix : "))
    print()
    print("------------------------------------")
    ID.append(i)
    nom.append(n)
    modul.append(m)
    anner.append(y)
    prix.append(p)
    print(f"""    -ID : {ID}
    -nom de voiture : {nom}
    -module de voiture : {modul}
    -anner : {anner}
    -prix : {prix}
          """)
def menu():
    print("----------------------------------")
    print("1- Ajouter une voiture")
    print("2- supprimer une voiture")
    print("3- afficher les voitures")
    print("4- modifier une voiture")
    print("5- quitter")
    choix=int(input("Entrez votre choix : "))
    if choix > 5 or choix < 1:
        print("choix invalide")
        return menu()
    return choix
def ajouter():
    entrer()
def afficher():
    for i in range(len(ID)):
        print(f" voiture : {ID[i]} - {nom[i]} - {modul[i]} - {anner[i]} - {prix[i]}")
def supprimer():
    i=int(input("entrer id de voiture a sipprimer : "))
    id.pop(i-1)
    nom.pop(i-1)
    modul.pop(i-1)
    anner.pop(i-1)
    prix.pop(i-1)
def modifier():
    i=int(input("entrer ID de voiture a modifier : "))
    q=input("voulez vous modifier (nom/modul/anner/prix)")
    if q == "nom":
        nom[i-1]=input("entrer nouveau nom : ")
    elif q== "modul":
        modul[i-1]=input("entrer nouveau modul : ")
    elif q == "anner":
        anner[i-1]=int(input("entrer nouveau anner : "))
    else:
        prix[i-1]=int(input("entrer nouveau prix : "))
while True :
    choix=menu()
    if choix==1:
        ajouter()
    elif choix ==2:
        supprimer()
    elif choix ==3:
        afficher()
    elif choix==4:
        modifier()
    else:
        break