import random

def effectuer_combat(joueur, ennemi):
    print("\n⚔️ Le combat commence entre", joueur.name, "et", ennemi.name)

    tour = 1
    while joueur.hp > 0 and ennemi.hp > 0:
        print(f"\n--- Tour {tour} ---")
        print(f"{joueur.name} : {joueur.hp:.1f} PV")
        print(f"{ennemi.name} : {ennemi.hp:.1f} PV")

        # Menu joueur
        print("\nQue veux-tu faire ?")
        print("1. Attaquer")
        print("2. Fuir")
        choix = input("> ")

        if choix == "1":
            # Attaque du joueur
            degats_joueur = calculer_degats(joueur, ennemi)
            ennemi.hp -= degats_joueur
            print(f"{joueur.name} inflige {degats_joueur:.1f} dégâts à {ennemi.name}.")
            if ennemi.hp <= 0:
                print(f"\n🎉 {joueur.name} a vaincu {ennemi.name} !")
                exp_gagnee = calculer_experience(ennemi)
                joueur.stats["exp"] += exp_gagnee
                print(f"✨ {joueur.name} gagne {exp_gagnee} points d'expérience.")
                break

        elif choix == "2":
            if tenter_fuite(joueur, ennemi):
                print(f"🏃 {joueur.name} a réussi à fuir le combat !")
                return
            else:
                print(f"❌ {joueur.name} essaie de fuir... mais la {ennemi.name} le rattrape !")

        else:
            print("Commande inconnue. Tour perdu 😢")

        # Tour de l’ennemi si toujours vivant
        if ennemi.hp > 0:
            degats_ennemi = calculer_degats(ennemi, joueur)
            joueur.hp -= degats_ennemi
            print(f"{ennemi.name} attaque et inflige {degats_ennemi:.1f} dégâts à {joueur.name}.")

            if joueur.hp <= 0:
                print(f"\n💀 {joueur.name} a été vaincu par {ennemi.name}...")

        tour += 1


def calculer_degats(attacker, defender):
    base = attacker.stats["force"]

    # Calcul du critique : notre chance - leur chance, borné entre 0% et 50%
    diff_chance = attacker.stats["chance"] - defender.stats["chance"]
    crit_chance = max(0, min(0.5, diff_chance / 1000))  # Ex: diff = 100 => 10%
    
    if random.random() < crit_chance:
        print("💥 Coup critique !")
        base *= 2

    reduction = defender.stats["defense"] / 100  # 100 def = -1 dégât
    degats = max(0, base - reduction)
    return degats


def tenter_fuite(joueur, ennemi):
    # Calcul simple : vitesse joueur - vitesse ennemi
    diff_vitesse = joueur.stats["vitesse"] - ennemi.stats["vitesse"]
    chance_fuite = max(0.1, min(0.9, 0.5 + diff_vitesse / 200))  # Entre 10% et 90%

    return random.random() < chance_fuite


def calculer_experience(ennemi):
    total_stats = sum(ennemi.stats.values())
    return total_stats // 10  # Exemple : 350 → 35 XP
