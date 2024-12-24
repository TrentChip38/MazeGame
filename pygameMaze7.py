import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Runner")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WALL_BLACK = (50, 50, 10)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (100, 100, 100)

# Player settings
player_size = 20
player_speed = 5

enemy_speed = 8

# Visibility settings
vis_radius = 2
vis_y_left = vis_radius - 1
vis_y_right = vis_radius + 1
vis_x_left = vis_y_left
vis_x_right = vis_y_right
#print(vis_x_left)
#print(vis_x_right)

import Level
# Goal settings
goal_size = 30

# Coin settings
coin_size = 15
coin_count = 5

# Enemy settings
enemy_size = 20


# level_goals = {
#     f"Goal {i+1}":{
#         "pos": [WIDTH //2, 0],
#         "sendto": 0,
#         "sendtopos": [WIDTH //2, HEIGHT]
#     }
# }



# Timer and Score
timer = 60  # 60 seconds per level
score = 0

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Reset level
current_level = 0
coins = []
enemies = []

# Tracking explored positions (2D array)
explored = [[False for _ in range(WIDTH // 40)] for _ in range(HEIGHT // 40)]

def reset_level():
    global player_pos, coins, enemies, timer, explored
    player_pos = start_positions[current_level]
    coins.clear()
    enemies.clear()

    # Reset explored areas for the new level
    explored = [[False for _ in range(WIDTH // 40)] for _ in range(HEIGHT // 40)]

    # Generate coins
    for _ in range(coin_count):
        while True:
            coin = [random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)]
            coin_rect = pygame.Rect(coin[0], coin[1], coin_size, coin_size)
            wall_rects = [pygame.Rect(wall) for wall in levels[current_level]]
            if not any(coin_rect.colliderect(wall_rect) for wall_rect in wall_rects):
                coins.append(coin)
                break

    # Generate enemies
    for _ in range(current_level + 2):
        while True:
            enemy = [
                #Position
                random.randint(100, WIDTH - 100),
                random.randint(100, HEIGHT - 100),
                #Velocity vecctors for diagnol
                random.choice([-2, 2]),
                random.choice([-2, 2]),
                #Direction vectors for hor/vert
                random.randint(0, 3),
            ]
            enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size)
            wall_rects = [pygame.Rect(wall) for wall in levels[current_level]]
            if not any(enemy_rect.colliderect(wall_rect) for wall_rect in wall_rects):
                enemies.append(enemy)
                break

    timer = 60  # Reset timer

# Function to draw everything
def draw_game():
    # Clear screen with gray background
    color = levels_color[current_level]
    screen.fill(color)

    # Draw walls (walls are always black)
    for wall in levels[current_level]:
        pygame.draw.rect(screen, WALL_BLACK, wall)

    # Draw goal
    if current_level == 0:
        for goal in levelZeroGoals.values():
            goal_rect = pygame.Rect(goal["pos"][0], goal["pos"][1], goal["size"], goal["size"])
            pygame.draw.rect(screen, goal["color"], goal_rect)
    else:
        goal_pos = [WIDTH - 50, HEIGHT - 50]
        goal_rect = pygame.Rect(goal_pos[0], goal_pos[1], goal_size, goal_size)
        pygame.draw.rect(screen, GREEN, goal_rect)

    # Draw coins
    for coin in coins:
        pygame.draw.circle(screen, YELLOW, (coin[0], coin[1]), coin_size // 2)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))
    
    # Draw unexplored areas in black
    if current_level == 0:
        #don't draw
        pass
    else:
        for row in range(HEIGHT // 40):
            for col in range(WIDTH // 40):
                if explored[row][col] == False:
                    pygame.draw.rect(screen, BLACK, (col * 40, row * 40, 40, 40))

    # Draw player
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    pygame.draw.rect(screen, BLUE, player_rect)

    # Draw timer and score
    font = pygame.font.SysFont(None, 36)
    #timer_text = font.render(f"Time: {int(timer)}", True, BLACK)
    score_text = font.render(f"Score: {score}", True, BLACK)
    #screen.blit(timer_text, (10, 10))
    screen.blit(score_text, (10, 50))

def update_explored():
    """Mark the area around the player as explored."""
    player_row = player_pos[1] // 40
    player_col = player_pos[0] // 40
    for dy in range(-vis_y_left, vis_y_right):  # 3x3 grid around the player
        for dx in range(-vis_y_left, vis_x_right):
            row = player_row + dy
            col = player_col + dx
            if 0 <= row < HEIGHT // 40 and 0 <= col < WIDTH // 40:
                explored[row][col] = True

# Initialize the first level
reset_level()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Timer
    # timer -= clock.get_time() / 1000
    # if timer <= 0:
    #     print("Time's up! Game Over!")
    #     running = False

    # Player movement
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:
        dx -= player_speed
    elif keys[pygame.K_a]:
        dx -= player_speed
    if keys[pygame.K_RIGHT]:
        dx += player_speed
    elif keys[pygame.K_d]:
        dx += player_speed
    if keys[pygame.K_UP]:
        dy -= player_speed
    elif keys[pygame.K_w]:
        dy -= player_speed
    if keys[pygame.K_DOWN]:
          dy += player_speed
    elif keys[pygame.K_s]:
            dy += player_speed

    # Move player with collision detection
    new_pos = [player_pos[0] + dx, player_pos[1] + dy]
    new_rect = pygame.Rect(new_pos[0], new_pos[1], player_size, player_size)
    wall_rects = [pygame.Rect(wall) for wall in levels[current_level]]
    if not any(new_rect.colliderect(wall_rect) for wall_rect in wall_rects):
        player_pos = new_pos

    # Update explored areas
    update_explored()

    # Check for reaching the gates on level 1
    if current_level == 0:
        for goal_name, goal in levelZeroGoals.items():
            #print(f"{goal_name}: {goal}")
            goal_rect = pygame.Rect(goal["pos"][0], goal["pos"][1], goal["size"], goal["size"])
            #pygame.draw.rect(screen, goal["color"], goal_rect)
            if new_rect.colliderect(goal_rect):
                score += 100
                current_level = goal["sendtolevel"]
                reset_level()

    # Check for reaching the goal
    goal_rect = pygame.Rect(WIDTH - 50, HEIGHT - 50, goal_size, goal_size)
    if new_rect.colliderect(goal_rect):
        score += 100
        current_level += 1
        if current_level >= len(levels):
            print("You win!")
            running = False
        else:
            reset_level()

    # Check for coin collection
    for coin in coins[:]:
        coin_rect = pygame.Rect(coin[0], coin[1], coin_size, coin_size)
        if new_rect.colliderect(coin_rect):
            coins.remove(coin)
            score += 10

    # Move enemies
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size)

        # Check wall collision and proximity
        wall_rects = [pygame.Rect(wall) for wall in levels[current_level]]
        step_back = 0#Thought this would be needed, but it breaks it
        proximity_margin = 5  # Adjust margin for better detection
        wall_proximity = False

        while True:
            # Create an expanded rectangle for proximity check based on direction
            if enemy[4] == 0:  # Up
                proximity_rect = enemy_rect.inflate(0, proximity_margin * 2)
                proximity_rect.top -= proximity_margin
            elif enemy[4] == 1:  # Right
                proximity_rect = enemy_rect.inflate(proximity_margin * 2, 0)
                proximity_rect.left += proximity_margin
            elif enemy[4] == 2:  # Down
                proximity_rect = enemy_rect.inflate(0, proximity_margin * 2)
                proximity_rect.bottom += proximity_margin
            elif enemy[4] == 3:  # Left
                proximity_rect = enemy_rect.inflate(proximity_margin * 2, 0)
                proximity_rect.right -= proximity_margin

            # Check if any walls are within the proximity area
            wall_proximity = any(proximity_rect.colliderect(wall_rect) for wall_rect in wall_rects)

            if not wall_proximity:
                break  # If no walls in the way, exit the loop

            # Handle wall collision based on direction and adjust path
            if enemy[4] == 0:  # Was going up
                enemy[1] += step_back  # Step back from wall
                enemy[4] = random.choice([3, 1])  # Choose a new direction (left or right)
            elif enemy[4] == 1:  # Was going right
                enemy[0] -= step_back  # Step back from wall
                enemy[4] = random.choice([2, 0])  # Choose a new direction (down or up)
            elif enemy[4] == 2:  # Was going down
                enemy[1] -= step_back  # Step back from wall
                enemy[4] = random.choice([3, 1])  # Choose a new direction (left or right)
            elif enemy[4] == 3:  # Was going left
                enemy[0] += step_back  # Step back from wall
                enemy[4] = random.choice([2, 0])  # Choose a new direction (down or up)

        # Screen edge collision
        if enemy[0] <= 0:
            enemy[4] = 1
        if enemy[0] >= WIDTH - enemy_size:
            enemy[4] = 3
        if enemy[1] <= 0:
            enemy[4] = 2
        if enemy[1] >= HEIGHT - enemy_size:
            enemy[4] = 0

        # Move in the current direction
        if enemy[4] == 0:  # Up
            enemy[1] -= enemy_speed
        elif enemy[4] == 1:  # Right
            enemy[0] += enemy_speed
        elif enemy[4] == 2:  # Down
            enemy[1] += enemy_speed
        elif enemy[4] == 3:  # Left
            enemy[0] -= enemy_speed

        # Player collision
        if new_rect.colliderect(enemy_rect):
            print("Game Over! Enemy collision.")
            running = False

    # Draw game
    draw_game()

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
