# Python | Naval Battle Cli Version - ISFATES Algorithmie Groupe Sandy Maurelle - Théo BELTZUNG - Assem HSSINI
# File_name = "cli_naval_battle.py" (version 1.0)

import random
import time
import sys

def tir_en_cours():
    #Animation CLI pour simuler un tir en cours.
    anim = ["💥", "🔫", "🎯", "💣"]
    for symb in anim:
        sys.stdout.write(f"\rTir en cours... {symb}")
        sys.stdout.flush()
        time.sleep(0.3)
    print("\rTir effectué !      ")

# (n=4) grid_exemple = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]

def plate(n):
    """fonction qui genere une matrice carré de dim=n"""
    return [[0 for _ in range(n)] for _ in range(n)]


def show_board(grid):
    """fonction pour afficher visuellement le plateau de jeux pour le joueur"""
    size = len(grid)
    letters = [chr(ord('A') + i) for i in range(size)]
    # Affichage de l'entete et des colonnes
    print("    " + "   ".join(str(i + 1) for i in range(size)))
    # Affichage pour chaques lignes
    for i, row in enumerate(grid):
        # Ligne avec contenu
        print(f"{letters[i]}   " + " | ".join(str(cell) for cell in row))
        # Ligne de séparation (pas après la dernière)
        if i < size - 1:
            print("   " + "---+" * (size - 1) + "---")


def gen_boat(t, grid):
    """Génère t bateaux (1 case chacun) sans doublon"""
    size = len(grid)
    boat_list = []

    while len(boat_list) < t:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        pos = (x, y)

        if pos not in boat_list:   # éviter les doublons
            boat_list.append(pos)

    return boat_list

def cli_naval_btl(grid, boat_list):
    print("\n\nWelcome to Naval Battle !!!\n")

    size = len(grid)
    tours = 6

    while tours > 0:
        show_board(grid)
        print(f"\nRemaining rounds : {tours}")
        print(f"Enter coordinates between 0 and {size-1}.")
        try:
            u_x = int(input("x = "))
            u_y = int(input("y = "))
            if not (0 <= u_x < size and 0 <= u_y < size):
                print("Invalid coordinates !")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        tir_en_cours()
        
        pos = (u_x, u_y)

        if pos in boat_list:
            print("\nYou find a boat !")
            grid[u_x][u_y] = "X"
            boat_list.remove(pos)

            if len(boat_list) == 0:
                print("\nAll the boats have been sunk !")
                break
        else:
            print("\nRaté…")
            grid[u_x][u_y] = "Z"

        tours -= 1

    if tours == 0 and len(boat_list) > 0:
        print(f"\nGame Over ! There were {len(boat_list)} boats left.")

    loop = input("\nDo you want to start again? (yes/no) : ")
    if loop.lower() == "oui":
        return cli_naval_btl(plate(len(grid)), gen_boat(len(boat_list), grid))

    print("Thank you for playing ! See you soon :)")

# Programme principal
n = 4
grid = plate(n)
boat_list = gen_boat(4, grid)

cli_naval_btl(grid, boat_list)
