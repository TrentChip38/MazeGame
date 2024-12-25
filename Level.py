# Screen dimensions
WIDTH, HEIGHT = 800, 600
mid_top_goal = [WIDTH//2 -10, 0]
mid_right_goal = [WIDTH-20, HEIGHT//2 -10]
mid_bottom_goal = [WIDTH//2 - 10,HEIGHT-20]
mid_left_goal = [0, HEIGHT//2 -10]
middle_middle = [390, 290]

bigger_goal_size = 20
default_goal_size = 20

corner_start = [50, 50]
top_start = [390, 30]
bottom_start = [390, 550]
right_start = [750, 290]
left_start = [30, 290]

# Player starting positions
start_positions = {0:[390, 290], 1:[390, 560], 2:[20, 280]}

# Levels and Walls
import Colors as C
levels_color = {0: C.GREEN, 1:(140, 100, 100), 2:C.GREY, 3: C.GREY, 4: C.GREY, 42: C.GREY, 44: C.GREY, 14: C.GREY, 12: C.GREY, 55: C.GREY, 56: C.GREY}

level_goals = {
    0: {
        "goalN": {"pos": mid_top_goal, "sendtolevel": 1, "sendtopos": bottom_start, "color": C.GREEN, "size": 20},
        "goalE": {"pos": mid_right_goal, "sendtolevel": 2, "sendtopos": left_start, "color": C.GREEN, "size": 20},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 3, "sendtopos": top_start, "color": C.GREEN, "size": 20},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 4, "sendtopos": right_start, "color": C.GREEN, "size": 20},
    },
    1: {
        "goalN": {"pos": mid_top_goal, "sendtolevel": 11, "sendtopos": bottom_start, "color": C.GREY, "size": bigger_goal_size},
        "goalE": {"pos": mid_right_goal, "sendtolevel": 12, "sendtopos": left_start, "color": C.GREY, "size": bigger_goal_size},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 0, "sendtopos": top_start, "color": C.GREEN, "size": bigger_goal_size},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 14, "sendtopos": right_start, "color": C.GREY, "size": bigger_goal_size},
    },
    2: {
        "goalN": {"pos": mid_top_goal, "sendtolevel": 21, "sendtopos": bottom_start, "color": C.GREY, "size": 20},
        "goalE": {"pos": mid_right_goal, "sendtolevel": 22, "sendtopos": left_start, "color": C.GREY, "size": 20},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 23, "sendtopos": top_start, "color": C.GREY, "size": 20},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 0, "sendtopos": right_start, "color": C.GREEN, "size": 20},
    },
    3: {
        "goalN": {"pos": mid_top_goal, "sendtolevel": 0, "sendtopos": bottom_start, "color": C.GREEN, "size": 20},
        "goalE": {"pos": mid_right_goal, "sendtolevel": 32, "sendtopos": left_start, "color": C.GREY, "size": 20},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 33, "sendtopos": top_start, "color": C.GREY, "size": 20},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 34, "sendtopos": right_start, "color": C.GREY, "size": 20},
    },
    4: {
        "goalN": {"pos": mid_top_goal, "sendtolevel": 41, "sendtopos": bottom_start, "color": C.GREY, "size": 20},
        "goalE": {"pos": mid_right_goal, "sendtolevel": 0, "sendtopos": left_start, "color": C.GREEN, "size": 20},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 43, "sendtopos": top_start, "color": C.GREY, "size": 20},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 44, "sendtopos": right_start, "color": C.GREY, "size": 20},
    },
    14: {
        "goalE": {"pos": mid_bottom_goal, "sendtolevel": 4, "sendtopos": top_start, "color": C.GREY, "size": 20},
        "goalW": {"pos": mid_top_goal, "sendtolevel": 0, "sendtopos": middle_middle, "color": C.GREY, "size": 20},
    },
    12: {
        "goalS": {"pos": [WIDTH //2, HEIGHT], "sendtolevel": 2, "sendtopos": [50, 50], "color": C.GREY, "size": 20},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 1, "sendtopos": right_start, "color": C.GREY, "size": 20},
    },
    11: {
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 2, "sendtopos": top_start, "color": C.GREY, "size": 20},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 1, "sendtopos": right_start, "color": C.GREY, "size": 20},
    },
    55: {
        "goalN": {"pos": mid_top_goal, "sendtolevel": 1, "sendtopos": bottom_start, "color": C.GREY, "size": 20},
        "goalE": {"pos": mid_right_goal, "sendtolevel": 2, "sendtopos": left_start, "color": C.GREY, "size": 20},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 3, "sendtopos": top_start, "color": C.GREY, "size": 20},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 4, "sendtopos": right_start, "color": C.GREY, "size": 20},
    },
    56: {
        "goalN": {"pos": mid_top_goal, "sendtolevel": 1, "sendtopos": bottom_start, "color": C.GREY, "size": 20},
        "goalE": {"pos": mid_right_goal, "sendtolevel": 2, "sendtopos": left_start, "color": C.GREY, "size": 20},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 3, "sendtopos": top_start, "color": C.GREY, "size": 20},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 4, "sendtopos": right_start, "color": C.GREY, "size": 20},
    },
}


