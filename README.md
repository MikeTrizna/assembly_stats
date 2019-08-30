# assembly_stats

A Python script that takes a FASTA file as input and calculates both scaffold and contig statistics (N50, L50, etc.) from a scaffold FASTA file. It does this by breaking each scaffold wherever there is more than one N and then calculating statistics for both the scaffolds and contigs.

This is a re-write of fasta_metadata_parser to speed up the old implementation, and -- most importantly -- to learn how to install Python scripts onto the Smithsonian HPC.


## Usage

The only Python library that this script relies on is NumPy, but this is installed and set up in a conda environment on the HPC.

``` 
  # Load the HPC assembly_stats module, which activates a conda environment
  # with the appropriate versions of Python and NumPy installed.

  $ module load bioinformatics/assembly_stats

  # Now that the module is loaded, assembly_stats.py should be accessible directly
  # in your PATH.

  $ assembly_stats.py [genome_file.fasta]
```

After calculating the statistics for the genome assembly, they will be printed out in JSON format.

Next steps
----------

* Add ability to save NumPy sequence length arrays for further visualization, since generating these are what takes the most time.
