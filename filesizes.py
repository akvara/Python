#!/usr/bin/python

import sys
import os
from os.path import join, getsize

def getFileSizes(dir):
    list = []
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.islink(path):
            # print "Not a file, a link", path
            continue
        if not os.path.isdir(path):
            list.append((getsize(path), name, dir))
        else:
            # print path, " is dir"
            list = list + getFileSizes(path)
    return list

def printFileSizes(list, level):
    if level == 0:
        divider = 1
        label = "b"
    elif level == 1:
        divider = 1024
        label = "kb"
    elif level == 2:
        divider = 1024 * 1024
        label = "mb"
    elif level == 3:
        divider = 1024 * 1024 * 1024
        label = "gb"
    else:
        print "Level is tooo high"
        exit(-1)

    maxwid = max([len(str(size / divider)) for (size, name, path) in list])
    for (size, name, path) in list:
        if size / divider > 0:
            print (str(size / divider) + label).rjust(maxwid + len(label)), name

def sortFileList(list):
    return sorted(list, key=lambda tup: tup[0], reverse=True)


if __name__ == "__main__":
    # execute only if run as a script
    arg_names = ['command', 'dir', 'level', 'number']
    args = dict(zip(arg_names, sys.argv))
    level = int(args['level'] if  'level' in args else 2)
    dir = args['dir'] if  'dir' in args else '.'
    number = args['number'] if  'number' in args else 10
    filelist = sortFileList(getFileSizes(dir))
    printFileSizes(filelist[:number], level)
    print "Total", len(filelist), "files"
