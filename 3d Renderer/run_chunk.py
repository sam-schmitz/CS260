# run_chunk.py -- ratrace a subset of a scene image
#    usage: pypy run_rt_sub.py scene0 320 240 4 1
# Two extra command line parameters: number of chunks, which chunk

import sys
import time
import pickle
from math import ceil

from ren3d.scenedef import load_scene
from ren3d.render_ray import raytrace_chunk


chunk_file = "chunks/chunk{:02d}"


class Progress:

    def __init__(self, size):
        self.size = size
        self.count = 0

    def show(self):
        self.count += 1
        print(str(round(self.count/self.size*100, 1))+"%", end="\r")
        sys.stdout.flush()

        
def main():
    scene, scenename = load_scene(sys.argv[1])
    size = int(sys.argv[2]), int(sys.argv[3])
    nchunks = int(sys.argv[4])
    off = int(sys.argv[5])
    scene.camera.set_resolution(*size)
    if off == 0:
        update = Progress(ceil(size[1]/nchunks)).show
    else:
        update = None
    chunk = raytrace_chunk(scene, size, nchunks, off, update)
    with open(chunk_file.format(off), "wb") as ofile:
        pickle.dump(chunk, ofile)
    with open(chunk_file.format(off)+".status", "w") as ofile:
        ofile.write("done\n")


if __name__ == "__main__":
    main()
