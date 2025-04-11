from player import Player
from enemy import create_mouse
from combat import effectuer_combat

# Création des personnages
joueur = Player("Héros")  # classe de base avec stats = 100 partout
souris = create_mouse()

# Affichage
joueur.afficher_stats()
souris.afficher_stats()

# Combat !
effectuer_combat(joueur, souris)

