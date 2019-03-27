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
Usage: functional_annotation_team2.py -i <input_dicrectory> [options]",
              "-i --input Input directory with 50 faa file,
              "-e --eggnog Search against eggnog[optional]",
              "-sp --signalP Running signalP to annotate signal peptide[optional]",
              "-tm --tmprotein Running tmhmm to annotate transmembrane proteins[optional]",
              "-ol --one_line One line annotation with gene names[True or False]",
              "-v --verbose Verbose mode",
              "-h --help Print usage")






