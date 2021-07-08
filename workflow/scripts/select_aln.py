#!/usr/bin/env python3

import argparse
import pandas as pd
import os
import shutil

def create_dir(dir):
  if os.path.exists(dir):
    shutil.rmtree(dir)
  os.makedirs(dir)

def check_missing_pct(df, threshold):
  df_filt = df[df['Missing_percent'] <= threshold]
  list_genes = list(df_filt['Alignment_name'])
#  print(list_genes)
  return list_genes

def find_input_directories(input_files):
  list_input_directories = []
  for file in input_files:
    list_input_directories.append(os.path.dirname(file))
  set_input_directories = set(list_input_directories)
  return set_input_directories

def list_files(list_genes, input_directories):
  list_selected_files = []
  for gene in list_genes:
    counter = 0
    for inputdir in input_directories:
      try_path = os.path.join(inputdir, gene)
      if os.path.isfile(try_path):
        list_selected_files.append(try_path)
        counter = counter + 1
    if counter == 0:
      raise ValueError('Aln file ' + str(gene) + ' cannot be found in any of ' + str(input_directories))
    elif counter > 1:
      raise ValueError('Aln file ' + str(gene) + ' is found in more than directory of ' + str(input_directories))
  return list_selected_files

def copy_files(list_selected_files, outdir):
  for file in list_selected_files:
    shutil.copy(file, outdir)

def main(args):
  df = pd.read_csv(args.amas, sep = '\t')
  list_genes = check_missing_pct(df, args.threshold)
  set_input_directories = find_input_directories(args.input)
  list_selected_files = list_files(list_genes, set_input_directories)
  create_dir(args.outdir)
  copy_files(list_selected_files, args.outdir)

if __name__ == "__main__":
  # Parse arguments if executed as main script
  parser = argparse.ArgumentParser(description='Select core genes from PIRATE file PIRATE.gene_families.tsv')

  parser.add_argument('--input', dest="input", help="Input file", nargs='+', type=str, metavar='INPUT FILES')
  parser.add_argument('--threshold', dest="threshold", help="Maximum missing percent to filter out genes (default: 50)", type=float, default=50, metavar='THRESHOLD')
  parser.add_argument('--amas', dest="amas", help="AMAS Summary report", type=str, metavar='AMAS SUMMARY')
  parser.add_argument('--outdir', dest="outdir", help="Output directory", type=str, metavar='OUTPUT DIRECTORY')

  args = parser.parse_args()

  main(args)
