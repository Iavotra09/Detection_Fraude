import random
import math

def genererGrapheAleatoire(n, p):
    graphe = {i: set() for i in range(n)}  #set est un ensemble d'éléments uniques, donc élimine les multi-arrêtes

    for u in range(n):
        for v in range(u+1, n):  #pour avoir une graphe non orientée et sans boucle
            if random.random() < p:
                graphe[u].add(v)
                graphe[v].add(u)

    return graphe

def rendreConnexe(graphe, n):
    sommetVisites = set()
    communautes = []

    for sommet in range(n):
        if sommet not in sommetVisites:  #parcours en largeur pour voir si le graphe est découpé en plusieurs morceaux
            communauteActuelle = set()
            file = [sommet]
            sommetVisites.add(sommet)

            while file:
                noeud = file.pop(0) #on sort le premier élément de la file
                communauteActuelle.add(noeud)
                for voisin in graphe[noeud]:  #on regarde ces voisin et on les ajoute à la communauté, et on les marques comme sommets déja visités aussi
                    if voisin not in sommetVisites:
                        sommetVisites.add(voisin)
                        file.append(voisin)
            communautes.append(list(communauteActuelle))

    if len(communautes) > 1: #si il existe plusieurs communautés, réparer la connexité
        for i in range(len(communautes) - 1):
        u = communautes[i][0]    #prendre chaque premier sommet de deux communautés et les relier
        v = communautes[i+1][0]
        graphe[u].add(v)
        graphe[v].add(u)

    return graphe

def obtenirMatriceAdjacence(graphe, n):
    matrice = [[0]*n for _ in range(n)]  #créer une matrice n*n remplie de 0
    
    for u in range(n):
        for voisin in graphe[u]:
            matrice[u][voisin] = 1
            
    return matrice