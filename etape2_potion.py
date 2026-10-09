# ==============================================================
# RPG - Système de combat au tour par tour
# À chaque tour, le joueur choisit d'attaquer ou de boire une potion.
# ==============================================================

# Caractéristiques du joueur et du monstre (dictionnaires)
player = {"name": "Héros", "hp": 30, "max_hp": 30, "attack": 6, "potions": 3}
monster = {"name": "Gobelin", "hp": 20, "attack": 4}

POTION_HEAL = 10 # Points de vie rendus par une potion

print(f"Un {monster['name']} sauvage apparaît !")

turn = 1

# Le combat continue tant que les deux personnages sont en vie
while player["hp"] > 0 and monster["hp"] > 0:
print(f"\n--- Tour {turn} ---")
print(f"{player['name']} : {player['hp']}/{player['max_hp']} PV | "
f"{monster['name']} : {monster['hp']} PV")
print("1. Attaquer")
print(f"2. Boire une potion ({player['potions']} restante(s))")
choice = input("Ton choix : ")

if choice == "1":
# Le joueur attaque
monster["hp"] = max(0, monster["hp"] - player["attack"])
print(f"{player['name']} attaque et inflige {player['attack']} dégâts.")

elif choice == "2":
if player["hp"] == player["max_hp"]:
print("Tes PV sont déjà au maximum ! Choisis une autre action.")
continue # Le tour est rejoué, la potion est conservée
elif player["potions"] > 0:
# Le joueur se soigne, sans dépasser ses PV maximum
healed = min(POTION_HEAL, player["max_hp"] - player["hp"])
player["hp"] += healed
player["potions"] -= 1
print(f"{player['name']} boit une potion et récupère {healed} PV.")
else:
print("Plus de potion ! Choisis une autre action.")
continue # Le tour est rejoué, le monstre n'attaque pas

else:
print("Choix invalide, tape 1 ou 2.")
continue

# Si le monstre est vaincu, il ne riposte pas
if monster["hp"] == 0:
break

# Le monstre riposte
player["hp"] = max(0, player["hp"] - monster["attack"])
print(f"{monster['name']} riposte et inflige {monster['attack']} dégâts.")

turn += 1

# Résultat du combat
if player["hp"] > 0:
print(f"\nVictoire ! {player['name']} a vaincu {monster['name']}.")
else:
print(f"\nDéfaite... {player['name']} a été vaincu par {monster['name']}.")
