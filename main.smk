configfile: "config/config.yaml"

IDS, = glob_wildcards("genomes/{sample}.fasta")

rule all:
  input:
    "iqtree_out"

include: "workflow/rules/prokka.snake"
include: "workflow/rules/pirate.snake"
#include: "workflow/rules/align_core.snake"
#include: "workflow/rules/amas.snake"
#include: "workflow/rules/filter_aln.snake"
include: "workflow/rules/iqtree.snake"
