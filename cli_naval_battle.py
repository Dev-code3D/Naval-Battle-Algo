# Python | Naval Battle Cli Version - ISFATES Algorithmie Groupe Sandy Maurelle - Théo BELTZUNG - Assem HSSINI
# File_name = "cli_naval_battle.py" (version 1.1.5)

import random

def plate(n):
    """fonction qui genere une matrice carré de dim=n"""
    return [[0 for _ in range(n)] for _ in range(n)]


def show_board(grid):
    """fonction pour afficher visuellement le plateau de jeux pour le joueur
       Lettres en colonnes, chiffres pour les lignes"""
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
    """Génère t bateaux (1 case chacun) sans doublon"""
    size = len(grid)
    boat_list = []

    while len(boat_list) < t:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        pos = (x, y)
        if pos not in boat_list:
            boat_list.append(pos)

    return boat_list


def parse_coord(coord, size):
    """Convertit une entrée type 'A1', 'b2' en indices (row, col)"""
    try:
        row = ord(coord[0].upper()) - ord('A')
        col = int(coord[1:]) - 1
        if not (0 <= row < size and 0 <= col < size):
            raise ValueError
        return row, col
    except (ValueError, IndexError):
        return None


def cli_naval_btl(grid, boat_list):
    print("\n\nWelcome to Naval Battle !!!\n")

    size = len(grid)
    tours = 6

    while tours > 0:
        show_board(grid)
        print(f"\nRemaining rounds : {tours}")
        print(f"Enter coordinates like A1, b2...")

        coord = input("Coordinate : ")
        parsed = parse_coord(coord, size)
        if parsed is None:
            print("Invalid format! Example: a2, C3...")
            continue

        row, col = parsed
        pos = (row, col)

        if grid[row][col] in ["X", "Z"]:
            print("You already tried this cell !")
            continue

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
        cli_naval_btl(new_grid, new_boats)

    print("Thank you for playing ! See you soon :)")


# Programme principal
n = 4
grid = plate(n)
boat_list = gen_boat(4, grid)

cli_naval_btl(grid, boat_list)
