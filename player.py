# player.py
class Player:
    def __init__(self, name):
        self.name = name
        self.stats = {
            "force": 100,
            "chance": 100,
            "vigueur": 100,
            "vitesse": 100,
            "defense": 100,
            "magie": 100,
            "exp": 0
        }
        self.level = 1
        self.hp = self.stats["vigueur"]  # Points de vie de départ
        self.mp = self.stats["magie"]    # Points de magie de départ

    def afficher_stats(self):
        print(f"\nStatistiques de {self.name} :")
        for stat, value in self.stats.items():
            print(f"- {stat.capitalize()} : {value}")
        print(f"PV : {self.hp} / {self.stats['vigueur']}")
        print(f"PM : {self.mp} / {self.stats['magie']}\n")
