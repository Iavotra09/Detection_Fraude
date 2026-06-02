from coloration import colorierGraphe

def rechercheClique(sommet, clique, candidats, graphe, cliquesMaximales, carteCouleurs):
    if not candidats:
        if len(clique) >= 3:
            cliqueValide = sorted(list(clique))
            if cliqueValide not in cliquesMaximales:
                cliquesMaximales.append(cliqueValide)
        return

    couleursRestantes = {carteCouleurs[c] for c in candidats}  #étalage par coloration
    if len(clique) + len(couleursRestantes) < 3:
        return

    for nextCandidat in list(candidats):
        if nextCandidat > sommet:
            clique.add(nextCandidat)
            newCandidats = candidats.intersection(graphe[nextCandidat])
            rechercheClique(nextCandidat, clique, newCandidats, graphe, cliquesMaximales, carteCouleurs)
            clique.remove(nextCandidat)


def toutesLesCliques(graphe, n, carteCouleurs):
    cliquesMaximales = []

    for sommet in range(n):
        cliqueInit = {sommet}
        candidatsInit = set(graphe[sommet])  #la liste de tous les voisins du sommet
        rechercheClique(sommet, cliqueInit, candidatsInit, graphe, cliquesMaximales, carteCouleurs)
    
    return cliquesMaximales
    

def classificationPopulation(graphe, n):
    carteCouleurs = colorierGraphe(graphe, n)
    listeCliques = toutesLesCliques(graphe, n, carteCouleurs)
    classification = {i: "Individu normal" for i in range(n)}  #tout le monde sera classé comme individu normal au début

    for clique in listeCliques:
        for sommet in clique:
            classification[sommet] = "Membre d'une clique (Fraudeur)"

    for sommet in range(n):
        if classification[sommet] == "Individu normal":  #ne plus analyser ceux qui sont déja membre d'un noyau
            nbInteractions = 0  #le nombre d'interactions avec les membre d'une clique

            for clique in listeCliques:
                x = len(graphe[sommet].intersection(clique)) #--> éléments communs entre deux ensemble
                if x > nbInteractions:
                    nbInteractions = x

            if nbInteractions >= 2:
                classification[sommet] = "Cible/Complice"
            if nbInteractions == 1:
                classification[sommet] = "Interaction simple"

    return classification, listeCliques
                
