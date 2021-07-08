#!/usr/bin/env python3
import argparse

def return_lines(input):
  tmp = open(input)
  return tmp.readlines()
  tmp.close()

def print_edited_lines(lines):
  for line in lines:
    print('DNA, ' + line.rstrip('\n'))

def main(args):
  lines = return_lines(args.input)
  print_edited_lines(lines)

if __name__ == "__main__":
  # Parse arguments if executed as main script
  parser = argparse.ArgumentParser(description='Prints edited partitions file to stdout')

  parser.add_argument('--input', dest="input", help="Input file", type=str, metavar='INPUT FILE')

  args = parser.parse_args()

  main(args)
