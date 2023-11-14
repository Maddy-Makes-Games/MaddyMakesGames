from ursina import *
Ursina()
# Set the paste-emit-keystrokes variable to its new default value of '0'
#ursina.config.set('paste-emit-keystrokes', '0')

# Your game logic goes here...
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from ursina.prefabs.first_person_controller import FirstPersonController 
size = 15

trap1 = 'assets/trap1.png'
enemy1 = 'assets/enemy1.png'
player = 'assets/player.png'
back = 'assets/bg.png'
ground = 'assets/ground.png'
wall1 = 'assets/wall1.png'
app = Ursina()
bg = Entity(model='quad', z=2, scale_y=10, scale_x=20, color=color.white,texture="bg.png")
trap1 = Entity(model='quad', scale=(4, 1), y=-2, x=-6, color=color.white, collider='box', texture="enemy1.png")
#ursina.config.set('paste-emit-keystrokes', '0')
player = PlatformerController2d(y=0, x=0, z=.01, color=color.white, texture="player.png")
ground = Entity(model='quad', y=-2, scale_x=10, collider="box", color=color.white, texture="ground.png")
wall = Entity(model='quad', color=color.white, scale=(2, 5), x=5.5, collider='quad', texture= "wall1.png")
duplicate(ground, x=-size)
duplicate(ground, x=-size)
duplicate(ground, x=-size)
duplicate(ground, x=-size)
duplicate(ground, x=-size)
duplicate(bg, x=-size)
duplicate(bg, x=-size)
duplicate(bg, x=-size)
duplicate(bg, x=-size)
duplicate(bg, x=-size)
camera.add_script(SmoothFollow(target=player, offset=[0, 1, -30], speed=4))
EditorCamera()
app.run()
