# Python | Naval Battle CLI Version - ISFATES Algorithmique L1
# Auteurs : Groupe Sandy Maurelle - Théo BELTZUNG - Assem HSSINI
# File_name = "cli_naval_battle.py" (version 1.3.0)

import random # -> pour générer des nombres aléatoires
import time # pour gèrer le temps de l'animation (emoji)
import sys # pour gèrer l'affichage des animation (emoji)

def tir_en_cours():
    """Animation pour simuler un tir en cours."""
    anim = ["💥", "🔫", "🎯", "💣", "🔥", "⚡", "💢", "🎇", "🎆"]
    for symb in anim:
        sys.stdout.write(f"\rShooting in progress... {symb}   ")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\rShooting completed !       ")  # Efface le reste de la ligne avec \r


def plate(n):
    """Fonction qui génère une matrice carrée de dim=n"""
    return [[0 for _ in range(n)] for _ in range(n)]


def show_board(grid):
    """Affiche le plateau comme un échiquier (style des échects) : lettres en colonnes, chiffres en lignes"""
    size = len(grid)
    letters = [chr(ord('A') + i) for i in range(size)]
    
    # Affichage de l'entête avec lettres (colonnes)
    print("    " + "   ".join(letters))
    print("  +" + "---+" * size)
    
    # Affichage des lignes avec chiffres à gauche
    for i, row in enumerate(grid):
        print(f"{i+1} | " + " | ".join(str(cell) for cell in row) + " |")
        print("  +" + "---+" * size)


def gen_boat(t, grid):
    """Génère un nombre t de bateaux (1 case chacun) sans doublon"""
    size = len(grid)
    boat_list = []

    while len(boat_list) < t:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        pos = (row, col)
        if pos not in boat_list: # Sans doublon
            boat_list.append(pos)

    return boat_list


def parse_coord(coord, size):  # Gestion de l'entrée des coordonnées
    """
    Convertit une entrée type 'A1', 'b2' en indices lignes/colonnes (row, col)
    Pour interagir avec la grille.
    """
    try:
        # Conversion de la lettre (1er) en indice de colonne (Ex : A=0,..Z=25)
        # ~> Str TO Unicode DE 'B' : ord('B') - ord('A') = 66 - 65 = 1
        col = ord(coord[0].upper()) - ord('A')

        # Conversion de la partie numérique (2eme) en indice de ligne
        # Exemple : '1' → 0, '2' → 1
        row = int(coord[1:]) - 1

        # Vérifie que les indices sont dans les limites de la grille
        if not (0 <= row < size and 0 <= col < size):
            raise ValueError  # Provoque l'entrée dans le except si hors limites

        return row, col  # Retourne un tuple (ligne, colonne)

    except (ValueError, IndexError):
        # En cas d'entrée invalide : coordonnée impossible, lettre incorrecte,
        # chiffre manquant, hors de la grille, etc.
        return None



def cli_naval_btl(grid, boat_list, tours=10): # Programe de bienvenue
    print("\n\nWelcome to Naval Battle !!!\n")

    size = len(grid)
    newtours=tours # Pour gèrer le fait de re-jouer plusieurs fois sans quitter le prgm
    while tours > 0:
        show_board(grid) # Affiche la grille
        print(f"\nRemaining rounds : {tours}") # Tours restants
        print("Enter coordinates (eq A1, b2)...")

        coord = input("Coordinate : ")
        parsed = parse_coord(coord, size)
        if parsed is None:
            print("Invalid format! Example: A1, C3...")
            continue

        row, col = parsed

        if grid[row][col] in ["X", "Z"]:
            print("You already tried this cell !")
            continue

        tir_en_cours() # Animation

        pos = (row, col)
        if pos in boat_list:
            print("\nYou find a boat !")
            grid[row][col] = "X"
            boat_list.remove(pos)

            if len(boat_list) == 0:
                print("\nAll the boats have been sunk !")
                break
        else:
            print("\nMissed…")
            grid[row][col] = "Z"

        tours -= 1

    if tours == 0 and len(boat_list) > 0:
        print(f"\nGame Over ! There were {len(boat_list)} boats left.")

    loop = input("\nDo you want to start again? (yes/oui/no) : ")
    if loop.lower() in ["oui", "yes", "y", "o"]:
        new_grid = plate(size)
        new_boats = gen_boat(4, new_grid)
        cli_naval_btl(new_grid, new_boats, newtours)

    print("Thank you for playing ! See you soon :)")


# Programme principal + lancement
n = 4 # n => est la valeur de la taille de la grille/ du plateau à générer (dim = n * n = n²)
grid = plate(n)
boat_list = gen_boat(4, grid)
tours = 10
cli_naval_btl(grid, boat_list, tours)
