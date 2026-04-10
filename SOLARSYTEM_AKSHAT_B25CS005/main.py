from vpython import *
import math

#use mouse for better experience
#to zoom use scroll or 2 fingers on cursor pad
#to move in 3-d hold right side of cursor and move
#space key to pause
#click on planet to zoom into it and info about it top left corner

#scene setup
scene.title = "Solar System Simulisation"
scene.width = 1275
scene.height = 625
scene.background = color.black
scene.forward = vector(-1, 1, -0.5) 
scene.up = vector(0, 0, 1)  

#sun
sun = sphere(radius=1000, pos=vector(0,0,0),up=vector(0,0,1), texture="images/sun.jpg", emissive=True)

#planets
mercury = sphere(radius=10, pos=vector(1183,0,0),up=vector(0,0,1), texture="images/mercury.jpg")
venus   = sphere(radius=23, pos=vector(1255,0,0), up=vector(0,0,1), texture="images/venus.jpg")
earth   = sphere(radius=25, pos=vector(1315,0,0),up=vector(0,0,1), texture="images/earth.jpg")
mars    = sphere(radius=15, pos=vector(1397,0,0),up=vector(0,0,1), texture="images/mars.jpg")
jupiter = sphere(radius=100.3, pos=vector(1619,0,0), up=vector(0,0,1), texture="images/jupiter.jpg")
saturn  = sphere(radius=83.6, pos=vector(1910,0,0),up=vector(0,0,1), texture="images/saturn.jpg")
saturn_ring = ring(pos=vec(1910, 0, 0), axis=vec(0, 0, 1), radius=100, thickness=5, texture="images/saturn_ring.jpg")
uranus  = sphere(radius=36.4, pos=vector(2125,0,0),up=vector(0,0,1), texture="images/uranus.jpg")
neptune = sphere(radius=35.3, pos=vector(2260,0,0),up=vector(0,0,1), texture="images/neptune.jpg")

#text on screen
instruction= text(text="SPACE KEY TO PAUSE AND RESUME",pos=vector(800,700,300),up=vector(1,1,1), axis=vector(1,1,0), height=50,depth=5,color=color.white)
instructions=text(text="CLICK TO ZOOM AND INFO",pos=vector(1000,500,300),up=vector(1,1,1), axis=vector(1,1,0), height=50,depth=5,color=color.white)
info= text(text="INFO OF TOP-LEFT",pos=vector(800,1100,300),up=vector(1,1,1), axis=vector(1,1,0), height=50, depth=5, color=color.white)
#lists containing planets
inner_planets=[mercury,venus,earth,mars]
outer_planets=[jupiter,saturn,uranus,neptune]
planets=[mercury,venus,earth,mars,jupiter,saturn,uranus,neptune]

# Distances of planets from sun
d_mercury = 1183
d_venus   = 1255
d_earth   = 1315
d_mars    = 1397
d_jupiter = 1619
d_saturn  = 1910
d_uranus  = 2125
d_neptune = 2260

#initial angles from x axis
a_mercury = a_venus = a_earth = a_mars = a_jupiter = a_saturn = a_uranus = a_neptune =0

#pause on space key press
paused = False
def pause(evt):
    global paused
    if evt.key == ' ':  # spacebar
        paused = not paused
        if paused:
            scene.title = "PAUSED"
        else:
            scene.title = "RUNNING"
#bind space key to pause
scene.bind("keydown", pause)

#zoom on click
def zoom(evt):
    global paused
    for o in planets:
#inner planets require more zoom due to small size
        if o in inner_planets:
            if scene.mouse.pick is o:
                paused = True
                for i in range(20):
                    rate(60)
                    scene.camera.pos = scene.camera.pos - (scene.camera.pos - o.pos) * 0.1
#text on title informing the planet 
                if o==mercury:
                    scene.title = "Mercury is smallest planet and closest to sun "
                elif o==venus:
                    scene.title = "Venus is hottest planet with posionous atmosphere"
                elif o==earth:
                    scene.title = "Earth is only planet which has life on it"
                elif o==mars:
                    scene.title = "Mars is also known as Red planet"
                return
#outer planets require less due to bigger size
        if o in outer_planets:
            if scene.mouse.pick is o:
                paused=True
                for i in range(5):
                    rate(60)
                    scene.camera.pos = scene.camera.pos - (scene.camera.pos - o.pos) * 0.1
#text on title informing the planet 
                if o==jupiter:
                    scene.title = "Jupiter is the biggest planet made of gas "
                elif o==saturn:
                    scene.title = "Saturn has large rings and most beautiful planet"
                elif o==uranus:
                    scene.title = "uranus is icy giant with retrogade rotation"
                elif o==neptune:
                    scene.title = "neptune is farthest planet from sun"
                return
            
# Bind the mouse click to zoom
scene.bind('click', zoom)

while True:
    rate(60)
    if paused:
        continue

    # Update angles
    a_mercury += 0.083
    a_venus   += 0.032
    a_earth   += 0.02
    a_mars    += 0.0106
    a_jupiter += 0.0017
    a_saturn  += 0.00068
    a_uranus  += 0.00024
    a_neptune += 0.00012

    # Update positions
    mercury.pos = vector(d_mercury*math.cos(a_mercury), d_mercury*math.sin(a_mercury), 0)
    venus.pos   = vector(d_venus*math.cos(a_venus),     d_venus*math.sin(a_venus),     0)
    earth.pos   = vector(d_earth*math.cos(a_earth),     d_earth*math.sin(a_earth),     0)
    mars.pos    = vector(d_mars*math.cos(a_mars),       d_mars*math.sin(a_mars),       0)
    jupiter.pos = vector(d_jupiter*math.cos(a_jupiter), d_jupiter*math.sin(a_jupiter), 0)
    saturn.pos  = vector(d_saturn*math.cos(a_saturn),   d_saturn*math.sin(a_saturn),   0)
    uranus.pos  = vector(d_uranus*math.cos(a_uranus),   d_uranus*math.sin(a_uranus),   0)
    neptune.pos = vector(d_neptune*math.cos(a_neptune), d_neptune*math.sin(a_neptune), 0)

# Move Saturn ring with Saturn
    saturn_ring.pos=saturn.pos  