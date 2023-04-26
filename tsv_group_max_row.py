#!/usr/bin/env python

import sys
import pandas as pd

if len(sys.argv) != 4:
    print("usage:", sys.argv[0], "in.tsv group_col_index(0-based) val_col_index", file=sys.stderr)
    sys.exit(1)

df = pd.read_table(sys.argv[1], header=None)
max_df = df.loc[df.groupby(int(sys.argv[2]))[int(sys.argv[3])].idxmax(), :]
max_df.to_csv(sys.stdout, header=None, index=None, sep="\t")
