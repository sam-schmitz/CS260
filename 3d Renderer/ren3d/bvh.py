#bvh.py

def make_BVH(surfaces):
    #build BVH from list of Surfaces
    assert len(surfaces) > 0
    if len(surfaces) == 1:
        return surfaces[0]
    else:
        return BVH(surfaces)

class BVH:

    def __init__(self, surfaces, axis=0):
        n = len(surfaces)
        assert n > 1

        #sort the ibjects by "midpoint" along axis
        def keyfn(s): return s.bbox.midpoint[axis]
        surfaces.sort(key=keyfn)

        #spli into 2 halves
        n = n // 2
        next_axis = (axis + 1) % 3
        self.left = make_BVH(surfaces[:n], next_axis)
        self.right = make_BVH(surfaces[n:], next_axis)

        self.bbox = self.left.bbox.combine(self.right.bbox)

    def intersect(self, ray, interval, info):
        if not self.bbox.hit(ray, interval):
            return False

        hit = False
        if self.left.intersect(ray, interval, info):
            hit = True
            interval.high = info.t

        #repeat wiht right
        if self.right.intersect(ray, interval, info):
            hit = True
            interval.high = info.t
            
        return hit
