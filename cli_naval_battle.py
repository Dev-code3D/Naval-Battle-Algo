# Python | Naval Battle CLI Version - ISFATES Algorithmique L1 Sem1
# Auteurs : Groupe Sandy Maurelle - (xThéo BELTZUNGx) - Assem HSSINI
# File_name = "cli_naval_battle.py" (version 1.5.3)

import random # -> pour générer des nombres aléatoires
import time # / pour gèrer le temps de l'animation (emoji)
import sys # / pour gèrer l'affichage-suppr des animation (emoji)

version = "1.5.4"

def set_difficulty(n, nbr_boat, tours):
    """Allows the user to set the game difficulty."""
    print("Choose the difficulty level:")
    print("1-Easy 🙃 \n2-Medium 🛳️ \n3-Hard ☠️☠")
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice == 1:
                return 4, 4, 10  # (grid size, boats, tours - Easy)
            elif choice == 2:
                return 6, 4, 8
            elif choice == 3:
                return 8, 6, 14
            else:
                print("Please enter a valid option.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 3.")


def show_menu():
    """Affiche le menu du jeu de manière visuelle"""
    print("\n🚢🚢🚢 WELCOME TO NAVAL BATTLE 🚢🚢🚢\n")
    print("🎯 Rules:")
    print("• Enter coordinates like A1, B2...")
    print("• Find and sink all the boats")
    print("• You have a limited number of rounds\n")
    var = 0
    while True:
        ready = input("Are you ready to play? (yes/no): ").lower()
        if ready in ["yes", "y", "oui", "o"]: print("\nGreat! Let's start! \n") ; break
        var+=1
        if var >= 3:
            print("No problem, see you soon!\n") ; sys.exit()
        print("Take your time! Press yes when you are ready.")

def countdown():
    """Animation d'un compte à rebours de 3 à 1"""
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print("GO! 🚀")

def tir_en_cours():
    """Animation pour simuler un tir en cours."""
    anim = ["💥", "🔫", "🎯", "💣", "🔥", "⚡", "💢", "🎇", "🎆", ""]
    for symb in anim:
        sys.stdout.write(f"\rShooting in progress... {symb}   ")
        sys.stdout.flush()
        time.sleep(0.2)
    print("\rShooting completed !")  # Efface le reste de la ligne avec \r


def plate(n):
    """Fonction qui génère une matrice carrée de dim=n**2"""
    return [[0 for i in range(n)] for i in range(n)]


def show_board(grid):
    """Affiche le plateau comme un échiquier (style des échects) : lettres en colonnes et chiffres en lignes"""
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
        if pos not in boat_list: # Verifie pour qu'il n'y a pas de doublon
            boat_list.append(pos)
    return boat_list


def parse_coord(coord, size):  # Gestion de l'entrée des coordonnées par l'utilisateur
    """
    Convertit une entrée type 'A1', 'b2' en indices lignes/colonnes (row, col)
    Pour faciliter l'interaction de l'utilisateur avec la grille - style echects.
    """
    try:
        # Conversion de la lettre (1ere) en indice de colonne (Ex : A=0,..Z=25)
        # Le calcul ~> Str VERS Unicode Pour trouver l'indice de colonne
        col = ord(coord[0].upper()) - ord('A') # EXEMPLE -> B = ord('B') - ord('A') = 66 - 65 = 1

        # Conversion de la partie numérique (2eme) en indice de ligne ; exemple : '1' -> 0, '2' -> 1
        row = int(coord[1:]) - 1

        # Vérifie que les indices sont dans les limites de la grille
        if not (0 <= row < size and 0 <= col < size):
            raise ValueError  # Provoque l'entrée dans le except si depassement de la limite

        return row, col  # Retourne un tuple (ligne, colonne)

    except (ValueError, IndexError):
        # En cas d'entrée invalide : coordonnée impossible ou lettre incorrecte, chiffre manquant, hors de la grille, etc.
        return None


def progress_bar(total_tours, tours):
    """Affiche une barre de progression vis-a-vis de a la progression du jeux fait par le joueur par rapport au nombre de tours max possibles"""
    # longueur de la barre vaut le max de "tours" soit la valeur par défaut
    i = total_tours - tours # (eq: i -> 1 = 10 - 9 )
    bar = "#" * i + "." * (tours)
    sys.stdout.write(f"\rProgress: [{bar}] - {tours}")
    sys.stdout.flush()
    time.sleep(0.4)
    print()

def chronogame(start, end):
    return(f"Time = {end - start:.3f}s")


def cli_naval_btl(grid, boat_list, tours, total_tours): # Programe principal
    """Boucle / programme principal du jeu"""
    print("By Grp1 : Sandy Maurelle - (xThéo BELTZUNGx) - Assem HSSINI")
    print(f"v.{version}\n")

    start=time.time()
    size = len(grid)
    cnt_boat = len(boat_list)
    icon_boat = "🛥️"
    icon_missed  = "🕸️" #🌊⚙️
    print("\nEnter coordinates (eq A1, b2)... [stop with: STOPall]\n")

    while tours > 0:
        show_board(grid) # Affiche la grille
        print(f"Boats : {len(boat_list)}/{cnt_boat}")

        progress_bar(total_tours,tours) # barre de progression + tours restants

        coord = input("Coordinate : ")
        parsed = parse_coord(coord, size)
        if coord == "STOPall": print("\nSee you soon!\n") ; sys.exit()
        if parsed is None:
            print("Invalid format! Example: A1, C3...\n")
            time.sleep(2.4)
            continue

        row, col = parsed

        if grid[row][col] in [icon_boat, icon_missed]:
            print("You already tried this cell !")
            continue

        tir_en_cours() # Animation 
        
        time.sleep(1)
        pos = (row, col)
        if pos in boat_list:
            print("\nYou find a boat !\n")
            grid[row][col] = icon_boat
            boat_list.remove(pos)

            if len(boat_list) == 0:
                print("\nAll the boats have been sunk !")
                break
        else:
            print("\nMissed…\n")
            grid[row][col] = icon_missed
            time.sleep(1.2)
        tours -= 1

    if tours == 0 and len(boat_list) > 0:
        print(f"\nGame Over ! There were {len(boat_list)} boats left.")

    loop = input("\nDo you want to start again? (yes/oui/no) : ")
    if loop.lower() in ["oui", "yes", "y", "o"]:
        run_prgm()
    else :
        end = time.time()
        print(chronogame(start, end))
        print("Thank you for playing ! See you soon :)")
        print("By Grp1 : Sandy Maurelle - (xThéo BELTZUNGx) - Assem HSSINI")
        print(f"v.{version}\n")


# Programme de lancement
def run_prgm():
    """Function to manage and launch the program - game"""
    show_menu()
    n, nbr_boat, tours = 4, 4, 10 # Default values
    n, nbr_boat, tours = set_difficulty(n, nbr_boat, tours)
    total_tours = tours
    grid = plate(n)
    boat_list = gen_boat(nbr_boat, grid)
    countdown()
    cli_naval_btl(grid, boat_list, tours, total_tours)
    return("___")

# Run the program
if __name__ == "__main__":
    print(run_prgm())

