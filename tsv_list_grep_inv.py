#!/usr/bin/env python

import sys

if len(sys.argv) != 4:
    print("usage:", sys.argv[0], "list.txt col_num(1-origin) target.tsv", file=sys.stderr)
    exit(1)

tgt_col = int(sys.argv[2])

tgt_set = set()
fin = open(sys.argv[1], "r") if sys.argv[1] != "-" else sys.stdin
for l in fin:
    tgt_set.add(l.rstrip("\n"))
fin.close()

fin = open(sys.argv[3], "r") if sys.argv[3] != "-" else sys.stdin
for l in fin:
    f = l.rstrip("\n").split("\t")
    if len(f) < tgt_col or f[tgt_col - 1] not in tgt_set:
        print(l, end="")
fin.close()
