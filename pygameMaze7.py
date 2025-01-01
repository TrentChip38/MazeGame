import pygame
import sys
import random
import math
import Colors as C
import Level

# Initialize Pygame
pygame.init()

WIDTH = Level.WIDTH
HEIGHT = Level.HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Runner")

#Money for power ups
dev_mode_cheats = True

# Player settings
player_size = 20
default_player_speed = 5
player_speed = default_player_speed

speed_boost_toggle = 0
dev_cost_divider = 1
# Timer and Score
timer = 60  # 60 seconds per level (unused)
score = 0

#Power ups
player_power = []
extra_lives = ["extralife", "extralife1", "extralife2", "extralife3", "extralife4"]
#Stuff for maps
is_explored = False
#powerup settings
speed_boost1_attained = False
#Enemy settings
enemy_speed = 8
default_enemy_amount = 4

# Visibility settings
Darkness_on = True
# Default
vis_radius = 2
vis_y_left = vis_radius - 1
vis_y_right = vis_radius + 1
vis_x_left = vis_y_left
vis_x_right = vis_y_right
#print(vis_x_left)
#print(vis_x_right)

# Goal settings
goal_size = 30

# Coin settings
coin_size = 15
coin_count = 5
default_coin_count = 5

# Enemy settings
enemy_size = 20

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Beginning level
current_level = 0
coins = []
enemies = []
global start_position
start_position = [390, 290]

#Set test mode stuff on
if dev_mode_cheats:
    Darkness_on = True
    #vis_radius = 6
    score = 10000
    #current_level = 0
    #start_position = [760, 290]#Custom start
    #start_position = [40, 290]

