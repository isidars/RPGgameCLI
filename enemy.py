class Enemy:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
        self.hp = stats["vigueur"]
        self.mp = stats["magie"]

    def afficher_stats(self):
        print(f"\nStatistiques de {self.name} :")
        for stat, value in self.stats.items():
            print(f"- {stat.capitalize()} : {value}")
        print(f"PV : {self.hp} / {self.stats['vigueur']}")
        print(f"PM : {self.mp} / {self.stats['magie']}\n")

# Fonction pour créer la souris
def create_mouse():
    stats = {
        "force": 50,
        "chance": 40,
        "vigueur": 100,
        "vitesse": 110,
        "defense": 30,
        "magie": 0
    }
    return Enemy("Souris sauvage", stats)
