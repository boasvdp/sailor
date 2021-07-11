configfile: "config/config.yaml"

IDS, = glob_wildcards("genomes/{sample}.fasta")

rule all:
  input:
    "pirate_features_out"

include: "workflow/rules/prokka.snake"
include: "workflow/rules/pirate.snake"
include: "workflow/rules/define_core.snake"
include: "workflow/rules/pirate_get_features.snake"
