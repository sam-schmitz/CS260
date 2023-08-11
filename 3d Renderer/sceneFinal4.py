from ren3d.scenedef import *
from math import sin, cos, pi

#g = Transformable(Box(color=Material((.3, .2, .4)))).scale(150, 2, 150)
#scene.add(g)
scene.textures = True


#desk
tp = Transformable(Mesh("desk.off", color = make_material((75/255, 43/255, 32/255)),
                        smooth=False, recenter=True))
tp.scale(69, 69, 69).translate(0, 0, 0)
scene.add(tp)


#mug
tp = Transformable(Mesh("m504.off", SILVER,
                        smooth=True, recenter=True))
tp.scale(6.5, 6.5, 6.5).translate(-16, 3, 10)
scene.add(tp)


#computer
group = Group()
t = Transformable(Mesh("m548.off", SILVER,
                        smooth=False, recenter=True))
t.scale(20, 20, 20)
group.add(t)

group.add(Transformable(Box(pos=(0, 4, 8), size=(11, 7, .5),
              color=BLACK_PLASTIC,
              texture=Boxtexture("textures/loading.ppm"))))

group.add(Transformable(Box(pos=(0, 2, 8), size=(11, 11, .5),
              color=BLACK_PLASTIC)))
            
group.add(Transformable(Box(pos=(0, 2.25, 8.1), size=(8, .25, .5),
              color=GREY_PLASTIC)))
group.add(Transformable(Box(pos=(0, -.25, 8.1), size=(8, .25, .5),
              color=GREY_PLASTIC)))
group.add(Transformable(Box(pos=(4, 1, 8.1), size=(.25, 2.5, .5),
              color=GREY_PLASTIC)))
group.add(Transformable(Box(pos=(-4, 1, 8.1), size=(.25, 2.5, .5),
              color=GREY_PLASTIC)))

group.add(Transformable(Box(pos=(-3, 1, 8.1), size=(1.5, 1.75, .5),
              color=GREY_PLASTIC)))

for obj in group.objects:
    obj.scale(.85, .85, .85).translate(-2, 8, 6.5)


scene.add(group)


#cradle
silver = Material(diffuse=(.2, .2, .2), specular=(.6, .6, .6),
                  shininess=100, reflect=(.4, .4, .4))
group = Group()

group.add(Transformable(Sphere(pos=(0, 0, 0), radius=1, color=silver)))
group.add(Transformable(Sphere(pos=(2, 0, 0), radius=1, color=silver)))
group.add(Transformable(Sphere(pos=(-2, 0, 0), radius=1, color=silver)))
group.add(Transformable(Sphere(pos=(-4, 0, 0), radius=1, color=silver)))
group.add(Transformable(Sphere(pos=(4+cos(pi/12)+cos(pi/6)+cos(pi/4), sin(pi/12)+sin(pi/6) +sin(pi/4), 0), radius=1, color=silver)))

g = Transformable(Box(color=Material((.82, .41, .12))))
g.scale(.1, 5, .1).translate(0, 2.5, 0)
group.add(g)
g = Transformable(Box(color=Material((.82, .41, .12))))
g.scale(.1, 5, .1).translate(-2, 2.5, 0)
group.add(g)
g = Transformable(Box(color=Material((.82, .41, .12))))
g.scale(.1, 5, .1).translate(2, 2.5, 0)
group.add(g)
g = Transformable(Box(color=Material((.82, .41, .12))))
g.scale(.1, 5, .1).rotate_z(45).translate(4+2*sin(pi/4), 2.5+(2.5-2.5*cos(pi/4)), 0)
group.add(g)
g = Transformable(Box(color=Material((.82, .41, .12))))
g.scale(.1, 5, .1).translate(-4, 2.5, 0)
group.add(g)

