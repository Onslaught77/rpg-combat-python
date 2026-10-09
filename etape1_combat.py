# ==============================================================
# RPG - Système de combat au tour par tour
# Un joueur affronte un monstre jusqu'à ce que l'un des deux tombe.
# ==============================================================

# Caractéristiques du joueur et du monstre (dictionnaires)
player = {"name": "Héros", "hp": 30, "attack": 6}
monster = {"name": "Gobelin", "hp": 20, "attack": 4}

print(f"Un {monster['name']} sauvage apparaît !")

turn = 1

# Le combat continue tant que les deux personnages sont en vie
while player["hp"] > 0 and monster["hp"] > 0:
print(f"\n--- Tour {turn} ---")

# Le joueur attaque
monster["hp"] = max(0, monster["hp"] - player["attack"])
print(f"{player['name']} attaque et inflige {player['attack']} dégâts.")
print(f"{monster['name']} : {monster['hp']} PV restants.")

# Si le monstre est vaincu, il ne riposte pas
if monster["hp"] == 0:
break

# Le monstre riposte
player["hp"] = max(0, player["hp"] - monster["attack"])
print(f"{monster['name']} riposte et inflige {monster['attack']} dégâts.")
print(f"{player['name']} : {player['hp']} PV restants.")

turn += 1

# Résultat du combat
if player["hp"] > 0:
print(f"\nVictoire ! {player['name']} a vaincu {monster['name']}.")
else:
print(f"\nDéfaite... {player['name']} a été vaincu par {monster['name']}.")
