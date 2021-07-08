configfile: "config/config.yaml"

COREGENES, = glob_wildcards("pirate_features_out/{sample}.fasta")

rule all:
  input:
    "iqtree_out"

include: "workflow/rules/align_core.snake"
include: "workflow/rules/detect_recombination.snake"
include: "workflow/rules/filter_recombination.snake"
include: "workflow/rules/check_aln.snake"
include: "workflow/rules/select_aln.snake"
include: "workflow/rules/concat_aln.snake"
include: "workflow/rules/edit_partitions.snake"
include: "workflow/rules/iqtree.snake"
