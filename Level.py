

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
        "shop_1": {"pos": [50, 50], "addpower": "extralife", "color": C.YELLOW, "size": 20},
        "shop_2": {"pos": [50, 80], "addpower": "speedboost1", "color": C.BLUE, "size": 20},
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
    },
    55: {
        "goalN": {"pos": mid_top_goal, "sendtolevel": 1, "sendtopos": bottom_start, "color": C.GREY, "size": default_goal_size},
        "goalE": {"pos": mid_right_goal, "sendtolevel": 2, "sendtopos": left_start, "color": C.GREY, "size": default_goal_size},
        "goalS": {"pos": mid_bottom_goal, "sendtolevel": 3, "sendtopos": top_start, "color": C.GREY, "size": default_goal_size},
        "goalW": {"pos": mid_left_goal, "sendtolevel": 4, "sendtopos": right_start, "color": C.GREY, "size": default_goal_size},
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
    21:{
        # Level 14
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
        (541, 39, 206, 10), (86, 78, 89, 10), (212, 78, 481, 10),               (710, 78, 40, 10), (129, 117, 23, 10), (190, 117, 148, 10), 
        (373, 117, 288, 10), (172, 156, 144, 10), (353, 156, 51, 10), (440, 156, 178, 10), (215, 195, 318, 10), (565, 195, 10, 10), 
        (258, 234, 249, 10), (301, 273, 163, 10),          (498, 273, 40, 10), (43, 548, 219, 10), (292, 548, 219, 10), 
        (541, 548, 206, 10), (86, 512, 183, 10), (307, 512, 150, 10), (495, 512, 209, 10), (129, 473, 153, 10), (319, 473, 316, 10), 
        (668, 473, 40, 10), (172, 434, 86, 10), (295, 434, 295, 10), (215, 395, 297, 10), (544, 395, 31, 10), 
        (258, 356, 156, 10), (444, 356, 88, 10), (301, 317, 128, 10), (464, 317, 25, 10), (43, 39, 10, 512), (747, 39, 10, 522), 
        (86, 78, 10, 434), (704, 78, 10, 444), (129, 117, 10, 356), (661, 117, 10, 366), (172, 156, 10, 278), (618, 156, 10, 288), 
        (215, 195, 10, 200), (575, 195, 10, 210), (258, 234, 10, 122), (532, 234, 10, 132), (301, 273, 10, 44), (489, 273, 10, 54),
        (200, 551, 10, 40), (720, 10, 10, 35)
    },
    1414:{

    },
    55:{
        # Outer walls
        (0, 0, 800, 20),           # Top wall
        (0, 580, 800, 20),         # Bottom wall
        (0, 0, 20, 600),           # Left wall
        (780, 0, 20, 600),         # Right wall

        # Horizontal walls
        (70, 80, 660, 20),         # Top horizontal
        (150, 160, 230, 20),        # 2nd horizontal
        (150, 270, 230, 20),
        (230, 240, 150, 20),        # 3rd horizontal
        (230, 190, 150, 20),
        #(310, 320, 180, 20),        # 4th horizontal
        (230, 340, 340, 20),        # 5th horizontal
        (150, 420, 500, 20),        # 5th horizontal
        (150, 420, 500, 20),
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