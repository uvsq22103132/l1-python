import random 

#initialise la grille de jeu avec des tuiles vides
def init_grid():
    return [[0 for i in range(4)] for j in range(4)]


#ajoute une nouvelle tuile (2 ou 4) au hasard sur la grille
def  add_random_tile(grid):
    empty_cells = [(i,j)for i in range(4)for j in range(4) if grid[i][j] == 0]
    if empty_cells:
        value = 2 if random.random() < 0.9 else 4
        (i,j)=random.choice(empty_cells)
        grid[i][j]=random.choice(empty_cells)
        grid[i][j]=value


#déplace les tuiles dans une direction donnée 
def move_tiles(grid,direction):
    if direction == 'up':
        grid = transpose(grid)
    elif direction == 'right':
        grid = reverse_rows(grid):
    elif direction == 'down':
        grid = reverse_rows(transpose(grid))
    for row in range(4):
        new_row = merge_row(grid[row])
        grid[row] = new_row
    if direction == 'up':
        grid = transpose(grid)
    elif direction == 'right':
        grid = reverse_rows(grid)
    elif direction == 'down':
        grid = reverse_rows(transpose(grid))
    return grid



#vérifie si le jeu est fini(plus de mouvement possible)
def is_game_over(grid):
    if any(0 in row for row in grid):
        return False
    if any(can_merge(row)for row in grid):
        return False
    if any(can_merge)