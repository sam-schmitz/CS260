# run_prt.py
# by: John Zelle

import sys
import os
import time
import pickle

from ren3d.image import Image

command = "python run_chunk.py {scene} {width} {height} {nchunks} {offset} &"
FNAME = "chunks/chunk{:02d}"

def assemble_chunks(chunks, size):
    nchunks = len(chunks)
    img = Image(size)
    for chunk_num, chunk in enumerate(chunks):
        y = chunk_num
        for line in chunk:
            for x in range(size[0]):
                img[x, y] = line[x]
            y += nchunks
    return img


def main():
    scene = sys.argv[1]
    width = int(sys.argv[2])
    height = int(sys.argv[3])
    try:
        nchunks = int(sys.argv[4])
    except IndexError:
        nchunks = 4

    os.system("rm -rf chunks/*")
    args = dict(scene=scene, width=width, height=height, nchunks=nchunks)
    t1 = time.time()
    # launch process to compute chunks
    for offset in range(nchunks):
        args["offset"] = offset
        os.system(command.format(**args))
    print("Launched")

    # wait for all the chunks
    for i in range(nchunks):
        fname = FNAME.format(i)
        while not os.path.isfile(fname+".status"):
            time.sleep(.5)
        print(i, end=" ")
        sys.stdout.flush()
    time.sleep(.1)

    # harvest and assemble_chunks
    chunks = []
    for i in range(nchunks):
        fname = FNAME.format(i)
        with open(fname, "rb") as infile:
            chunks.append(pickle.load(infile))
    print()

    img = assemble_chunks(chunks, (width, height))
    t2 = time.time()

    img.show()
    img.save("images/{}-rt-{:d}-{:d}.ppm".format(scene, width, height))
    print(round(t2-t1,1), "seconds")
    input("Press <Enter> to quit")
    img.unshow()


if __name__ == "__main__":
    main()
