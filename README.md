# assembly_stats

[![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3968775.svg)](http://doi.org/10.5281/zenodo.3968775)

A Python library that takes a FASTA file as input and calculates both scaffold and contig statistics (N50, L50, etc.) from a scaffold FASTA file. It does this by breaking each scaffold wherever there is more than one N and then calculating statistics for both the scaffolds and contigs.

This is a re-write of [fasta_metadata_parser](https://github.com/pbfrandsen/fasta_metadata_parser) to speed up the old implementation, and -- most importantly -- to learn how to install Python scripts onto the Smithsonian HPC.

## Installation

```
pip install assembly_stats
```

## Usage

```
  $ assembly_stats -h

    usage: assembly_stats [-h] filename

    Calculate statistics about genome assemblies.

    positional arguments:
      filename    Genome file in FASTA format.

    optional arguments:
      -h, --help  show this help message and exit
```

After calculating the statistics for the genome assembly, they will be printed out in JSON format.

## Hoow to Cite

The assembly_stats package has been added to Zenodo in order to receive a stable DOI for citation: "10.5281/zenodo.3968774".

Please go to the Zenodo page for assembly_stats to find style-specific formatting options: https://zenodo.org/record/3968774.

Next steps
----------

* Add ability to save NumPy sequence length arrays for further visualization, since generating these are what takes the most time.
