import turtle
import math
import random
import time
from PIL import Image, ImageTk

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
screen.title("Spinning Heart for Usha with Animated Cat")
screen.tracer(0)

frames = []
try:
    gif_image = Image.open("cat.gif")
    frame_idx = 0
    TARGET_SIZE = (180, 180) 
    
    while True:
        gif_image.seek(frame_idx)
        frame_rgba = gif_image.convert("RGBA")
        frame_rgba.thumbnail(TARGET_SIZE, Image.Resampling.LANCZOS)
        tk_frame = ImageTk.PhotoImage(frame_rgba)
        frames.append(tk_frame)
        
        shape_name = f"cat_frame_{frame_idx}"
        screen.register_shape(shape_name, turtle.Shape("image", tk_frame))
        
        frame_idx += 1
except EOFError:
    pass
except Exception:
    pass

bg_t = turtle.Turtle()
bg_t.hideturtle()
bg_t.penup()

img_t = turtle.Turtle()
img_t.penup()
img_t.goto(0, -40) 

if frames:
    img_t.shape("cat_frame_0")

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.color("#ff69b4")

FONT_SIZE = 6
FONT_STYLE = ("Arial", FONT_SIZE, "bold")

particles = []
colors = ["#ff69b4", "#ffe4e1"] 

for _ in range(400): 
    x = random.randint(-1200, 1200)
    y = random.randint(-1000, 1000) 
    speed = random.uniform(1.5, 4.0)
    size = random.randint(4, 10) 
    color = random.choice(colors)
    shape = random.choice(['❤', '♦']) 
    particles.append([x, y, speed, size, color, shape])

def update_background(speed_multiplier=1.0):
    bg_t.clear()
    for p in particles:
        p[1] -= p[2] * speed_multiplier
        
        if p[1] < -1000:
            p[1] = 1000
            p[0] = random.randint(-1200, 1200)
            
        bg_t.goto(p[0], p[1])
        bg_t.color(p[4])
        bg_t.write(p[5], align="center", font=("Arial", p[3], "normal"))

animation_start_time = time.time()

def update_gif():
    if not frames:
        return
    
    elapsed_time = time.time() - animation_start_time
    fps = 15 
    
    idx = int(elapsed_time * fps) % len(frames)
    img_t.shape(f"cat_frame_{idx}")

step_count = 0

for scale in range(16, 22):
    for i in range(180):
        angle = i * (math.pi * 2) / 180
        
        x = 16 * (math.sin(angle) ** 3) * scale
        y = (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * scale
        
        t.goto(x, y)
        t.write("usha", align="center", font=FONT_STYLE)
        
        step_count += 1
        
        if step_count % 4 == 0: 
            update_background(speed_multiplier=1.0)
            update_gif()
            screen.update()

current_rotation = 0
try:
    while True:
        t.clear() 
        current_rotation += 0.15 
        
        for scale in range(16, 22):
            for i in range(180): 
                angle = i * (math.pi * 2) / 180
                
                raw_x = 16 * (math.sin(angle) ** 3) * scale
                y = (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * scale
                
                x = raw_x * math.cos(current_rotation)
                
                t.goto(x, y)
                t.write("usha", align="center", font=FONT_STYLE)
        
        update_background(speed_multiplier=3.5)
        update_gif()
        
        screen.update() 
        
except turtle.Terminator:
    pass
