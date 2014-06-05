#! /usr/bin/env python

# (c) 2014 Patrick Kage

import sys, os
try:
        outfile = open(sys.argv[2], 'w')
except:
        print "Failed to open outfile!"
        sys.exit(1)

try:
        infile = sys.argv[1]
except:
        print "No infile specified!"
        sys.exit(1)

def strip(line):
        if (line[0:2] == "#@"):
                return line[3:]
        else:
                return ""

def preprocess(fn):
        if fn[-1] == '\n':
                fn = fn[:-1]
        if not os.path.exists(fn):
                print "\nFile " + fn + " does not exist."
                return False

        f = open(fn, "r")
        for line in f:
                if (strip(line) != ""):
                        preprocess(strip(line))
                outfile.write(line)
        return True

preprocess(infile)
print "preprocessed " + infile
sys.exit(0)
