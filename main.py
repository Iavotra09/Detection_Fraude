import math
from constructionGraphe import genererGrapheAleatoire, rendreConnexe, obtenirMatriceAdjacence
from classification import classificationPopulation
from visualisation import dessinerGrapheInteractif

def executerPipelineDetection():
    n = int(input("Entrez la taille de la population (n) : "))
    p_seuil = math.log(n) / n
    p_choisi = p_seuil * 1.2 # Légèrement au-dessus du seuil pour la connexité
    
    
    G = genererGrapheAleatoire(n, p_choisi)
    G_prime = rendreConnexe(G, n)
    resultats, cliques_detectees = classificationPopulation(G_prime, n)
    
    print(f"Nombre total de cliques frauduleuses détectées : {len(cliques_detectees)}")
    stats = {"Membre d'une clique": 0, "Cible/Complice": 0, "Interaction simple": 0, "Individu normal": 0}
    for role in resultats.values():
        stats[role] += 1
        
    print("\n--- RÉSULTATS DE LA DÉTECTION ---")
    for role, total in stats.items():
        print(f"-> {role} : {total} personnes ({(total/n)*100:.1f}%)")
    
    dessinerGrapheInteractif(G_prime, resultats)

if __name__ == "__main__":
    executerPipelineDetection()
