# helper.py

offsets = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0),
}

def read_maze(file_name):
    """
    Read as maze stored in a file and return a 2D list contained the maze 
    reprezentation
    """
    try:
        with open(file_name) as fh:
            maze = [[char for char in line.strip('\n')] for line in fh]
            num_cols_top_row = len(maze[0])
            for row in maze:
                if len(row) != num_cols_top_row:
                    print(f'The maze {file_name} is not rect!')
                    raise SystemExit
            return maze
    except OSError:
        print("There is a problem with the file you have selected.")
        raise SystemExit

def is_legal_pos(maze, pos):
    i, j = pos
    num_rows = len(maze)
    num_cols = len(maze[0])
    return 0 <= i < num_rows and 0<= j < num_cols and maze[i][j] != "*"

def get_path(predecessors, start_pos, goal_pos):
    current_pos = goal_pos
    path = []
    while current_pos != start_pos:
        path.append(current_pos)
        current_pos = predecessors[current_pos]
    path.append(start_pos)
    path.reverse()
    return path

def print_maze(maze):
    out_chars = {" ":" ", ".":".", "*":"\U00002588", "S":"S", "G":"G"} #"\U0001F0A1"
    print("+", "-" * len(maze[0]), "+", sep="")
    for row in maze:
        print("|", sep="", end="")
        for char in row:
            print(out_chars[char], end='')    
        print('|')
    print("+", "-" * len(maze[0]), "+", sep="")

def print_maze_with_path(maze, path, start_pos, goal_pos):
    shadow_maze = [[char for char in row] for row in maze]
    if path:
        for pos in path:
            row, col = pos
            shadow_maze[row][col] = "."
    else:
        print("Sorry no path present")
    shadow_maze[start_pos[0]][start_pos[1]] = "S"
    shadow_maze[goal_pos[0]][goal_pos[1]] = "G"
    print("shadow_maze:")
    print_maze(shadow_maze)