g = Transformable(Box(color=GOLD))
g.scale(12, .25, .25).translate(0, 5, 0)
group.add(g)
g = Transformable(Box(color=GOLD))
g.scale(.25, 10, .25).rotate_x(-36.87).translate(5.75, 1, 3)
group.add(g)
g = Transformable(Box(color=GOLD))
g.scale(.25, 10, .25).rotate_x(36.87).translate(5.75, 1, -3)
group.add(g)
g = Transformable(Box(color=GOLD))
g.scale(.25, 10, .25).rotate_x(-36.87).translate(-5.75, 1, 3)
group.add(g)
g = Transformable(Box(color=GOLD))
g.scale(.25, 10, .25).rotate_x(36.87).translate(-5.75, 1, -3)
group.add(g)
for obj in group.objects:
    obj.rotate_y(10).translate(15, 3, 5)
scene.add(group)


#floor
r = Box(pos=(0, 0, 0), size=(50, .1, 50), color = (0, 0, .2), texture=Boxtexture("textures/carpet.ppm"))
rug = Transformable(r)
rug.rotate_y(45).translate(0, -30, 0)
scene.add(rug)

bmat = Material((.4, .4, .4), reflect=(.4, .4, .4))
floor = Transformable((Box(pos=(0, -30.5, 0), size=(200, 1, 120),
              color=bmat, texture=Boxtexture("textures/wood.ppm"))))
floor.rotate_y(25).translate(0, 0, -15)
scene.add(floor)

#globe

globegroup = Group()
s = Sphere(pos=(0, 0, 0), radius=3,
        color=BRASS,
        texture=Spheretexture("textures/globe.ppm"))
globe = Transformable(s)
globe.rotate_y(90)
globegroup.add(globe)

thick = .2
oh = Sphere((0, 0, 0), .5, color=GOLD)
oh1 = Transformable(oh)
oh1.scale(2.10, .5, 2.10).translate(0, -5, 0)#.translate(0, thick/2, 0)
globegroup.add(oh1)

post = Box(pos=(0, 0, 0), size=(1, 1, 1), color = GOLD)
post1 = Transformable(post)
post1.scale(.5, 1.75, .5).translate(0, -3.875, 0)
globegroup.add(post1)

for obj in globegroup.objects:
    obj.scale(2, 2, 2).translate(-8, 32, -5)

scene.add(globegroup)


#modle Car
silver = Material(diffuse=(.2, .2, .2), specular=(.6, .6, .6),
                  shininess=100, reflect=(.4, .4, .4))

tp = Transformable(Mesh("m1549.off", SILVER,
                        smooth=False, recenter=True))
tp.scale(13, 13 ,13).rotate_y(135).translate(12, 23, -4)
scene.add(tp)



#Books
tp = Transformable(Mesh("m1791.off", color=make_material((.25, 0, 0)),
                        smooth=False, recenter=True))
tp.scale(8, 8, 8).rotate_z(90).translate(15, 16, -3)
scene.add(tp)
tp = Transformable(Mesh("m1791.off", color=make_material((0, .25, 0)),
                        smooth=False, recenter=True))
tp.scale(8, 8, 8).rotate_z(90).translate(15, 14.5, -2)
scene.add(tp)
tp = Transformable(Mesh("m1791.off", color=make_material((0, 0, .25)),
                        smooth=False, recenter=True))
tp.scale(6, 6, 6).rotate_z(-20).translate(20, 8, -2)
scene.add(tp)
tp = Transformable(Mesh("m1791.off", color=make_material((.25, .25, .0)),
                        smooth=False, recenter=True))
tp.scale(8, 8, 8).rotate_z(90).translate(10, 7, -2)
scene.add(tp)
tp = Transformable(Mesh("m1791.off", color=make_material((.25, 0, .25)),
                        smooth=False, recenter=True))
tp.scale(6, 6, 6).rotate_z(20).translate(3, 16, -3)
scene.add(tp)


camera.set_perspective(40, 4/3, 3)
camera.set_view((60, 65, 125), (0, 0, 0), (0, 1, 0))

scene.set_light((60, 100, 100), (1, 1, 1))
scene.ambient = (.5, .5, .5)
scene.background = (0, 0, 0)
scene.shadows = True