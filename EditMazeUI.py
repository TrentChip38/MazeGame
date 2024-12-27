import pygame
import sys
import time
import maze_layout
import Level
# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Designer with Grid and Resizing")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Grid size, use 10 for finer control
GRID_SIZE = 20

# # Outer walls
#     (0, 0, 380, 20), (420, 0, 380, 20), (780, 0, 20, 280), (780, 320, 20, 280),
#         (0, 580, 380, 20), (420, 580, 380, 20), (0, 0, 20, 280), (0, 320, 20, 280),
# # Gate walls
# (380, 0, 40, 20),(780, 280, 20, 40), (380, 580, 40, 20),(0, 280, 20, 40),

# Variables
new_wall = False
walls_defualt = [
    # Start with outer and gate walls drawn as default for new maze
        (0, 0, 380, 20), (420, 0, 380, 20), (780, 0, 20, 280), (780, 320, 20, 280),
        (0, 580, 380, 20), (420, 580, 380, 20), (0, 0, 20, 280), (0, 320, 20, 280),
        (380, 0, 40, 20),(780, 280, 20, 40), (380, 580, 40, 20),(0, 280, 20, 40),
]
walls = []# Can use this with premade stuff
#walls = maze_layout.walls #use this if you want to use previouse layout still in the file

#Get num and decide if edit current or if start new
if len(sys.argv) > 1:
    try:
        level_num = int(sys.argv[1])
    except ValueError:
        print("Invalid argument. Falling back to interactive mode.")
        level_num = int(input("Enter the level number to save the maze: "))
else:
    level_num = int(input("Enter the level number to load the maze: "))
print(f"Level number: {level_num}")

#If level already exists, load wall array to edit it
if level_num in Level.levels.keys():
    #walls.extend(Level.levels[level_num].values())
    for wall in Level.levels[level_num]:
        walls.append(wall)
else:
    #Create new array by using default start
    #And later, don't delete anything but start a new spot
    new_wall = True
    walls = walls_defualt

level_phrase = "Level: " + str(level_num)
# Font for instructions
font = pygame.font.SysFont(None, 24)
instructions = [
    level_phrase,
    "Left-click and drag to create a wall.",
    "Right-click a wall to delete it.",
    "Press 'S' to save, 'ESC' to exit.",
]

def draw_instructions():
    """Draws the instructions on the screen."""
    for i, line in enumerate(instructions):
        text = font.render(line, True, BLACK)
        screen.blit(text, (10, 10 + i * 20))

def snap_to_grid(value, grid_size):
    """Snaps a value to the nearest grid position."""
    return round(value / grid_size) * grid_size

def normalize_rect(rect):
    #Fix wrong rectangles
    #Changes backwards or negative nums to positive and flips it
    x, y, width, height = rect
    if width < 0:
        x += width  # Shift x to the left
        width = abs(width)  # Make width positive
    if height < 0:
        y += height  # Shift y upward
        height = abs(height)  # Make height positive
    rect = (x, y, width, height)
    return rect

def save_maze_file(filename="UImaze.py"):
    """Saves the maze layout to a Python file."""
    with open(filename, "w") as file:
        file.write(str(level_num) + ":{\n     ")
        num = 0
        for rect in walls:
            if True:#not any(items < 0 for items in rect):
                file.write(f"({rect[0]}, {rect[1]}, {rect[2]}, {rect[3]}),")
                num += 1
                if num == 6:
                    file.write(f"\n     ")
                    num = 0
        file.write("\n},\n")
    print(f"Maze layout saved to {filename}")

def add_to_dict(file_path, array_name, key):
    #Open and read in the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    file.close()
    #Start creating new file with changes
    updated_lines = []
    #Flag to know to skip the original key files
    in_key = False
    in_dict = False
    for line in lines:
        #Wait until in the levels dictionary
        if array_name in line:
            in_dict = True
        # Find the line starting the target key
        if in_dict and ":" in line and str(level_num) in line:
            in_key = True
            # Insert the new key and array in this spot
            updated_lines.append(str(level_num) + ":{\n     \n")
            num = 0
            for rect in walls:
                updated_lines.append(f"   ({rect[0]}, {rect[1]}, {rect[2]}, {rect[3]}),")
                num += 1
                if num == 6:
                    updated_lines.append(f"\n")
                    num = 0
            updated_lines.append("\n" + "},\n")
        #Watch for bracket that ends target key
        if in_key and "}" in line:
            in_key = False
        if not in_key:
            #Add all original lines except those in the current target key
            updated_lines.append(line)
    with open("NewLevelFile.py", "w") as file:
        file.writelines(updated_lines)

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)

def get_resize_side(rect, mouse_pos, margin=10):
    """Checks if the mouse is near one of the rectangle's edges for resizing."""
    x, y = mouse_pos
    if abs(rect.left - x) <= margin:
        return "left"
    elif abs(rect.right - x) <= margin:
        return "right"
    elif abs(rect.top - y) <= margin:
        return "top"
    elif abs(rect.bottom - y) <= margin:
        return "bottom"
    return None

# Main loop
running = True
waiting = True
dragging = False
while running:
    screen.fill(WHITE)

    # Draw grid
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, GREY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GREY, (0, y), (WIDTH, y))

    # Draw existing walls
    for wall in walls:
        pygame.draw.rect(screen, GREY, wall)
        pygame.draw.rect(screen, BLACK, wall, 2)

    if dragging:
            mouse_pos = pygame.mouse.get_pos()
            end_pos = (
                snap_to_grid(mouse_pos[0], GRID_SIZE),
                snap_to_grid(mouse_pos[1], GRID_SIZE),
            )
            drawing_rect = (start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
            drawing_rect = normalize_rect(drawing_rect)
            #print(drawing_rect)
            pygame.draw.rect(screen, BLUE, drawing_rect, 2)

    # Draw instructions
    draw_instructions()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Start creating a rectangle
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and waiting:
            mouse_pos = pygame.mouse.get_pos()
            start_pos = (
                snap_to_grid(mouse_pos[0], GRID_SIZE),
                snap_to_grid(mouse_pos[1], GRID_SIZE),
            )
            #print("StartPos: ", start_pos)
            waiting = False
            dragging = True
        # End rectangle
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and dragging:
            mouse_pos = pygame.mouse.get_pos()
            end_pos = (
                snap_to_grid(mouse_pos[0], GRID_SIZE),
                snap_to_grid(mouse_pos[1], GRID_SIZE),
            )
            #print("EndPos: ", start_pos)
            current_rect = (start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
            print(current_rect)
            current_rect = normalize_rect(current_rect)
            print(current_rect)
            walls.append(current_rect)
            waiting = True
            dragging = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # Right click
            # Delete a wall if right-clicked
            mouse_pos = pygame.mouse.get_pos()
            for wall in walls:
                # Rectangle: (x, y, width, height)
                rect_x, rect_y, rect_width, rect_height = wall
                # Check if the mouse is inside the rectangle
                if rect_x <= mouse_pos[0] <= rect_x + rect_width and rect_y <= mouse_pos[1] <= rect_y + rect_height:
                    walls.remove(wall)
                    break

        # Save the maze layout
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                #save_maze_file()
                add_to_dict("Level.py", "levels", level_num)
            elif event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
