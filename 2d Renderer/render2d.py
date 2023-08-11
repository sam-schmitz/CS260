# render2d.py
#  Class for 2D rendering with transformations

from math import sin, cos, pi

from image import Image
from painter import Painter
import trans2d
import matrix as mat


class Render2d(object):

    def __init__(self, size, background=(255, 255, 255)):
        self.image = Image(size)
        self.image.clear(background)
        self.painter = Painter(self.image)
        self.trans = mat.unit(3)            # current transformation
        self.trans_stack = []
        self.background = background
        self.color = (0, 0, 0)
        w, h = size
        self.loadview((0, 0, w-1, h-1))      # natural coordinates for image

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, rgb):
        self._color = rgb
        self.painter.color = rgb

    @property
    def viewport(self):
        return self.painter.viewport

    @property
    def window(self):
        return self._window

    def _trans_pt(self, pt):
        """ return transformed point """
        x, y, _ = mat.apply(self.trans, pt+(1,))
        return (x, y)

    def _trans_pts(self, points):
        """ return list of transformed points """
        tran = []
        for i in points:
            tran.append(self._trans_pt(i))
        return tran

    def loadview(self, window, viewport=None):
        """ set transform to a window-viewport transformation """
        #takes two boxes (the image in the world and the viewport)
        #if no viewport use the entire image
        if viewport is None:
            w, h = self.image.size
            viewport = (0, 0, w-1, h-1)
        self.painter.viewport = viewport
        vl, vb, vr, vt = viewport
        self.trans = trans2d.window(window, (vl-.5, vb-.5, vr+.5, vt+.5))
        self._window = window


    def push_matrix(self):
        """ push current transformation matrix onto the stack """
        self.trans_stack.append(self.trans)

    def pop_matrix(self):
        """ remove top matrix from stack and make it the current tranformation """
        self.trans = self.trans_stack.pop()

    def scale(self, sx, sy):
        """ update current transform with a scaling """
        self.trans = mat.mul(self.trans, trans2d.scale(sx, sy))

    def rotate(self, angle):
        """ update current transform with a rotation """
        self.trans = mat.mul(self.trans, trans2d.rotate(angle))

    def translate(self, dx, dy):
        """ update current transform with a translation """
        self.trans = mat.mul(self.trans, trans2d.translate(dx, dy))

    def point(self, pt):
        """ draw point pt """
        self.painter.draw_point(self._trans_pt(pt))

    def line(self, a, b):
        """ line from point a to point b"""
        self.painter.draw_line(self._trans_pt(a), self._trans_pt(b))

    def lines(self, points):
        """ draw polyline connecting points"""
        self.painter.draw_lines(self._trans_pts(points))

    def polygon(self, points):
        """ draw the polygon having points as vertices"""
        self.painter.draw_polygon(self._trans_pts(points))

    def filled_triangle(self, a, b, c):
        """ draw filled triangle a, b, c """
        self.painter.draw_filled_triangle(self._trans_pt(a), self._trans_pt(b), self._trans_pt(c))

    def filled_polygon(self, points):
        """ draw filled polygon having points as vertices """
        self.painter.draw_filled_polygon(self._trans_pts(points))

    def circle(self, center, radius, segments=50):
        """ draw circle with given center and radius """
        self.painter.draw_polygon(self._trans_pts(self._circle_points(center, radius, segements)))

    def _circle_points(self, center, radius, npoints):
        cx, cy = center
        dtheta = 2 * pi / npoints
        theta = 0.0
        points = []
        for _ in range(npoints):
            x = cx + radius*cos(theta)
            y = cy + radius*sin(theta)
            points.append((x, y))
            theta += dtheta
        return points

    def filled_circle(self, center, radius, segments=50):
        """draw filled circle with given center and radius

        note: This will have to use the patinter's
        draw_filled_polygon, as a transformed circle may no longer be
        circular.

        """
        self.painter.draw_filled_polygon(self._trans_pts(self._circle_points(center, radius, segments)))

if __name__ == "__main__":
    r = Render2d((400, 300))
    r.loadview((0, 0, 3, 3))
    r.line((1, 0), (1, 3))
    r.line((2, 0), (2, 3))
    r.line((0, 1), (3, 1))
    r.line((0, 2), (3, 2))
    r.filled_polygon([(1, 1), (1, 2), (2, 2), (2, 1)])
    r.color = (255, 0, 0)
    r.filled_circle((1.5, 1.5), .5, 50)
    r.image.show()
    r.image.save("window_test.ppm")
