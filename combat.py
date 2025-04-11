
import random

def effectuer_combat(joueur, ennemi):
    print("\nLe combat commence entre", joueur.name, "et", ennemi.name)

    tour = 1
    while joueur.hp > 0 and ennemi.hp > 0:
        print(f"\n--- Tour {tour} ---")
        print(f"{joueur.name} : {joueur.hp:.1f} PV")
        print(f"{ennemi.name} : {ennemi.hp:.1f} PV")

        # Tour du joueur
        input("\nAppuie sur Entrée pour attaquer !")
        degats_joueur = calculer_degats(joueur, ennemi)
        ennemi.hp -= degats_joueur
        print(f"{joueur.name} inflige {degats_joueur:.1f} dégâts à {ennemi.name}.")

        if ennemi.hp <= 0:
            print(f"\n🎉 {joueur.name} a vaincu {ennemi.name} !")
            break

        # Tour de l'ennemi
        degats_ennemi = calculer_degats(ennemi, joueur)
        joueur.hp -= degats_ennemi
        print(f"{ennemi.name} riposte et inflige {degats_ennemi:.1f} dégâts à {joueur.name}.")

        if joueur.hp <= 0:
            print(f"\n💀 {joueur.name} a été vaincu par {ennemi.name}...")

        tour += 1


def calculer_degats(attacker, defender):
    base = attacker.stats["force"]
    crit_chance = attacker.stats["chance"] / 1000  # 10 = 1% crit
    if random.random() < crit_chance:
        print("Coup critique !")
        base *= 2
    reduction = defender.stats["defense"] / 100  # 100 def = -1 dégât
    degats = max(0, base - reduction)
    return degats
