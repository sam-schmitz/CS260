# trans2d.py
#By Sam Schmitz and Tryton Harper
#    implementation of 2d transformations in homogeneous coords


#from math import radians, sin, cos, tan
import math
import matrix as mat


def scale(sx, sy):
    """ return a matrix that scales by sx, sy.

    >>> scale(2,3)
    [[2.0, 0.0, 0.0], [0.0, 3.0, 0.0], [0.0, 0.0, 1.0]]
    >>>
    """
    matx = mat.unit(3)
    matx[0][0] *= sx
    matx[1][1] *= sy
    return matx

def translate(dx, dy):
    """return a matrix that translates by (dx, dy)

    >>> translate(-3, 2)
    [[1.0, 0.0, -3.0], [0.0, 1.0, 2.0], [0.0, 0.0, 1.0]]
    """
    matx = mat.unit(3)
    matx[0][2] = dx * 1.0
    matx[1][2] = dy * 1.0
    return matx


def rotate(angle):
    """returns a matrix that rotates angle degrees counter-clockwise

    >>> print(rotate(30))
    [[0.8660254037844387, -0.49999999999999994, 0.0], [0.49999999999999994, 0.8660254037844387, 0.0], [0.0, 0.0, 1.0]]
    """
    matx = mat.unit(3)
    rads = math.radians(angle)
    matx[0][0] = math.cos(rads)
    matx[0][1] = -1 * math.sin(rads)
    matx[1][0] = math.sin(rads)
    matx[1][1] = math.cos(rads)
    return matx


def window(box0, box1):
    """returns a transformation that maps box0 to box1

    note: a box is a tuple: (left, bottom, right, top) where
    (left,bottom) is the point at the lower-left corner and
    (right, top) is the point in the upper-right corner.

    >>> window((20, 10, 60,40), (5, 5, 9, 8))
    [[0.1, 0.0, 3.0], [0.0, 0.1, 4.0], [0.0, 0.0, 1.0]]
    >>> m=window((20, 10, 60,40), (5, 5, 9, 8))
    >>> mat.apply(m, (20,10,1))
    [5.0, 5.0, 1.0]
    >>> mat.apply(m, (60,40,1))
    [9.0, 8.0, 1.0]
    >>> mat.apply(m, (40,25,1))
    [7.0, 6.5, 1.0]

    """
    l0, b0, r0, t0 = box0
    l1, b1, r1, t1 = box1
    m = translate(-l0, -b0)
    sx = (r1 - l1) / (r0 - l0)
    sy = (t1 - b1) / (t0 - b0)
    m = mat.mul(scale(sx, sy), m)
    m = mat.mul(translate(l1, b1), m)
    return m


if __name__ == '__main__':
    import doctest
    doctest.testmod()
