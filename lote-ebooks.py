#!/usr/bin/env python3
import os, time, glob, subprocess

files = glob.glob('*.epub')

workers = []
while files or workers:
    while len(workers) < 4 and files:
        f = files.pop(0)
        w = subprocess.Popen(['ebook-convert', f,
            os.path.splitext(f)[0]+'.mobi'])
        workers.append(w)
    for w in list(workers):
        if w.poll() is not None:
            workers.remove(w)
    time.sleep(0.1)
