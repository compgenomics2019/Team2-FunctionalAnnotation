# Team2-FunctionalAnnotation

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
run bash_initialization which runs SPP and TMHMM. It subsequently calls other python scripts for running other tools
to run command
./bash bash_initialization
