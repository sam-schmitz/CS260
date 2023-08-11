#scenecylinder
#By: Sam Schmitz

from ren3d.scenedef import *

camera.set_perspective(30, 1.3333, 5)
camera.set_view((4, 3, 5), (0, 0, -20))

scene.background = (0, 0, 0)
scene.ambient = (.3, .3, .3)
scene.set_light(pos=(-150, 200, 50), color=(.8, .8, .8))
scene.add_light(pos=(150, 50, 50), color=(.5, .5, .5))

scene.shadows = True
scene.reflections = 5
scene.textures = True

scene.add(Cylinder(pos=(0, 0, -25), height=2, radius=1, color=(0, 0, 1)))
