#sceneGlobe.py

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

rbrass = Material(*BRASS)
rbrass.reflect = (.1, .1, .1)
s = Sphere(pos=(0, 0, 0), radius=3,
        color=rbrass,
        texture=Spheretexture("textures/globe.ppm"))
globe = Transformable(s)
globe.rotate_y(60).translate(0, 0, -25)
scene.add(globe)

#the stand for the globe
thick = .2
oh = Sphere((0, 0, 0), .5, texture=Spheretexture("textures/wood.ppm"))
oh1 = Transformable(oh)
oh1.scale(2.10, .5, 2.10).translate(0, -5, -25)#.translate(0, thick/2, 0)
scene.add(oh1)

post = Box(pos=(0, 0, 0), size=(1, 1, 1), texture=Boxtexture("textures/wood.ppm"))
post1 = Transformable(post)
post1.scale(.5, 1.75, .5).translate(0, -3.875, -25)
scene.add(post1)

#scene.add(Box(pos=(), size(),
            #color=, texture=Boxtexture("textures/wood.ppm")))

#bmat = Material((.4, .4, .4), reflect=(.4, .4, .4))
#scene.add(Box(pos=(0, -3.5, -20), size=(18, 1, 30),
              #color=bmat, texture=Boxtexture("textures/wood.ppm")))
