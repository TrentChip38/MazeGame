#Creating Maps
# Outer walls
import math
WIDTH, HEIGHT = 800, 600

ver_dec_amount = 60
hor_dec_amount = 60

Width = 20
hor_start = 60
vert_start = 60
vert_length = 500
hori_length = 680
hole_amount = 40
levelwall = [
        (0, 0, 800, 10),           # Top wall
        (0, 590, 800, 10),         # Bottom wall
        (0, 0, 10, 600),           # Left wall
        (790, 0, 10, 600),         # Right wall

        # Horizontal walls
        (hor_start, 60, hori_length, Width),         # Top horizontal
        (hor_start + hor_dec_amount, 120, hori_length - 60*2, Width),           # 2nd horizontal
        (hor_start + hor_dec_amount*2, 180, hori_length - 60*4, Width),        # 3rd horizontal
        (hor_start + hor_dec_amount*3, 240, hori_length - 60*6, Width),        # 4th horizontal
        (hor_start + hor_dec_amount*4, 320, hori_length - 60*8, Width),        # 5th horizontal
        (hor_start + hor_dec_amount*3, 360, hori_length - 60*6, Width),        # 6th horizontal
        (hor_start + hor_dec_amount*2, 420, hori_length - 60*4, Width),        # 7th horizontal
        (hor_start + hor_dec_amount*1, 480, hori_length - 60*2, Width),        # 8th horizontal
        (hor_start, 540, hori_length, Width),        # Bottom horizontal

        # Vertical walls
        (60, vert_start, Width, vert_length),         # 1st vertical
        (120, vert_start + ver_dec_amount, Width, vert_length - ver_dec_amount*2),        # 2nd vertical
        (180, vert_start + ver_dec_amount*2, Width, vert_length - ver_dec_amount*4),        # 3rd vertical
        (240, vert_start + ver_dec_amount*3, Width, vert_length - ver_dec_amount*6),        # 4th vertical
        (300, vert_start + ver_dec_amount*4, Width, vert_length - ver_dec_amount*8),        # 5th vertical
        (360, vert_start + ver_dec_amount*5, Width, vert_length - ver_dec_amount*10),        # 6th vertical
        (420, vert_start + ver_dec_amount*5, Width, vert_length - ver_dec_amount*10),        # Center vertical
        (480, vert_start + ver_dec_amount*4, Width, vert_length - ver_dec_amount*8),        # 8th vertical
        (540, vert_start + ver_dec_amount*3, Width, vert_length - ver_dec_amount*6),        # 9th vertical
        (600, vert_start + ver_dec_amount*2, Width, vert_length - ver_dec_amount*4),        # 10th vertical
        (660, vert_start + ver_dec_amount, Width, vert_length - ver_dec_amount*2),        # 11th vertical
        (720, vert_start, Width, vert_length),        # 12th vertical
        #(780, vert_start, Width, vert_length),        # Right vertical
]
print(levelwall)
print("CustomWalls")
WIDTH, HEIGHT = 800, 600

hor_walls = 17
ver_walls = 14
hor_spaces = hor_walls+1
ver_spaces = ver_walls+1

hor_dec_amount = WIDTH//hor_spaces
ver_dec_amount = HEIGHT//ver_spaces
print(ver_dec_amount)
print(hor_dec_amount)

Width = 10
hor_start = hor_dec_amount
vert_start = ver_dec_amount
vert_length = HEIGHT - 2*ver_dec_amount
hori_length = WIDTH -2*hor_dec_amount
hole_amount = 40
customwalls = [
    (0, 0, 800, 10),           # Top wall
    (0, 590, 800, 10),         # Bottom wall
    (0, 0, 10, 600),           # Left wall
    (790, 0, 10, 600),         # Right wall
]
#Create horizontal walls
for i in list(range(math.ceil(hor_walls/2))):
    new_wall = (hor_start + hor_dec_amount*i, vert_start + ver_dec_amount*i, hori_length - hor_dec_amount*(i*2), Width)
    if not any(val < 0 for val in new_wall):
        customwalls.append(new_wall)
    new_wall = (hor_start + hor_dec_amount*i, (HEIGHT -vert_start - ver_dec_amount*i), hori_length - hor_dec_amount*(i*2), Width)
    if not any(val < 0 for val in new_wall):
        customwalls.append(new_wall)
#Create vertical walls
for i in list(range(math.ceil(ver_walls/2))):
    new_wall = (hor_start + hor_dec_amount*i, vert_start + ver_dec_amount*i, Width, vert_length - ver_dec_amount*(i*2))
    if not any(val < 0 for val in new_wall):
        customwalls.append(new_wall)
        new_wall = ((WIDTH -hor_start - hor_dec_amount*i), vert_start + ver_dec_amount*i, Width, 10 +vert_length - ver_dec_amount*(i*2))
    if not any(val < 0 for val in new_wall):
        customwalls.append(new_wall)

print(customwalls)