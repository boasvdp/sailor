#!/usr/bin/env python3

import argparse

def filter_no_genomes(df, threshold):
  total_genomes = df.shape[1] - 20
  threshold_genomes = total_genomes * threshold
  df_filt = df[df['number_genomes'] > threshold_genomes]
  return df_filt

def filter_dosage(df, dosage):
  df_filt = df[df['max_dose'] <= dosage]
  return df_filt

def main(args):
  import pandas as pd
  df = pd.read_csv(args.input, sep = '\t')
  df_filt_genomes = filter_no_genomes(df, args.threshold)
  if args.dosage is not None:
    df_final = filter_dosage(df_filt_genomes, args.dosage)
  else:
    df_final = df_filt_genomes
  df_final.to_csv(args.output, sep = '\t', index=False)

if __name__ == "__main__":
  # Parse arguments if executed as main script
  parser = argparse.ArgumentParser(description='Select core genes from PIRATE file PIRATE.gene_families.tsv')

  parser.add_argument('--input', dest="input", help="Input file", type=str, metavar='INPUT FILE')
  parser.add_argument('--threshold', dest="threshold", help="Threshold to define core (ratio of total strains, default: 0.95)", type=float, default=0.95, metavar='THRESHOLD')
  parser.add_argument('--max-dosage', dest="dosage", help="Max dosage to include", type=float, metavar='DOSAGE THRESHOLD')
  parser.add_argument('--output', dest="output", help="Output file", type=str, metavar='OUTPUT FILE')

  args = parser.parse_args()

  main(args)
