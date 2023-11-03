# dfs.py
from helpers import offsets, read_maze, is_legal_pos, get_path, print_maze, print_maze_with_path
from stack import Stack


def dfs(maze, start, goal):
    if not is_legal_pos(maze, start):
        print("Not legal start pos. Sorry")
        return None
    if not is_legal_pos(maze, goal):
        print("Not legal goal pos. Sorry")
        return None

    stack = Stack()
    stack.push(start)
    predecessors = {start: None}

    while not stack.is_empty():
        current_cell = stack.pop()
        # print(f"curr_cell:{current_cell}, stack:{stack}")
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        for direction in ("up", "right", "down", "left"):
            row_offset, col_offset = offsets[direction]
            neighbor = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(maze, neighbor) and neighbor not in predecessors:
                stack.push(neighbor)
                predecessors[neighbor] = current_cell
    return None


if __name__ == "__main__":
    # # Test1
    # print("Test1")
    # maze = [[" "] * 3 for row in range(3)]
    # print_maze(maze)
    # start_pos = (0, 0)
    # goal_pos = (2, 2)
    # result = dfs(maze, start_pos, goal_pos)
    # print(result)
    # print_maze_with_path(maze, result, start_pos, goal_pos)
    # assert result == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    # print("-" * 20)

    # #Test2
    # print("Test2")
    # maze = read_maze("mazes/mini_maze.txt")
    # print_maze(maze)
    # start_pos = (0, 0)
    # goal_pos = (2, 2)
    # result = dfs(maze, start_pos, goal_pos)
    # print(result)
    # print_maze_with_path(maze, result, start_pos, goal_pos)
    # assert result == [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]
    # print("-" * 20)

    # # Test3
    # print("Test3")
    # maze = read_maze("mazes/mini_dfs.txt")
    # print_maze(maze)
    # start_pos = (0, 0)
    # goal_pos = (3, 3)
    # result = dfs(maze, start_pos, goal_pos)
    # print(result)
    # print_maze_with_path(maze, result, start_pos, goal_pos)
    # assert result is None

    # # Test4
    # print("Test4")
    # maze = read_maze("mazes/modest_maze.txt")
    # print_maze(maze)
    # start_pos = (1, 1)
    # goal_pos = (8, 8)
    # result = dfs(maze, start_pos, goal_pos)
    # print(result)
    # print_maze_with_path(maze, result, start_pos, goal_pos)
    # assert result == [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (4, 4), (5, 4), (6, 4), (6, 5), (7, 5), (8, 5), (8, 6), (8, 7), (8, 8)]

    # # Test5
    # print("Test5")
    # maze = read_maze("mazes/wide_maze.txt")
    # print_maze(maze)
    # start_pos = (1, 1)
    # goal_pos = (23, 32)
    # result = dfs(maze, start_pos, goal_pos)
    # print(result)
    # print_maze_with_path(maze, result, start_pos, goal_pos)

    # # Test5.2
    # print("Test5.2")
    # maze = read_maze("mazes/wide_maze.txt")
    # print_maze(maze)
    # start_pos = (1, 1)
    # goal_pos = (23, 7)
    # result = dfs(maze, start_pos, goal_pos)
    # print(result)
    # print_maze_with_path(maze, result, start_pos, goal_pos)

    # Test5.3
    print("Test5.3")
    maze = read_maze("mazes/wide_maze.txt")
    print_maze(maze)
    start_pos = (1, 1)
    goal_pos = (15, 39)
    result = dfs(maze, start_pos, goal_pos)
    print(result)
    print_maze_with_path(maze, result, start_pos, goal_pos)
