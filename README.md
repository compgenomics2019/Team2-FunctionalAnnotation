# Team2-FunctionalAnnotation

by Tzu-Chuan Huang, Bridget Neary, Mingming Cao, Di Zhou, Mansi Gupta and Priyam Raut

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
"Usage: functional_annotation_team2.py -i <input_dicrectory> [options]\n",
              "-i\t--input\tInput directory with faa files\n",
              "-ni\t--nucleotide_input\tInput directory with fna files\n",
              "-e\t--eggnog\tSearch against eggnog[optional]\n",
              "-sp\t--signalP\tRunning signalP to annotate signal peptide[optional]\n",
              "-tm\t--tmprotein\tRunning tmhmm to annotate transmembrane proteins[optinal]\n",
              "-ol\t--one_line\tOne line annotation with gene names[Ture or False]\n",
              "-v\t--verbose\tVerbose mode\n",
              "-h\t--help\tPrint usage\n")




