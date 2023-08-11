#scenerug.py

from ren3d.scenedef import *

camera.set_perspective(40, 1, 3)
camera.set_view((60, 65, 110), (0, 0, 0), (0, 1, 0))

scene.background = (0, 0, 0)
scene.ambient = (.5, .5, .5)
scene.set_light(pos=(60, 100, 100), color=(1, 1, 1))
#scene.set_light(pos=(-150, 200, 50), color=(.8, .8, .8))
#scene.add_light(pos=(150, 50, 50), color=(.5, .5, .5))

scene.shadows = True
#scene.reflections = 5
scene.textures = True

r = Box(pos=(0, 0, 0), size=(1, 1, 1), texture=Boxtexture("textures/carpet.ppm"))
rug = Transformable(r)
rug.scale(50, .1, 50).translate(0, -3, 0)
scene.add(rug)

bmat = Material((.4, .4, .4), reflect=(.4, .4, .4))
scene.add(Box(pos=(0, -3.5, 0), size=(100, 1, 120),
              color=bmat, texture=Boxtexture("textures/wood.ppm")))

s = Sphere(pos=(0, 0, 0), radius=3,
        color=rbrass,
        texture=Spheretexture("textures/globe.ppm"))
globe = Transformable(s)
globe.rotate_y(360).translate(0, 0, -25)
scene.add(globe)

#scene.add(Box(pos=(0, -3.5, -50), size=(30, 20, 1), color=(.8, .8, .8)))
#scene.add(Box(pos=(-10, -3.5, -20), size=(1, 20, 30), color=(.8, .8, .8)))
