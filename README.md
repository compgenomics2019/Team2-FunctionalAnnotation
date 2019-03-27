# Team2-FunctionalAnnotation

by Tzu-Chuan Huang, Bridget Neary, Mingming Cao, Di Zhou, Mansi Gupta and Priyam Raut

This pipeline is in /projects/team2/func_annotation/Team2-FunctionalAnnotation on the server.

The piepline should be run on the server that some of the databases and programs have fixed path.

###OBJECTIVE

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

-e is using eggnog methods

./functional_annotation_team2.py -c <clusteredfile> [-e] 
  
For each other patterns, use the scripts in other different repos.

An integrated version will be published soon.


### Integrated Version

```shell
Usage: functional_annotation_team2.py -i <input_dicrectory> [options],
              -i  --input Input directory with faa files",
              -ni --nucleotide_input  Input directory with fna files",
              -e  --eggnog  Search against eggnog[optional]",
              -sp --signalP Running signalP to annotate signal peptide[optional]",
              -tm --tmprotein Running tmhmm to annotate transmembrane proteins[optinal]",
              -ol --one_line  One line annotation with gene names[Ture or False]",
              -v  --verbose Verbose mode",
              -h  --help  Print usage\n")
```

