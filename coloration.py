def colorierGraphe(graphe, n):    #on va symboliser les couleurs avec des chiffres 1, 2, 3, ...
    couleurs = {i: -1 for i in range(n)}  #au début, aucune couleur n'est attribuée 
    couleurs[0] = 0  #initialiser la couleur du premier sommet à 0

    for u in range(1, n):
        indisponible = [False] * n
        for voisin in graphe[u]:  #regarder les voisins de u et notés les couleurs déja prises
            if couleurs[voisin] != -1:
                indisponible[couleurs[voisin]] = True

        couleurDispo = 0
        while couleurDispo < n:  
            if not indisponible[couleurDispo]:
                break
            couleurDispo += 1  #la plus petite couleur disponible

        couleurs[u] = couleurDispo

    return couleurs
