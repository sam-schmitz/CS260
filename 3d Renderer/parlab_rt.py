# parlab_rt.py
# by: John Zelle

import sys
import os
import time
import pickle
import glob
from parlab import Runner

from ren3d.image import Image

command = "pypy run_chunk.py {scene} {width} {height} {nchunks} {offset}"
FNAME = "chunks/chunk{:02d}"

def launch_processes(run, args, nchunks):
    print("Launching", nchunks, "process...", end="")
    sys.stdout.flush()
    for offset in range(1, nchunks):
        args["offset"] = offset
        host = run.remote(command.format(**args))
        #print(offset, end=" ")
        #sys.stdout.flush()
    print("Done")


def wait_for_chunks(nchunks):
    print("\nWaiting for chunks to complete")
    done = 0
    while True:
        done1 = len(glob.glob("chunks/*.status"))
        if done1 > done:
            print("Done", done1, end='\r')
            sys.stdout.flush()
            done = done1
        if done == nchunks:
            break
        time.sleep(.1)
    print("\nComplete!")


def collect_chunks(nchunks):
    print("Collecting chunks")
    chunks = []
    for i in range(nchunks):
        fname = FNAME.format(i)
        with open(fname, "rb") as infile:
            chunks.append(pickle.load(infile))
        os.unlink(fname+".status")
        os.unlink(fname)
    return chunks


def assemble_chunks(chunks, size):
    nchunks = len(chunks)
    img = Image(size)
    for chunk_num, chunk in enumerate(chunks):
        y = chunk_num
        for line in chunk:
            for x in range(size[0]):
                img[(x, y)] = line[x]
            y += nchunks
    return img


def main():
    scene = sys.argv[1]
    width = int(sys.argv[2])
    height = int(sys.argv[3])
    try:
        nchunks = int(sys.argv[4])
    except IndexError:
        nchunks = 37
    args = dict(scene=scene, width=width, height=height, nchunks=nchunks)

    run = Runner()
    print("Dead hosts:", run.deadhosts)
    run.local("rm -rf chunk/*")  #  clean chunk directory

    t1 = time.time()
    launch_processes(run, args, nchunks)

    # run "main" chunk locally
    args["offset"] = 0
    run.local(command.format(**args), True)
    time.sleep(.1)

    wait_for_chunks(nchunks)
    chunks = collect_chunks(nchunks)
 
    img = assemble_chunks(chunks, (width, height))
    t2 = time.time()

    img.show()
    img.save("images/{}-rt-{:d}-{:d}.ppm".format(scene, width, height))
    print()
    print(t2-t1, "seconds")
    input("Press <Enter> to quit")
    img.unshow()


if __name__ == "__main__":
    main()
