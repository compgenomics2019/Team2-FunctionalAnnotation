##### Annotation format annocement

###### For comman annotation gff from protein fasta files (from cluster or direct 50 fasta files).

- May leave multiple lines by different programs

- The start site and end site record the original contig position information, if programs applied protein positions, transfer to nucleotide positions.

- Leave the score column as blank if applied multiple databases.

- **GFF Type I** :Annotate resutls from a single program with **one line**. Different results from different database are annotated in the final column.

-- Define the final column with 

  ```shell
  ID=<Define this after merging>;Target=<Node name>;Each_program_name=Each_match;..;..; 
  ```
  
- **GFF Type II**: Leave multiple line for each gene but for clustered sequence, because we couldn't know exact each positions are, so just fill with '.' .

###### For ncRNA and CRISPR (direct from contigs)

-  Need new IDs and node names 

###### For merged file

- Define the common column with

  ```shell
  Node\tProgram\tPattern\tStart\End\Score\tStrand\t.\tDefined_column	
  ```

- Consist of types: **protein_match**, **sp**, **tm**, **ard**, **operon**, **ncRNA(spedific type)**,**CRISPR**, and/or other pattern names

- Apply bedtools sort with start sites and bedtools merge for overlaps (may happen between protein and non coding parts)

###### For final results present

- Clustered files (fasta/uc)
- Trimmed(if needed) interproscan/eggnog/ard/operon results with cluster
- Original signalP/tmhmm results
- Original ncRNA gffs and CRISPR results
- Merged gff files (for each sample) with two types
- 50 one-line annotation gff files with gene names (for each sample)
