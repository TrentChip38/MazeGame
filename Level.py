

starter_shop = {




}






# Screen dimensions
WIDTH, HEIGHT = 800, 600
mid_top_goal = [WIDTH//2 -20, -20]
mid_right_goal = [WIDTH-20, HEIGHT//2 -20]
mid_bottom_goal = [WIDTH//2 - 20,HEIGHT-20]
mid_left_goal = [-20, HEIGHT//2 -20]

# mid_top_goal_big = [WIDTH//2 -10, 0]
# mid_right_goal_big = [WIDTH-20, HEIGHT//2 -10]
# mid_bottom_goal_big = [WIDTH//2 - 10,HEIGHT-20]
# mid_left_goal_big = [0, HEIGHT//2 -10]

mid_top_goal_thin = [WIDTH//2 -10, -10]
mid_right_goal_thin = [WIDTH +10, HEIGHT//2]
mid_bottom_goal_thin = [WIDTH//2 - 10, HEIGHT+10]
mid_left_goal_thin = [-10, HEIGHT//2 -10]

middle_middle = [390, 290]

bigger_goal_size = 40
default_goal_size = 40

corner_start = [50, 50]
top_start = [390, 30]
bottom_start = [390, 550]
right_start = [750, 290]
left_start = [30, 290]

# Player starting positions
start_positions = {0:[390, 290], 1:[390, 560], 2:[20, 280]}

# Levels and Walls
import Colors as C
levels_color = {0: C.GREEN, 1:(140, 100, 100), 2:C.GREY, 3: C.GREY, 4: C.GREY, 42: C.GREY, 44: C.GREY, 14: C.GREY, 12: C.GREY, 55: C.GREY, 56: C.GREY, 57: C.GREY}
levels_enemies = {0: 0, 141: 10}

level_goals = {
    0: {
        "goalN": {"pos": mid_top_goal, "sendtolevel": 1, "sendtopos": bottom_start, "color": C.GREEN, "size": default_goal_size},
        "goalE": {"pos": mid_right_goal, "sendtolevel": 2, "sendtopos": left_start, "color": C.GREEN, "size": default_goal_size},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 3, "sendtopos": top_start, "color": C.GREEN, "size": default_goal_size},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 4, "sendtopos": right_start, "color": C.GREEN, "size": default_goal_size},
        "shop_1": {"pos": [50, 60], "addpower": "extralife1", "cost": 100,"color": C.YELLOW, "size": 20},
        "shop_2": {"pos": [50, 100], "addpower": "speedboost1", "cost": 100, "color": C.BLUE, "size": 20},
        "shop_3": {"pos": [50, 140], "addpower": "speedboost10", "cost": 2000, "color": C.CYAN, "size": 20},
        "shop_4": {"pos": [50, 180], "addpower": "vision4", "cost": 500, "color": C.BROWN, "size": 20},
        #"shop_5": {"pos": [50, 220], "addpower": "vision8", "cost": 2000, "color": C.CYAN, "size": 20},
    },
    1: {
        "goalN": {"pos": mid_top_goal, "sendtolevel": 11, "sendtopos": bottom_start, "color": C.GREY, "size": bigger_goal_size},
        "goalE": {"pos": mid_right_goal, "sendtolevel": 12, "sendtopos": left_start, "color": C.GREY, "size": bigger_goal_size},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 0, "sendtopos": top_start, "color": C.GREEN, "size": bigger_goal_size},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 14, "sendtopos": right_start, "color": C.GREY, "size": bigger_goal_size},
    },
    2: {
        "goalN": {"pos": mid_top_goal, "sendtolevel": 21, "sendtopos": bottom_start, "color": C.GREY, "size": default_goal_size},
        "goalE": {"pos": mid_right_goal, "sendtolevel": 22, "sendtopos": left_start, "color": C.GREY, "size": default_goal_size},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 23, "sendtopos": top_start, "color": C.GREY, "size": default_goal_size},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 0, "sendtopos": right_start, "color": C.GREEN, "size": default_goal_size},
    },
    3: {
        "goalN": {"pos": mid_top_goal, "sendtolevel": 0, "sendtopos": bottom_start, "color": C.GREEN, "size": default_goal_size},
        "goalE": {"pos": mid_right_goal, "sendtolevel": 32, "sendtopos": left_start, "color": C.GREY, "size": default_goal_size},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 33, "sendtopos": top_start, "color": C.GREY, "size": default_goal_size},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 34, "sendtopos": right_start, "color": C.GREY, "size": default_goal_size},
    },
    4: {
        "goalN": {"pos": mid_top_goal, "sendtolevel": 41, "sendtopos": bottom_start, "color": C.GREY, "size": default_goal_size},
        "goalE": {"pos": mid_right_goal, "sendtolevel": 0, "sendtopos": left_start, "color": C.GREEN, "size": default_goal_size},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 43, "sendtopos": top_start, "color": C.GREY, "size": default_goal_size},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 44, "sendtopos": right_start, "color": C.GREY, "size": default_goal_size},
    },
    14: {
        "goalE": {"pos": mid_bottom_goal, "sendtolevel": 4, "sendtopos": top_start, "color": C.GREY, "size": default_goal_size},
        "goalN": {"pos": mid_top_goal, "sendtolevel": 141, "sendtopos": [390, 560], "color": C.GREY, "size": default_goal_size},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 56, "sendtopos": top_start, "color": C.GREY, "size": default_goal_size},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 55, "sendtopos": right_start, "color": C.GREY, "size": default_goal_size},
        "goalP": {"pos": [90, 100], "addpower": "extralife", "color": C.YELLOW, "size": 20},
    },
    12: {
        "goalN": {"pos": mid_top_goal, "sendtolevel": 56, "sendtopos": bottom_start, "color": C.GREY, "size": default_goal_size},
        "goalE": {"pos": mid_bottom_goal, "sendtolevel": 57, "sendtopos": middle_middle, "color": C.GREY, "size": default_goal_size},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 2, "sendtopos": top_start, "color": C.GREY, "size": default_goal_size},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 1, "sendtopos": right_start, "color": C.GREY, "size": default_goal_size},
    },
    11: {
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 2, "sendtopos": top_start, "color": C.GREY, "size": default_goal_size},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 1, "sendtopos": right_start, "color": C.GREY, "size": default_goal_size},
    },
    141: {
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 14, "sendtopos": top_start, "color": C.GREY, "size": default_goal_size},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 1414, "sendtopos": right_start, "color": C.GREY, "size": default_goal_size},
    },
    1414: {
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 0, "sendtopos": corner_start, "color": C.GREEN, "size": default_goal_size},
        "goalW": {"pos": mid_right_goal, "sendtolevel": 141, "sendtopos": [20, 290], "color": C.GREY, "size": default_goal_size},
        "shop_3": {"pos": [250, 400], "addpower": "speedboost10", "cost": 200, "color": C.CYAN, "size": 20},
    },
    21:{
        "goalN": {"pos": mid_top_goal, "sendtolevel": 0, "sendtopos": bottom_start, "color": C.GREEN, "size": default_goal_size},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 2, "sendtopos": top_start, "color": C.GREY, "size": default_goal_size},
    },
    22:{
        "goalN": {"pos": mid_top_goal, "sendtolevel": 221, "sendtopos": bottom_start, "color": C.GREY, "size": bigger_goal_size},
        "goalE": {"pos": mid_right_goal, "sendtolevel": 222, "sendtopos": left_start, "color": C.GREY, "size": bigger_goal_size},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 223, "sendtopos": top_start, "color": C.GREY, "size": bigger_goal_size},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 2, "sendtopos": right_start, "color": C.GREY, "size": bigger_goal_size},
    },
    221:{
        #"goalN": {"pos": mid_top_goal, "sendtolevel": 2211, "sendtopos": bottom_start, "color": C.GREY, "size": bigger_goal_size},
        #"goalE": {"pos": mid_right_goal, "sendtolevel": 2212, "sendtopos": left_start, "color": C.GREY, "size": bigger_goal_size},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 22, "sendtopos": top_start, "color": C.GREY, "size": bigger_goal_size},
        #"goalW": {"pos": mid_left_goal, "sendtolevel": 2214, "sendtopos": right_start, "color": C.GREY, "size": bigger_goal_size},
    },
    222:{
        #"goalN": {"pos": mid_top_goal, "sendtolevel": 2221, "sendtopos": bottom_start, "color": C.GREY, "size": bigger_goal_size},
        #"goalE": {"pos": mid_right_goal, "sendtolevel": 2222, "sendtopos": left_start, "color": C.GREY, "size": bigger_goal_size},
        #"goalS": {"pos": mid_bottom_goal, "sendtolevel": 2223, "sendtopos": top_start, "color": C.GREEN, "size": bigger_goal_size},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 22, "sendtopos": right_start, "color": C.GREY, "size": bigger_goal_size},
    },
    223:{
        "goalN": {"pos": mid_top_goal, "sendtolevel": 22, "sendtopos": bottom_start, "color": C.GREY, "size": bigger_goal_size},
        #"goalE": {"pos": mid_right_goal, "sendtolevel": 2222, "sendtopos": left_start, "color": C.GREY, "size": bigger_goal_size},
        #"goalS": {"pos": mid_bottom_goal, "sendtolevel": 2223, "sendtopos": top_start, "color": C.GREEN, "size": bigger_goal_size},
        #"goalW": {"pos": mid_left_goal, "sendtolevel": 2224, "sendtopos": right_start, "color": C.GREY, "size": bigger_goal_size},
    },
    32:{
        "goalN": {"pos": mid_top_goal, "sendtolevel": 11, "sendtopos": bottom_start, "color": C.GREY, "size": bigger_goal_size},
        "goalE": {"pos": mid_right_goal, "sendtolevel": 12, "sendtopos": left_start, "color": C.GREY, "size": bigger_goal_size},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 0, "sendtopos": top_start, "color": C.GREEN, "size": bigger_goal_size},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 14, "sendtopos": right_start, "color": C.GREY, "size": bigger_goal_size},
    },
    55: {
        "goalN": {"pos": mid_top_goal, "sendtolevel": 1, "sendtopos": bottom_start, "color": C.GREY, "size": default_goal_size},
        "goalE": {"pos": mid_right_goal, "sendtolevel": 2, "sendtopos": left_start, "color": C.GREY, "size": default_goal_size},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 3, "sendtopos": top_start, "color": C.GREY, "size": default_goal_size},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 4, "sendtopos": right_start, "color": C.GREY, "size": default_goal_size},
        "goalP": {"pos": [360, 290], "addpower": "extralife2", "color": C.YELLOW, "size": 20},
    },
    56: {
        "goalN": {"pos": mid_top_goal, "sendtolevel": 1, "sendtopos": bottom_start, "color": C.GREY, "size": default_goal_size},
        "goalE": {"pos": mid_right_goal, "sendtolevel": 2, "sendtopos": left_start, "color": C.GREY, "size": default_goal_size},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 3, "sendtopos": top_start, "color": C.GREY, "size": default_goal_size},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 4, "sendtopos": right_start, "color": C.GREY, "size": default_goal_size},
    },
    57: {
        "goalN": {"pos": mid_top_goal_thin, "sendtolevel": 1, "sendtopos": bottom_start, "color": C.GREY, "size": 20},
        "goalE": {"pos": mid_right_goal_thin, "sendtolevel": 2, "sendtopos": left_start, "color": C.GREY, "size": 20},
        "goalS": {"pos": mid_bottom_goal_thin, "sendtolevel": 3, "sendtopos": top_start, "color": C.GREY, "size": 20},
        "goalW": {"pos": mid_left_goal_thin, "sendtolevel": 4, "sendtopos": right_start, "color": C.GREY, "size": 20},
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
        (0, 0, 800, 20), (0, 580, 800, 20), (0, 0, 20, 600), (780, 0, 20, 600),# Outer walls
        (50, 100, 400, 20), (200, 100, 20, 200), (400, 50, 20, 400), (600, 0, 20, 300),
        (300, 400, 200, 20), (700, 200, 20, 250), (100, 500, 300, 20), (500, 450, 200, 20),
        (150, 150, 200, 20), (500, 300, 100, 20), (550, 350, 20, 100),
    },
    3:{
        # Level 3
        (0, 0, 800, 20), (0, 580, 800, 20), (0, 0, 20, 600), (780, 0, 20, 600),# Outer walls
        (420, 0, 20, 200), (300, 100, 20, 300), (500, 0, 20, 400), (700, 200, 20, 200),
        (400, 500, 200, 20), (200, 300, 20, 200), (0, 100, 200, 20), (600, 100, 20, 200),
        (300, 500, 20, 100), (150, 400, 200, 20), (400, 400, 20, 100), (600, 300, 100, 20),
    },
    4:{
        # Level 4
        (0, 0, 800, 20), (0, 580, 800, 20), (0, 0, 20, 600), (780, 0, 20, 600),# Outer walls
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
    21:{
        # Level 14
        (0, 0, 800, 20), (0, 580, 800, 20), (0, 0, 20, 600), (780, 0, 20, 600),# Outer walls
        (50, 100, 800, 20), (100, 100, 20, 400), (700, 50, 20, 500), (400, 0, 20, 250),
        (300, 300, 200, 20), (500, 200, 100, 20), (600, 300, 20, 200), (300, 400, 100, 20),
        (200, 200, 20, 100), (0, 500, 300, 20), (400, 400, 20, 100),
    },
    22:{
    (0, 0, 380, 20),(420, 0, 380, 20),(780, 0, 20, 280),(0, 580, 380, 20),(0, 0, 20, 280),
    (0, 320, 20, 280),(420, 20, 0, 0),(420, 20, 0, 0),(60, 60, 20, 220),(120, 60, 20, 220),(180, 60, 20, 220),
    (240, 60, 20, 220),(300, 60, 20, 220),(360, 60, 20, 220),(420, 60, 20, 220),(480, 60, 20, 220),
    (540, 60, 20, 220),(600, 60, 20, 220),(660, 60, 20, 220),(720, 60, 20, 220),(60, 320, 20, 220),(120, 320, 20, 220),
    (180, 320, 20, 220),(240, 320, 20, 220),(300, 320, 20, 220),(360, 320, 20, 220),(420, 320, 20, 220),(480, 320, 20, 220),
    (540, 320, 20, 220),(600, 320, 20, 220),(660, 320, 20, 220),(720, 320, 20, 220),(420, 580, 380, 20),(780, 320, 20, 280),
    },
    221:{
    (0, 0, 380, 20),(420, 0, 380, 20),(780, 0, 20, 280),(0, 580, 380, 20),(380, 0, 40, 20),(780, 280, 20, 40),
    (380, 580, 40, 20),(0, 280, 20, 40),(0, 0, 20, 280),(0, 320, 20, 280),(420, 20, 0, 0),(420, 20, 0, 0),
    (60, 60, 20, 220),(120, 60, 20, 220),(240, 60, 20, 220),(360, 60, 20, 220),(420, 60, 20, 220),(600, 60, 20, 220),
    (60, 320, 20, 220),(120, 320, 20, 220),(180, 320, 20, 220),(420, 320, 20, 220),(600, 320, 20, 220),(720, 320, 20, 220),
    (420, 580, 380, 20),(780, 320, 20, 280),(80, 60, 40, 20),(260, 60, 40, 20),(320, 160, 40, 20),(80, 380, 40, 20),
    (140, 520, 40, 20),(240, 560, 20, 20),(480, 20, 20, 20),(300, 540, 20, 40),(300, 320, 20, 180),(540, 320, 20, 120),
    (540, 480, 20, 40),(540, 560, 20, 20),(660, 440, 20, 140),(660, 320, 20, 60),(480, 320, 20, 100),(480, 460, 20, 60),
    (360, 320, 20, 80),(360, 460, 20, 80),(300, 160, 20, 120),(300, 60, 20, 60),(440, 120, 40, 20),(480, 80, 20, 60),
    (480, 180, 20, 100),(500, 180, 40, 20),(540, 60, 20, 140),(540, 260, 60, 20),(260, 320, 40, 20),(240, 320, 20, 40),
    (240, 400, 20, 120),(720, 60, 20, 80),(720, 200, 20, 80),(660, 60, 20, 80),(660, 200, 20, 80),(680, 120, 40, 20),
    (660, 180, 80, 20),(180, 180, 20, 100),(440, 400, 40, 20),(140, 180, 40, 20),(180, 20, 20, 20),(180, 80, 20, 60),
    },
    222:{
    
    },
    223:{
        (0, 0, 380, 20),(420, 0, 380, 20),(780, 0, 20, 280),(780, 320, 20, 280),(0, 580, 380, 20),(420, 580, 380, 20),
        (0, 0, 20, 280),(0, 320, 20, 280),(380, 0, 40, 20),(780, 280, 20, 40),(380, 580, 40, 20),(0, 280, 20, 40),
        (60, 60, 20, 220),(180, 60, 20, 220),(60, 520, 180, 20),(60, 360, 180, 0),(60, 340, 180, 20),(300, 60, 20, 220),
        (360, 60, 20, 220),(420, 80, 140, 0),(420, 60, 140, 20),(600, 60, 140, 20),(420, 120, 80, 20),(560, 120, 120, 20),
        (720, 120, 60, 20),(420, 200, 180, 0),(420, 200, 180, 0),(420, 200, 160, 0),(420, 180, 200, 20),(660, 180, 120, 20),
        (420, 240, 160, 20),(620, 240, 120, 20),(280, 340, 120, 20),(280, 400, 120, 20),(180, 460, 140, 20),(360, 460, 40, 20),
        (280, 520, 80, 20),(20, 460, 120, 20),(120, 400, 120, 20),(20, 400, 40, 20),(320, 160, 40, 20),(260, 60, 40, 20),
        (200, 260, 40, 20),(240, 160, 20, 120),(240, 60, 20, 40),(120, 120, 0, 0),(120, 60, 20, 100),(120, 200, 20, 80),
        (440, 300, 20, 60),(440, 400, 20, 100),(440, 540, 20, 40),(500, 300, 20, 140),(500, 520, 20, 60),(560, 300, 20, 60),
        (560, 420, 20, 160),(580, 480, 40, 20),(620, 300, 20, 60),(620, 400, 20, 140),(700, 320, 20, 40),(640, 300, 80, 20),
        (700, 400, 20, 80),(640, 460, 60, 20),(680, 520, 20, 60),(140, 140, 40, 20),(120, 320, 20, 40),
    },
    32:  {
(0, 0, 380, 10),(410, 0, 380, 10),(780, 0, 10, 280),(780, 310, 10, 280),(0, 580, 380, 10),(410, 580, 380, 10),
(0, 0, 10, 280),(0, 310, 10, 280),(40, 340, 40, 0),(40, 340, 0, 0),(40, 340, 60, 0),
(10, 310, 0, 0),(10, 310, 0, 0),(0, 310, 100, 10),(80, 210, 0, 80),
(60, 210, 10, 60),(10, 180, 60, 10),(100, 140, 10, 100),(100, 60, 10, 80),(80, 260, 100, 10),(160, 180, 10, 80),
(140, 280, 10, 100),(40, 380, 60, 10),(110, 410, 80, 10),(40, 510, 110, 10),
(80, 400, 10, 40),(80, 410, 40, 10),(10, 440, 10, 10),(80, 460, 10, 60),(160, 510, 100, 10),(260, 510, 0, 40),
(260, 510, 10, 60),(260, 440, 10, 80),(210, 380, 100, 10),(260, 410, 110, 10),(300, 310, 10, 60),
(140, 440, 10, 40),(180, 460, 0, 60),(180, 460, 10, 60),(100, 410, 10, 10),(210, 440, 10, 10),(210, 410, 10, 10),
(100, 380, 10, 10),(180, 400, 10, 0),(180, 400, 10, 10),(180, 180, 140, 10),(300, 100, 10, 110),(100, 240, 10, 140),
(240, 100, 10, 60),(210, 280, 40, 0),(260, 280, 10, 60),(240, 310, 10, 10),(260, 340, 10, 10),
(40, 110, 60, 10),(10, 60, 60, 10),(100, 10, 10, 10),(600, 10, 10, 100),(400, 60, 160, 10),(400, 110, 210, 10),
(380, 80, 10, 40),(310, 60, 10, 140),(360, 340, 10, 80),(380, 340, 180, 10),(680, 260, 100, 10),(680, 280, 10, 100),
(560, 380, 80, 0),(560, 380, 140, 10),(260, 240, 0, 40),(260, 240, 10, 40),(340, 160, 180, 10),(510, 140, 10, 40),
(540, 210, 10, 110),(660, 280, 40, 40),(700, 310, 0, 0),(160, 80, 10, 10),(110, 140, 60, 0),(110, 140, 140, 10),
(240, 110, 80, 10),(180, 10, 10, 100),(110, 60, 10, 10),(210, 40, 110, 10),(360, 240, 10, 100),(410, 180, 10, 140),
(480, 180, 10, 140),(580, 180, 140, 40),(580, 210, 10, 110),(600, 280, 40, 10),(710, 180, 40, 0),(710, 180, 10, 10),
(710, 110, 10, 60),(710, 60, 60, 10),(660, 60, 10, 110),(740, 310, 40, 10),(700, 380, 40, 10),
(710, 400, 10, 40),(710, 560, 10, 10),(660, 410, 60, 10),(660, 480, 60, 0),(600, 480, 140, 40),(660, 510, 10, 10),
(610, 560, 10, 10),(560, 510, 10, 10),(510, 560, 10, 10),(480, 540, 10, 10),(480, 510, 100, 10),(510, 480, 80, 10),
(500, 480, 10, 40),(600, 440, 10, 40),(540, 400, 10, 40),(310, 510, 110, 10),(410, 460, 100, 10),(410, 360, 10, 100),
(310, 480, 10, 40),(380, 460, 10, 10),(480, 400, 60, 10),
    },
    34:{
    (200, 140, 40, 200), (400, 140, 20, 200), (480, 140, 20, 200), (660, 300, 20, 60),
    (580, 140, 20, 120), (660, 100, 60, 140), (220, 400, 380, 60), (220, 500, 480, 20),
    (220, 540, 480, 20),(260, 200, 100, 20),(280, 240, 100, 20),(240, 280, 100, 20),
    (280, 320, 120, 20),(300, 360, 300, 20),(300, 80, 300, 20),(20, 140, 100, 20),
    (80, 200, 100, 20),(20, 260, 100, 20),(80, 320, 80, 20),(20, 360, 100, 20),
    (80, 400, 100, 20),(40, 440, 20, 100),(120, 440, 20, 80),(160, 520, 20, 60),
    (640, 400, 120, 40),(560, 40, 180, 20),(80, 40, 200, 20),
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
        (60, 60, 80, 20),         # Top horizontal
        (260, 120, 40, 20),        # 5th horizontal
        (60, 240, 200, 20),        # 3rd horizontal
        (200, 240, 300, 20),        # 4th horizontal
        (400, 300, 300, 20),        # 5th horizontal
        (200, 360, 400, 20),        # 6th horizontal
        (100, 420, 100, 20),        # 7th horizontal
        (0, 480, 300, 20),        # 8th horizontal
        (0, 540, 500, 20),        # Bottom horizontal

        # Vertical walls
        (60, 40, 20, 200),         # 1st vertical
        (120, 0, 20, 150),        # 2nd vertical
        (180, 80, 20, 200),        # 3rd vertical
        (240, 00, 20, 200),        # 4th vertical
        (300, 40, 20, 120),        # 5th vertical
        (360, 80, 20, 200),        # 6th vertical
        (420, 0, 20, 200),        # Center vertical
        (480, 80, 20, 200),        # 8th vertical
        (540, 40, 20, 200),        # 9th vertical
        (600, 20, 20, 200),        # 10th vertical
        (660, 40, 20, 200),        # 11th vertical
        (720, 80, 20, 200),        # 12th vertical
        (780, 20, 20, 200),        # Right vertical
    },
    141:{
        (0, 0, 800, 10), (0, 590, 800, 10), (0, 0, 10, 600), (790, 0, 10, 600), (43, 39, 219, 10), (292, 39, 219, 10), 
        (541, 39, 206, 10), (86, 78, 89, 10), (212, 78, 481, 10),  (710, 78, 40, 10), (129, 117, 23, 10), (190, 117, 148, 10), 
        (373, 117, 288, 10), (172, 156, 144, 10), (353, 156, 51, 10), (440, 156, 178, 10), (215, 195, 318, 10), (565, 195, 10, 10), 
        (258, 234, 249, 10), (301, 273, 163, 10),   (498, 273, 40, 10), (43, 548, 219, 10), (292, 548, 219, 10), 
        (541, 548, 206, 10), (86, 512, 183, 10), (307, 512, 150, 10), (495, 512, 209, 10), (129, 473, 153, 10), (319, 473, 316, 10), 
        (668, 473, 40, 10), (172, 434, 86, 10), (295, 434, 295, 10), (215, 395, 297, 10), (544, 395, 31, 10), 
        (258, 356, 156, 10), (444, 356, 88, 10), (301, 317, 128, 10), (464, 317, 25, 10), (43, 39, 10, 512), (747, 39, 10, 522), 
        (86, 78, 10, 434), (704, 78, 10, 444), (129, 117, 10, 356), (661, 117, 10, 366), (172, 156, 10, 278), (618, 156, 10, 288), 
        (215, 195, 10, 200), (575, 195, 10, 210), (258, 234, 10, 122), (532, 234, 10, 132), (301, 273, 10, 44), (489, 273, 10, 54),
        (200, 551, 10, 40), (720, 10, 10, 35), (120, 512, 10, 40), (86, 300, 40, 10),
    },
    1414:{
        (0, 0, 800, 20), (0, 580, 800, 20), (0, 0, 20, 600), (780, 0, 20, 600),# Outer walls
    },
    55:{
        # Outer walls
        (0, 0, 800, 20),           # Top wall
        (0, 580, 800, 20),         # Bottom wall
        (0, 0, 20, 600),           # Left wall
        (780, 0, 20, 600),         # Right wall

        # Horizontal walls
        (70, 80, 660, 20),         # Top horizontal
        (150, 160, 180, 20),        # 2nd horizontal
        (460, 160, 180, 20),
        (230, 240, 120, 20),        # 3rd horizontal
        (450, 240, 100, 20),
        #(310, 320, 180, 20),        # 4th horizontal
        (230, 340, 340, 20),        # 5th horizontal
        (150, 420, 180, 20),        # 5th horizontal
        (460, 420, 180, 20),
        (70, 500, 660, 20),        # Bottom horizontal

        # Vertical walls
        (70, 80, 20, 190),         # Left vertical
        (70, 330, 20, 190),
        (150, 160, 20, 120),        # 2nd vertical
        (150, 320, 20, 120),
        (230, 240, 20, 120),        # 3rd vertical
        #(310, 80, 20, 440),        # 4th vertical
        #(390, 80, 20, 460),        # Center vertical
        #(470, 80, 20, 440),        # 6th vertical
        (550, 240, 20, 120),        # 7th vertical
        (630, 160, 20, 120),        # 8th vertical
        (630, 320, 20, 120),
        (710, 80, 20, 180),        # Right vertical
        (710, 340, 20, 180), 
    },
    56:{
        (0, 0, 800, 20), (0, 590, 800, 20), (0, 0, 20, 600), (790, 0, 20, 600), (60, 60, 680, 20), 
        (120, 120, 560, 20), (180, 180, 440, 20), (240, 240, 320, 20), (300, 320, 200, 20), (240, 360, 320, 20), 
        (180, 420, 440, 20), (120, 480, 560, 20), (60, 540, 680, 20), (60, 60, 20, 500), (120, 120, 20, 380), 
        (180, 180, 20, 260), (240, 240, 20, 140), (300, 300, 20, 20), #(360, 360, 20, -100), (420, 360, 20, -100), 
        (480, 300, 20, 20), (540, 240, 20, 140), (600, 180, 20, 260), (660, 120, 20, 380), (720, 60, 20, 500)

    },
    57:{
        #Kinda messed up version
        #(0, 0, 800, 10), (0, 590, 800, 10), (0, 0, 10, 600), (790, 0, 10, 600), (47, 42, 706, 10), (47, 558, 706, 10), 
        #(94, 84, 612, 10), (94, 516, 612, 10), (141, 126, 518, 10), (141, 474, 518, 10), (188, 168, 424, 10), 
        # (188, 432, 424, 10), (235, 210, 330, 10), (235, 390, 330, 10), (282, 252, 236, 10), (282, 348, 236, 10), 
        # (329, 294, 142, 10), (329, 306, 142, 10), (376, 336, 48, 10), (376, 264, 48, 10), (47, 42, 10, 516), 
        # (753, 42, 10, 526), (94, 84, 10, 432), (706, 84, 10, 442), (141, 126, 10, 348), (659, 126, 10, 358), (188, 168, 10, 264), 
        # (612, 168, 10, 274), (235, 210, 10, 180), (565, 210, 10, 190), (282, 252, 10, 96), (518, 252, 10, 106), (329, 294, 10, 12), (471, 294, 10, 22)
        
        #Super tight perfect boxes
        # (0, 0, 800, 10), (0, 590, 800, 10), (0, 0, 10, 600), (790, 0, 10, 600), (44, 40, 712, 10), (44, 560, 712, 10), 
        # (88, 80, 624, 10), (88, 520, 624, 10), (132, 120, 536, 10), (132, 480, 536, 10), (176, 160, 448, 10), 
        # (176, 440, 448, 10), (220, 200, 360, 10), (220, 400, 360, 10), (264, 240, 272, 10), (264, 360, 272, 10), 
        # (308, 280, 184, 10), (308, 320, 184, 10), (352, 320, 96, 10), (352, 280, 96, 10), (396, 360, 8, 10), 
        # (396, 240, 8, 10), (44, 40, 10, 520), (756, 40, 10, 530), (88, 80, 10, 440), (712, 80, 10, 450), 
        # (132, 120, 10, 360), (668, 120, 10, 370), (176, 160, 10, 280), (624, 160, 10, 290), (220, 200, 10, 200), 
        # (580, 200, 10, 210), (264, 240, 10, 120), (536, 240, 10, 130), (308, 280, 10, 40), (492, 280, 10, 50)

        #Puttin holes in the wall
        (0, 0, 800, 10), (0, 590, 800, 10), (0, 0, 10, 600), (790, 0, 10, 600), (43, 39, 219, 10), (292, 39, 219, 10), (541, 39, 206, 10), (86, 78, 89, 10), (212, 78, 481, 10), (732, 78, -28, 10), (129, 117, 23, 10), (190, 117, 148, 10), (373, 117, 288, 10), (172, 156, 144, 10), (353, 156, 51, 10), (440, 156, 178, 10), (215, 195, 318, 10), (565, 195, 10, 10), (258, 234, 249, 10), (547, 234, -15, 10), (301, 273, 163, 10), (503, 273, -14, 10), (43, 551, 219, 10), (292, 551, 219, 10), (541, 551, 206, 10), (86, 512, 183, 10), (307, 512, 150, 10), (495, 512, 209, 10), (129, 473, 153, 10), (319, 473, 316, 10), (668, 473, -7, 10), (172, 434, 86, 10), (295, 434, 295, 10), (621, 434, -3, 10), (215, 395, 297, 10), (544, 395, 31, 10), (258, 356, 156, 10), (444, 356, 88, 10), (301, 317, 128, 10), (464, 317, 25, 10), (43, 39, 10, 512), (747, 39, 10, 522), (86, 78, 10, 434), (704, 78, 10, 444), (129, 117, 10, 356), (661, 117, 10, 366), (172, 156, 10, 278), (618, 156, 10, 288), (215, 195, 10, 200), (575, 195, 10, 210), (258, 234, 10, 122), (532, 234, 10, 132), (301, 273, 10, 44), (489, 273, 10, 54)

        }
}