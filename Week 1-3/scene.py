from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random

def main():
    scene_width = 800
    scene_height = 500
    canvas = start_drawing("Scene", scene_width, scene_height)

    draw_sky(canvas, scene_width, scene_height)
    draw_mountain(canvas, 300, 0, 450)
    draw_trees(canvas,300, 0, 450 )
    draw_hills(canvas, 550, 0, 50)
    draw_clouds(canvas)
    draw_flowers(canvas)
    draw_snow(canvas, 300, 0, 450)
    #draw_grid(canvas, scene_width, scene_height, 50)

    finish_drawing(canvas)

# Define Functions

def draw_sky(canvas, scene_width, scene_height):
    #Draw the Sky
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height, width=0, fill="lightCyan1")

def draw_hills(canvas, center_x, bottom, height):

    draw_polygon(canvas, 
        0,0,
        550, 200,
        550,0,
        outline="", width=1, fill="green")

    draw_polygon(canvas, 
        550, 0,
        550, 200,
        800, 180,
        800, 0,
        outline="", width=1, fill="green")

    draw_polygon(canvas, 
        0,0,
        0, 100,
        400, 145,
        outline="", width=1, fill="dark green")

def draw_mountain(canvas, center_x, bottom, height):

    draw_polygon(canvas, 
        250, 125,
        550, 140,
        300, 400,
        160, 230,
        outline="", width=1, fill="grey")

    draw_polygon(canvas, 
        0, 100,
        100, 300,
        250, 125,
        outline="", width=1, fill="dark grey")

def draw_trees(canvas, center_x, bottom, height):
    x = 50
    for i in range(8):
        y= random.randint(-10,30)
        draw_polygon(canvas, 
            x + 20, 75,
            x + 40, 200+ y,
            x + 60, 75,
            outline="", width=1, fill="green")
        x += 50

def draw_clouds(canvas):
    for i in range(4):
        x1 = random.randint(400, 550)
        y1 = random.randint(300, 400)
        x2 = random.randint(650, 800)
        y2 = random.randint(400, 500)
        draw_oval(canvas, x1, y1, x2, y2, outline="floralWhite", fill="floralWhite")

def draw_flowers(canvas):
    min_diam = 2
    max_diam = 8
    for i in range(90):
        x = random.randint(0, 800)
        y = random.randint(0, 100)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                fill="mediumOrchid1")
                
    for i in range(60):
        x = random.randint(0, 800)
        y = random.randint(0, 100)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                fill="orange")

    for i in range(60):
        x = random.randint(0, 800)
        y = random.randint(0, 100)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                fill="yellow")

    for i in range(30):
        x = random.randint(300, 800)
        y = random.randint(100, 130)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter, fill="yellow")

    for i in range(20):
        x = random.randint(250, 800)
        y = random.randint(100, 130)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter, fill="mediumOrchid1")

    for i in range(20):
        x = random.randint(300, 800)
        y = random.randint(100, 130)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter, fill="orange")

    for i in range(15):
        x = random.randint(450, 800)
        y = random.randint(150, 175)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter, fill="yellow")

    for i in range(10):
        x = random.randint(450, 800)
        y = random.randint(150, 175)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter, fill="mediumOrchid1")

    for i in range(10):
        x = random.randint(450, 800)
        y = random.randint(150, 175)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter, fill="orange")

def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)

def draw_snow(canvas, center_x, bottom, height):

    draw_polygon(canvas, 
        216, 300,
        300, 400,
        396, 300,
        outline="", width=1, fill="floralWhite")

    draw_polygon(canvas, 
        60, 220,
        100, 300,
        170, 220,
        outline="", width=1, fill="floralWhite")

main()