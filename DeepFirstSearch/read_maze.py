# read_maze.py

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
                    print('The maze is not rect!')
                    raise SystemExit
            return maze
    except OSError:
        print("There is a problem with the file you have selected.")
        raise SystemExit


if __name__ == "__main__":
    # maze = read_maze("mazes/modest_maze.txt")
    maze = read_maze("mazes/chalenge_maze.txt")
    for row in maze:
        print(row)
    ## My Output 
    # for row in maze:
    #     for char in row:
    #         print(char, end='')
        
    #     print('')