# Tracking explored positions (2D array)
explored = [[False for _ in range(WIDTH // 40)] for _ in range(HEIGHT // 40)]

def update_speed():
    pass




def reset_level():
    global player_pos, coins, enemies, timer, explored
    player_pos = start_position
    print("player position: ", player_pos)
    #Level.start_positions[current_level]
    #print(Level.start_positions[current_level])
    #print(start_position)
    coins.clear()
    enemies.clear()
    #Add map if level mostly explored?
    
    # Reset explored areas for the new level
    explored = [[False for _ in range(WIDTH // 40)] for _ in range(HEIGHT // 40)]

    # Generate coins
    coin_count = default_coin_count
    if current_level in Level.levels_coins:
        coin_count = Level.levels_coins[current_level]
    for _ in range(coin_count):
        while True:
            coin = [random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)]
            coin_rect = pygame.Rect(coin[0], coin[1], coin_size, coin_size)
            wall_rects = [pygame.Rect(wall) for wall in Level.levels[current_level]]
            if not any(coin_rect.colliderect(wall_rect) for wall_rect in wall_rects):
                coins.append(coin)
                break

    # Generate enemies
    enemy_amount = default_enemy_amount
    #unless there is a specified amount on that level
    if current_level in Level.levels_enemies:
        enemy_amount = Level.levels_enemies[current_level]
    for _ in range(enemy_amount):#current_level + 2
        while True:
            enemy = [
                #Position
                random.randint(100, WIDTH - 100),
                random.randint(100, HEIGHT - 100),
                #Velocity vecctors for diagnol (now unused)
                random.choice([-2, 2]),
                random.choice([-2, 2]),
                #Direction vectors for up, right, down, left
                random.randint(0, 3),
            ]
            enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size)
            wall_rects = [pygame.Rect(wall) for wall in Level.levels[current_level]]
            if not any(enemy_rect.colliderect(wall_rect) for wall_rect in wall_rects):
                enemies.append(enemy)
                break
    timer = 60  # Reset timer

# Function to draw everything
def draw_game():
    # Clear screen with gray background
    if current_level in Level.levels_color:
        color = Level.levels_color[current_level]
    else:
        color = C.GREY
    screen.fill(color)

    # Draw walls (walls are always black)
    for wall in Level.levels[current_level]:
        pygame.draw.rect(screen, C.WALL_BLACK, wall)

    # Draw goal
    for goal_name, goal in Level.level_goals[current_level].items():
        goal_rect = pygame.Rect(goal["pos"][0], goal["pos"][1], goal["size"], goal["size"])
        pygame.draw.rect(screen, goal["color"], goal_rect)

    # Draw coins
    for coin in coins:
        pygame.draw.circle(screen, C.YELLOW, (coin[0], coin[1]), coin_size // 2)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, C.RED, (enemy[0], enemy[1], enemy_size, enemy_size))
    
    # Draw unexplored areas in black
    if current_level == 0 or Darkness_on == False or is_explored:
        #don't draw
        pass
    else:
        for row in range(HEIGHT // 40):
            for col in range(WIDTH // 40):
                if explored[row][col] == False:
                    pygame.draw.rect(screen, C.BLACK, (col * 40, row * 40, 40, 40))

    # Draw player
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    pygame.draw.rect(screen, C.BLUE, player_rect)

    # Draw timer and score
    font = pygame.font.SysFont(None, 36)
    #timer_text = font.render(f"Time: {int(timer)}", True, BLACK)
    level_text = font.render(f"Level: {current_level}", True, C.BLACK)
    score_text = font.render(f"Score: {score}", True, C.BLACK)
    #screen.blit(timer_text, (10, 10))
    screen.blit(level_text, (10, 10))
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

# Main game loop------------------------------
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
    #Power up toggling
    if "speedboost10" in player_power:
        if keys[pygame.K_m] or keys[pygame.K_e]:
            if speed_boost_toggle:
                speed_boost_toggle = 0
                player_speed = default_player_speed
            else:
                speed_boost_toggle = 1
                player_speed = 10
    #updating speed
    if "speedboost1" in player_power and speed_boost1_attained == False:
        player_speed += 1
        speed_boost1_attained = True
    # Default to 2
    vis_radius = 2
    #vision
    if "vision4" in player_power:
        vis_radius += 2
    if "vision6" in player_power:
        vis_radius += 2
    vis_y_left = vis_radius # -1
    vis_y_right = vis_radius + 1
    vis_x_left = vis_y_left
    vis_x_right = vis_y_right

    # Move player with collision detection
    wall_rects = [pygame.Rect(wall) for wall in Level.levels[current_level]]
    
    # Check wall collision
    new_pos = [player_pos[0] + dx, player_pos[1] + dy]
    new_rect = pygame.Rect(new_pos[0], new_pos[1], player_size, player_size)
    # Check if collide with wall at
    if not any(new_rect.colliderect(wall_rect) for wall_rect in wall_rects):
        player_pos = new_pos
    else:
        # Handle horizontal and verticle movement seperate
        if dx != 0:
            for step in range(abs(dx), 0, -1):
                #Try full movement but if not then decrement it
                new_dx = dx // abs(dx) * step
                new_pos_x = player_pos[0] + new_dx
                new_rect_x = pygame.Rect(new_pos_x, player_pos[1], player_size, player_size)
                if not any(new_rect_x.colliderect(wall_rect) for wall_rect in wall_rects):
                    #If you won't hit any walls then move there
                    player_pos[0] = new_pos_x
                    break
        if dy != 0:
            for step in range(abs(dy), 0, -1):
                new_dy = dy // abs(dy) * step
                new_pos_y = player_pos[1] + new_dy
                new_rect_y = pygame.Rect(player_pos[0], new_pos_y, player_size, player_size)
                if not any(new_rect_y.colliderect(wall_rect) for wall_rect in wall_rects):
                    player_pos[1] = new_pos_y
                    break

    # Update explored areas
    update_explored()


    #Check for hitting goals
    for goal_name, goal in Level.level_goals[current_level].items():
        goal_rect = pygame.Rect(goal["pos"][0], goal["pos"][1], goal["size"], goal["size"])

        if new_rect.colliderect(goal_rect):
            if "sendtolevel" in goal:
                print(f"Player reached {goal_name}! Moving to level {goal['sendtolevel']}.")
            #score += 100
            #Add power or attribute to player
            if "addpower" in goal:
                if not goal["addpower"] in player_power:
                    if "cost" in goal:
                        if score >= goal["cost"]//dev_cost_divider:
                            player_power.append(goal["addpower"])
                            score -= goal["cost"]
                    else:
                        player_power.append(goal["addpower"])
            #Move if send to pos defined in goal
            if "sendtolevel" in goal:
                if goal["sendtolevel"] in Level.levels:
                    current_level = goal["sendtolevel"]
                else:
                    current_level = 55 #the ghost level
                start_position = goal["sendtopos"]
                reset_level()
                print("player pos after goal: ", player_pos)

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
        wall_rects = [pygame.Rect(wall) for wall in Level.levels[current_level]]
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
            #No extra life, you reset
            if not any(item in player_power for item in extra_lives):
                #running = False
                score -= 50
                current_level = 0
                start_position = [390, 290]
                reset_level()
            else:
                #Check for extra life
                for extra_life in extra_lives:
                    if extra_life in player_power:
                        #Extra life saves you and get rid of that enemy
                        print("Enemy collision. Saved")
                        player_power.remove(extra_life)
                        if enemy in enemies:
                            enemies.remove(enemy)
                        print("Enemy collision. Reset")
                        break
            
                


    # Draw game
    draw_game()

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
