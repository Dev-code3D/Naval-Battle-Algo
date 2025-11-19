# Python | Naval Battle Cli Version - ISFATES Algorithmie Groupe Sandy Maurelle - Théo BELTZUNG - Assem HSSINI
# File_name = "cli_naval_battle.py" (version 1.0)

import random

# grid_exemple = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]

def plate(n):
    """fonction qui genere une matrice carré de dim=n"""
    grid = []
    grid = [[0 for _ in range(n)] for _ in range(n)]
    return grid
n = 4
# plate(n)

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

show_board(plate(n))

def gen_boat(n):
    """fonction qui genere une liste de n bateau"""
    boat_list = [[] for _ in range(n)]
    return boat_list
n = 4
gen_boat(n)

def cli_naval_btl(grid, boat_list):
    """programme principal"""

    print("\n\nWelcome in Naval Battle !!!\n")

    p_min = 0
    p_max = len(grid)-1

    n = 0
    while n < 4:
        x,y = random.randint(p_min, p_max), random.randint(p_min, p_max)
        boat_pos = (x,y)
        boat_list[n].append(boat_pos)
        sol = grid[x][y] = "X"
        n += 1
    
    print(f"Board :\n{grid}\n")

    print(f"Enter coordinate (x,y) between {p_min} and {p_max} !")
    u_x, u_y = int(input('x = ')), int(input('y = '))
    pos = (u_x,u_y)

    user = grid[u_x][u_y] = "i"
    
    print(f"\np = {grid}\nboat_pos = {boat_pos}\npos = {pos}")
    
    if boat_pos in pos:
        print("\nYou find a boat !")
    else:
        print("\nrestart")

    print(f"Boat list = {boat_list}")

    loop = str(input("Voulez-vous recommencer ? (oui/non) : "))
    if loop == "oui":   print(cli_naval_btl(grid, boat_list)) 
    print("Merci d'avoir jouer et à bientôt ! :)")
    return grid

print(cli_naval_btl(grid, boat_list))