levels = {
    0: {
        # Level 0
        (0, 0, 380, 20), (420, 0, 380, 20), (780, 0, 20, 280), (780, 320, 20, 280),
        (0, 580, 380, 20), (420, 580, 380, 20), (0, 0, 20, 280), (0, 320, 20, 280),
    },
    1:{
        # Level 1
            # Outer walls
            (0, 0, 800, 20), (0, 580, 800, 20), (0, 0, 20, 600), (780, 0, 20, 600),

            # Inner maze walls
            (100, 100, 400, 20),       # Horizontal top center
            (100, 480, 400, 20), (100, 100, 20, 200),  (680, 100, 20, 200), (300, 100, 20, 200),
            (480, 300, 20, 200), (300, 300, 200, 20), (200, 200, 20, 200), (580, 200, 20, 200),
            (100, 300, 100, 20), (600, 300, 100, 20), (400, 100, 20, 200), (300, 400, 200, 20),
    },
    2:{
        # Level 2
        (50, 100, 400, 20), (200, 100, 20, 200), (400, 50, 20, 400), (600, 0, 20, 300),
        (300, 400, 200, 20), (700, 200, 20, 250), (100, 500, 300, 20), (500, 450, 200, 20),
        (150, 150, 200, 20), (500, 300, 100, 20), (550, 350, 20, 100),
    },
    3:{
        # Level 3
        (420, 0, 20, 200), (300, 100, 20, 300), (500, 0, 20, 400), (700, 200, 20, 200),
        (400, 500, 200, 20), (200, 300, 20, 200), (0, 100, 200, 20), (600, 100, 20, 200),
        (300, 500, 20, 100), (150, 400, 200, 20), (400, 400, 20, 100), (600, 300, 100, 20),
    },
    4:{
        # Level 4
        (0, 150, 600, 20), (700, 150, 20, 450), (600, 300, 20, 300), (400, 200, 200, 20),
        (300, 400, 200, 20), (100, 300, 200, 20), (0, 500, 300, 20), (0, 400, 20, 100),
        (100, 200, 20, 100), (400, 100, 200, 20), (600, 200, 20, 100),
    },
    13:{
        # Level 5
        (0, 100, 600, 20), (0, 200, 200, 20), (300, 100, 20, 300), (500, 100, 20, 400),
        (600, 400, 200, 20), (200, 300, 100, 20), (700, 150, 20, 350), (400, 500, 200, 20),
        (100, 400, 200, 20), (200, 200, 20, 100), (400, 300, 200, 20), (600, 200, 20, 100),
    },
    14:{
        # Level 6 (Final Level)
        (50, 100, 800, 20), (100, 100, 20, 400), (700, 50, 20, 500), (400, 0, 20, 250),
        (300, 300, 200, 20), (500, 200, 100, 20), (600, 300, 20, 200), (300, 400, 100, 20),
        (200, 200, 20, 100), (0, 500, 300, 20), (400, 400, 20, 100),
    },
    5:{
        # Weird grid
        (0, 0, 800, 20),           # Top wall
        (0, 580, 800, 20),         # Bottom wall
        (0, 0, 20, 600),           # Left wall
        (780, 0, 20, 600),         # Right wall

        # Horizontal walls
        (40, 80, 720, 20),         # Top horizontal
        (40, 160, 720, 20),        # 2nd horizontal
        (40, 240, 720, 20),        # 3rd horizontal
        (40, 320, 720, 20),        # 4th horizontal
        (40, 400, 720, 20),        # 5th horizontal
        (40, 480, 720, 20),        # Bottom horizontal

        # Vertical walls
        (80, 40, 20, 520),         # Left vertical
        (160, 40, 20, 520),        # 2nd vertical
        (240, 40, 20, 520),        # 3rd vertical
        (320, 40, 20, 520),        # 4th vertical
        (400, 40, 20, 520),        # Center vertical
        (480, 40, 20, 520),        # 6th vertical
        (560, 40, 20, 520),        # 7th vertical
        (640, 40, 20, 520),        # 8th vertical
        (720, 40, 20, 520),        # Right vertical
    },
    12:{
            # tighter grid
        (0, 0, 800, 20),           # Top wall
        (0, 580, 800, 20),         # Bottom wall
        (0, 0, 20, 600),           # Left wall
        (780, 0, 20, 600),         # Right wall

        # Horizontal walls
        (0, 60, 280, 20),          # Top horizontal
        (340, 60, 120, 20),
        (500, 60, 300, 20),
        (250, 120, 250, 20),       # 2nd horizontal
        (0, 120, 200, 20),
        (600, 120, 200, 20),        
        (100, 180, 250, 20),        # 3rd horizontal
        (450, 180, 250, 20),
        (200, 240, 300, 20),        # 4th horizontal
        (400, 300, 200, 20),        # 5th horizontal
        (200, 360, 400, 20),        # 6th horizontal
        (100, 420, 250, 20),        # 7th horizontal
        (450, 420, 250, 20),
        (250, 480, 250, 20),        # 8th horizontal
        (0, 480, 200, 20),
        (600, 480, 200, 20),
        (0, 540, 280, 20),        # Bottom horizontal
        (340, 540, 120, 20),
        (500, 540, 300, 20),

        # Vertical walls
        
        #(300, 400, 20, 200),        # 5th vertical
        #(540, 40, 20, 200),        # 9th vertical
        #(620, 200, 20, 200),        # 12th vertical
        #(780, 20, 20, 200),        # Right vertical
    },
    14:{
            # tighter grid
        (0, 0, 800, 10),           # Top wall
        (0, 590, 800, 10),         # Bottom wall
        (0, 0, 10, 600),           # Left wall
        (790, 0, 10, 600),         # Right wall

        # Horizontal walls
        (20, 60, 100, 20),         # Top horizontal
        (20, 120, 200, 20),        # 2nd horizontal
        (20, 180, 300, 20),        # 3rd horizontal
        (200, 240, 300, 20),        # 4th horizontal
        (400, 300, 200, 20),        # 5th horizontal
        (200, 360, 400, 20),        # 6th horizontal
        (100, 420, 100, 20),        # 7th horizontal
        (0, 480, 300, 20),        # 8th horizontal
        (0, 540, 500, 20),        # Bottom horizontal

        # Vertical walls
        (60, 40, 20, 200),         # 1st vertical
        (120, 0, 20, 200),        # 2nd vertical
        (180, 80, 20, 200),        # 3rd vertical
        (240, 00, 20, 200),        # 4th vertical
        (300, 40, 20, 200),        # 5th vertical
        (360, 80, 20, 200),        # 6th vertical
        (420, 0, 20, 200),        # Center vertical
        (480, 80, 20, 200),        # 8th vertical
        (540, 40, 20, 200),        # 9th vertical
        (600, 20, 20, 200),        # 10th vertical
        (660, 40, 20, 200),        # 11th vertical
        (720, 80, 20, 200),        # 12th vertical
        (780, 20, 20, 200),        # Right vertical
    },
    55:{
        # Outer walls
        (0, 0, 800, 20),           # Top wall
        (0, 580, 800, 20),         # Bottom wall
        (0, 0, 20, 600),           # Left wall
        (780, 0, 20, 600),         # Right wall

        # Horizontal walls
        (70, 80, 660, 20),         # Top horizontal
        (150, 160, 500, 20),        # 2nd horizontal
        (230, 240, 340, 20),        # 3rd horizontal
        #(310, 320, 180, 20),        # 4th horizontal
        (230, 340, 340, 20),        # 5th horizontal
        (150, 420, 500, 20),        # 5th horizontal
        (70, 500, 660, 20),        # Bottom horizontal

        # Vertical walls
        (70, 80, 20, 190),         # Left vertical
        (70, 330, 20, 190),
        (150, 160, 20, 280),        # 2nd vertical
        (230, 240, 20, 120),        # 3rd vertical
        #(310, 80, 20, 440),        # 4th vertical
        #(390, 80, 20, 460),        # Center vertical
        #(470, 80, 20, 440),        # 6th vertical
        (550, 240, 20, 120),        # 7th vertical
        (630, 160, 20, 280),        # 8th vertical
        (710, 80, 20, 180),        # Right vertical
        (710, 340, 20, 180), 
    },
    56:{
        (0, 0, 800, 20), (0, 590, 800, 20), (0, 0, 20, 600), (790, 0, 20, 600), (60, 60, 680, 20), 
        (120, 120, 560, 20), (180, 180, 440, 20), (240, 240, 320, 20), (300, 320, 200, 20), (240, 360, 320, 20), 
        (180, 420, 440, 20), (120, 480, 560, 20), (60, 540, 680, 20), (60, 60, 20, 500), (120, 120, 20, 380), 
        (180, 180, 20, 260), (240, 240, 20, 140), (300, 300, 20, 20), #(360, 360, 20, -100), (420, 360, 20, -100), 
        (480, 300, 20, 20), (540, 240, 20, 140), (600, 180, 20, 260), (660, 120, 20, 380), (720, 60, 20, 500)

    }
}