#!/usr/bin/env python

import sys
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description="Script to left-join dataframe pair.", formatter_class=argparse.MetavarTypeHelpFormatter)

parser.add_argument("left_df_file", type=str, help="left dataframe (TSV file)")
parser.add_argument("right_df_file", type=str, help="right dataframe (TSV file)")
parser.add_argument("-l", "--left_i", type=int, default=0, help="index of left dataframe (0-based)")
parser.add_argument("-r", "--right_i", type=int, default=0, help="index of right dataframe (0-based)")
parser.add_argument("-n", "--na_str", type=str, default="", help="string of NA value")
parser.add_argument("-d", "--header", action="store_true", help="input file has header line")

args = parser.parse_args()


opt_header = None
if args.header:
    opt_header = 0
left_df = pd.read_table(args.left_df_file, sep="\t", header=opt_header, index_col=args.left_i, dtype=object)
right_df = pd.read_table(args.right_df_file, sep="\t", header=opt_header, index_col=args.right_i, dtype=object)

left_df.index = left_df.index.astype(str)
right_df.index = right_df.index.astype(str)
merged_df = pd.merge(left_df, right_df, left_index=True, right_index=True, how="left")
merged_df.fillna(args.na_str, inplace=True)

opt_header = None
if args.header:
    opt_header = True
merged_df.to_csv(sys.stdout, sep="\t", header=opt_header)
