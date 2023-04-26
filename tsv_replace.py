#!/usr/bin/env python

import sys

if len(sys.argv) != 3:
    print("usage:", sys.argv[0], "target.tsv replace.tsv", file=sys.stderr)
    sys.exit(1)

replace_dict = dict()
with open(sys.argv[2]) as fin:
    for ln in fin:
        f = ln.rstrip("\n").split("\t")
        if len(f) == 2:
            replace_dict[f[0]] = f[1]

with open(sys.argv[1]) as fin:
    for ln in fin:
        f = ln.rstrip("\n").split("\t")
        for i in range(0, len(f)):
            if f[i] in replace_dict:
                f[i] = replace_dict[f[i]]
        print("\t".join(f))
