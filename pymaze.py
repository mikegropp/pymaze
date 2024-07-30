import random

def generate_maze(rows, cols):
    # Initialize maze grid with walls and border
    maze = [[1] * (cols * 2 + 1) for _ in range(rows * 2 + 1)]

    def create_maze(x, y):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2  # Move two steps in the direction
            
            if 1 <= nx < rows * 2 and 1 <= ny < cols * 2 and maze[nx][ny] == 1:
                maze[x + dx][y + dy] = 0  # Open the wall between cells
                maze[nx][ny] = 0
                create_maze(nx, ny)

    # Start maze generation from (1, 1)
    maze[1][1] = 0
    create_maze(1, 1)
    
    # Create entrance and exit by making gaps in the border
    maze[0][1] = 0  # Entrance (gap in the top border)
    maze[rows * 2][cols * 2 - 1] = 0  # Exit (gap in the bottom border)
    
    for row in maze:
        for cell in row:
            if cell == 1:
                print("#", end=" ")  # wall
            else:
                print(" ", end=" ")  # path
        print()
