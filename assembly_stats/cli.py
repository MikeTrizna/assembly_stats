import argparse
import assembly_stats
import json

def cli():
    parser = argparse.ArgumentParser(description='Calculate statistics about genome assemblies.')
    parser.add_argument('filename',
                        help='Genome file in FASTA format.')
    options = parser.parse_args()
    contig_lens, scaffold_lens, gc_cont = assembly_stats.read_genome(options.filename)
    contig_stats = assembly_stats.calculate_stats(contig_lens, gc_cont)
    scaffold_stats = assembly_stats.calculate_stats(scaffold_lens, gc_cont)
    stat_output = {'Contig Stats': contig_stats,
                   'Scaffold Stats': scaffold_stats}
    print(json.dumps(stat_output, indent=2, sort_keys=True))
    return

if __name__ == "__main__":
    print('ok')
    cli()