# Team2-FunctionalAnnotation

by Tzu-Chuan Huang, Bridget Neary, Mingming Cao, Di Zhou, Mansi Gupta and Priyam Raut

This pipeline is in /projects/team2/func_annotation/Team2-FunctionalAnnotation on the server.

The piepline should be run on the server that some of the databases and programs have fixed path.

It's a python script based on python 3.7 and above. 

The python3.7 can be found on the server /projects/team2/func_annotation/bin/python3

### OBJECTIVE

The objective of the group is to annotate the gff and fasta files of the draft genomes and try to uncover as much relevant information about the gene such as structural features such as transmembrane proteins, signal peptides, virulence factors, domains, motifs and functions.

### Requirements

**Python 2.7** 

**Python 3.6** or above

**interproscan 5.33-72.0**

**emapper** from eggNOG 4.5.1

**SignalP 5.0**

**TMHMM v2.0**

**CRT1.2-CLI**

**perl**

**blast+**

### Quick Start

To just run interproscan

python3 ./functional_annotation_team2.py -i <input_directory>

### Integrated Version

```shell
Usage: functional_annotation_team2.py -i <input_dicrectory> [options],
              -i  --input Input directory with faa files,
              -ni --nucleotide_input  Input directory with fna files,
              -e  --eggnog  Search against eggnog[optional],
              -crt  --crispr  Running CRISPR annotatation, # Uses assemlied contigs
              -ard  --antibiotic  Running antibiotic annotatation,
              -sp --signalP Running signalP to annotate signal peptide[optional],
              -tm --tmprotein Running tmhmm to annotate transmembrane proteins[optinal],
              -ol --one_line  One line annotation with gene names[Ture or False],
              -v  --verbose Verbose mode,
              -h  --help  Print usage
```

### Miniconda

Install the prerequirements using the miniconda command .Easisest installation is to create environments from the .yml files provided. They have all the dependencies required to use the pipeline. Please make sure the conda command is in your path.
```shell 
conda env create -f func_ann.yml
```
You can then run the program by activating the func_ann environment.

### TMHMM
Before running TMHMM make sure the the path of perl is specified correctly in TMHMM/bin/tmhmm and TMHMM/bin/tmhmmformat.pl
