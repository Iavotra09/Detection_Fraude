import webbrowser
from pyvis.network import Network

def dessinerGrapheInteractif(graphe, classification, nom_fichier="Detection_fraude.html"):
    net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white", notebook=False)
   
    table_couleurs = {
        "Membre d'une clique": "red",
        "Cible/Complice": "orange",
        "Interaction simple": "yellow",
        "Individu normal": "green"
    }

    for sommet in graphe.keys():
        role = classification[sommet]
        couleur_noeud = table_couleurs.get(role, "gray")
        net.add_node(
            sommet, 
            label=str(sommet), 
            title=f"Individu {sommet} : {role}", 
            color=couleur_noeud,
            size=25 if couleur_noeud == "red" else 15
        )

    for u in graphe.keys():
        for v in graphe[u]:
            if u < v:
                net.add_edge(u, v, color="gray", width=1)

    net.toggle_physics(True) 
    
    net.write_html(nom_fichier, open_browser=False, notebook=False)
    webbrowser.open(nom_fichier)

