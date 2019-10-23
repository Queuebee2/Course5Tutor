### automated proteomics for bioinformatics course 5


In this repository we try to construct a pipeline with commandline tools to find and analyse orthologs of a protein

The expected input is a fasta file with a bunch of closely related orthologs.
These sequences will then be alligned and turned into a profile HMM using MAFFT and hmmerbuild commandtools
A consensus pattern is extracted from the HMM file and then blasted against protein databases to find more orthologs.
The current BLAST algorithm is mostly chosen out of convenience and lack of motivation (or understanding) to use other algorithms.
The program then iterates over the blast results, inserting each previously unknown sequence into our database, along with some efetched GO terms and the output of a regex.
