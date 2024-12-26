import pygame
import sys
import time
import maze_layout
# if event.type == pygame.MOUSEBUTTONDOWN:
#     print(f"Click registered at {event.pos}")
#     time.sleep(0.2)  # Pause for 200 milliseconds

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

# Grid size
GRID_SIZE = 10
# # Outer walls
#     (0, 0, 380, 20), (420, 0, 380, 20), (780, 0, 20, 280), (780, 320, 20, 280),
#         (0, 580, 380, 20), (420, 580, 380, 20), (0, 0, 20, 280), (0, 320, 20, 280),
# Variables
walls = [
    # Level 0
        (0, 0, 380, 20), (420, 0, 380, 20), (780, 0, 20, 280), (780, 320, 20, 280),
        (0, 580, 380, 20), (420, 580, 380, 20), (0, 0, 20, 280), (0, 320, 20, 280),
        (380, 0, 40, 20),(780, 280, 20, 40), (380, 580, 40, 20),(0, 280, 20, 40),
]
walls1 = []# Can use this with premade stuff
walls = maze_layout.walls #use this if you want to use previouse layout still in the file
dragging = False
resizing = False
current_rect = None
resize_rect = None
resize_side = None  # Keeps track of which side is being resized (e.g., "left", "top", etc.)

# Font for instructions
font = pygame.font.SysFont(None, 24)
instructions = [
    "Left-click and drag to create a wall.",
    "Right-click a wall to delete it.",
    "Drag edges to resize walls.",
    "Press 'S' to save the maze to a file.",
    "Press 'ESC' to exit.",
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
    x, y, width, height = rect
    if width < 0:
        x += width  # Shift x to the left
        width = abs(width)  # Make width positive
    if height < 0:
        y += height  # Shift y upward
        height = abs(height)  # Make height positive
    rect = (x, y, width, height)
    return rect

def save_maze(filename="maze_layout.py"):
    """Saves the maze layout to a Python file."""
    with open(filename, "w") as file:
        file.write("walls = [\n")
        num = 0
        for rect in walls:
            if True:#not any(items < 0 for items in rect):
                file.write(f"({rect[0]}, {rect[1]}, {rect[2]}, {rect[3]}),")
                num += 1
                if num == 6:
                    file.write(f"\n")
                    num = 0
        file.write("\n]\n")
    print(f"Maze layout saved to {filename}")

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
            #pygame.display.flip()

    # # Draw the rectangle being dragged or resized
    # if dragging and current_rect:
    #     pygame.draw.rect(screen, BLUE, current_rect, 2)
    # elif resizing and resize_rect:
    #     pygame.draw.rect(screen, RED, resize_rect, 2)

    # Draw instructions
    draw_instructions()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Start creating a rectangle
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and waiting:
            mouse_pos = pygame.mouse.get_pos()
            #print("Mouse: ", mouse_pos)
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
            #print("Mouse: ", mouse_pos)
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
        # # Start creating a rectangle
        # elif event.type == pygame.MOUSEBUTTONUP:
        #     if event.button == 1:  # Left click
        #         mouse_pos = pygame.mouse.get_pos()
        #         print("Mouse: ", mouse_pos)

        #         # Check if resizing an existing wall
        #         for wall in walls:
        #             resize_side = get_resize_side(wall, mouse_pos)
        #             if resize_side:
        #                 resize_rect = wall
        #                 resizing = True
        #                 break

        #         # Start creating a new wall
        #         if not resizing:
        #             start_pos = (
        #                 snap_to_grid(mouse_pos[0], GRID_SIZE),
        #                 snap_to_grid(mouse_pos[1], GRID_SIZE),
        #             )
        #             print("StartPos: ", start_pos)
        #             current_rect = pygame.Rect(start_pos[0], start_pos[1], 1, 1)
        #             dragging = True

        #     elif event.button == 3:  # Right click
        #         # Delete a wall if right-clicked
        #         mouse_pos = pygame.mouse.get_pos()
        #         for wall in walls:
        #             if wall.collidepoint(mouse_pos):
        #                 walls.remove(wall)
        #                 break

        # # Stop creating or resizing a rectangle
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 1:
        #         print("CurrentRect: ", current_rect)
        #         if dragging and current_rect:
        #             # Only add the rectangle if it has a significant size
        #             if current_rect.width > 5 and current_rect.height > 5:
        #                 walls.append(current_rect)
        #             current_rect = None
        #             dragging = False
        #         elif resizing:
        #             resize_rect = None
        #             resizing = False

        # # Adjust the rectangle size during drag
        # elif event.type == pygame.MOUSEMOTION:
        #     mouse_pos = pygame.mouse.get_pos()
        #     if dragging and current_rect:
        #         end_pos = (
        #             snap_to_grid(mouse_pos[0], GRID_SIZE),
        #             snap_to_grid(mouse_pos[1], GRID_SIZE),
        #         )
        #         print("EndPos", end_pos)
        #         current_rect.width = abs(end_pos[0] - current_rect.x)
        #         current_rect.height = abs(end_pos[1] - current_rect.y)
        #         current_rect.x = min(end_pos[0], current_rect.x)
        #         current_rect.y = min(end_pos[1], current_rect.y)
        #     elif resizing and resize_rect:
        #         if resize_side == "left":
        #             resize_rect.width += resize_rect.x - mouse_pos[0]
        #             resize_rect.x = snap_to_grid(mouse_pos[0], GRID_SIZE)
        #         elif resize_side == "right":
        #             resize_rect.width = snap_to_grid(mouse_pos[0], GRID_SIZE) - resize_rect.x
        #         elif resize_side == "top":
        #             resize_rect.height += resize_rect.y - mouse_pos[1]
        #             resize_rect.y = snap_to_grid(mouse_pos[1], GRID_SIZE)
        #         elif resize_side == "bottom":
        #             resize_rect.height = snap_to_grid(mouse_pos[1], GRID_SIZE) - resize_rect.y

        # Save the maze layout
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                save_maze()
            elif event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.flip()
    #time.sleep(0.2)  # Pause for 200 milliseconds

# Quit Pygame
pygame.quit()
sys.exit()
