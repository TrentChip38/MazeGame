# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Player starting positions
start_positions = {0:[390, 290], 1:[390, 560], 2:[20, 280]}

# Levels and Walls
import Colors as C
levels_color = {0: C.GREEN, 1:(140, 100, 100), 2:C.GREY, 3: C.GREY, 4: C.GREY, 42: C.GREY, 44: C.GREY, 14: C.GREY}

level_goals = {
    0: {
        "goalN": {"pos": [WIDTH //2, 0], "sendtolevel": 1, "sendtopos": [WIDTH //2 -10, HEIGHT-40], "color": C.GREEN, "size": 20},
        "goalE": {"pos": [WIDTH, HEIGHT//2], "sendtolevel": 2, "sendtopos": [50, 50], "color": C.GREEN, "size": 20},
        "goalS": {"pos": [WIDTH //2, HEIGHT], "sendtolevel": 3, "sendtopos": [50, 50], "color": C.GREEN, "size": 20},
        "goalW": {"pos": [0, HEIGHT//2], "sendtolevel": 4, "sendtopos": [50, 50], "color": C.GREEN, "size": 20},
    },
    1: {
        "goalN": {"pos": [WIDTH //2, 0], "sendtolevel": 11, "sendtopos": [WIDTH //2, HEIGHT], "color": C.GREEN, "size": 20},
        "goalE": {"pos": [WIDTH, HEIGHT//2], "sendtolevel": 12, "sendtopos": [50, 50], "color": C.GREEN, "size": 20},
        "goalS": {"pos": [WIDTH //2, HEIGHT], "sendtolevel": 13, "sendtopos": [50, 50], "color": C.GREEN, "size": 20},
        "goalW": {"pos": [0, HEIGHT//2], "sendtolevel": 14, "sendtopos": [WIDTH - 40, HEIGHT//2 - 10], "color": C.GREEN, "size": 20},
    },
    2: {
        "goalN": {"pos": [WIDTH //2, 0], "sendtolevel": 21, "sendtopos": [WIDTH //2, HEIGHT], "color": C.GREEN, "size": 20},
        "goalE": {"pos": [WIDTH, HEIGHT//2], "sendtolevel": 22, "sendtopos": [50, 50], "color": C.GREEN, "size": 20},
        "goalS": {"pos": [WIDTH //2, HEIGHT], "sendtolevel": 23, "sendtopos": [50, 50], "color": C.GREEN, "size": 20},
        "goalW": {"pos": [0, HEIGHT//2], "sendtolevel": 24, "sendtopos": [50, 50], "color": C.GREEN, "size": 20},
    },
    14: {
        "goalS": {"pos": [WIDTH //2, HEIGHT], "sendtolevel": 1, "sendtopos": [50, 50], "color": C.GREEN, "size": 20},
        "goalW": {"pos": [0, HEIGHT//2], "sendtolevel": 0, "sendtopos": [380, 280], "color": C.GREEN, "size": 20},
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
        (400, 0, 20, 200), (300, 100, 20, 300), (500, 0, 20, 400), (700, 200, 20, 200),
        (400, 500, 200, 20), (200, 300, 20, 200), (0, 100, 200, 20), (600, 100, 20, 200),
        (300, 500, 20, 100), (150, 400, 200, 20), (400, 400, 20, 100), (600, 300, 100, 20),
    },
    4:{
        # Level 4
        (0, 150, 600, 20), (700, 150, 20, 450), (600, 300, 20, 300), (400, 200, 200, 20),
        (300, 400, 200, 20), (100, 300, 200, 20), (0, 500, 300, 20), (0, 400, 20, 100),
        (100, 200, 20, 100), (400, 100, 200, 20), (600, 200, 20, 100),
    },
    12:{
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
    }
}