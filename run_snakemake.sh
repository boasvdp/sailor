#!/bin/bash

if [[ ! -d pirate_features_out ]]
then
  snakemake --cluster 'sbatch' --cluster-config cluster.json --scheduler greedy --use-conda -s core_genome_definition.smk --immediate-submit --notemp -j all --latency-wait 60
else
  snakemake --cluster 'sbatch' --cluster-config cluster.json --scheduler greedy --use-conda -s core_genome_alignment.smk --immediate-submit --notemp -j all --latency-wait 60
fi
