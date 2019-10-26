# important files to set
#### `FASTA_DATABASE : str `
the main database to query with hmmsearch

#### `MAIN_FASTA_FILENAME : str`
the main dataset of fasta files to create MSA’s with

#### `FASTA_TOADD_FILENAME : str `
keeps track of fasta sequences from this iteration. Will be added to MAIN_FASTA_FILENAME when the next iteration starts and then the file is cleared to start over. Only fasta files not previously existing in MAIN_FASTA will be added here.

# global variables
#### `DEFAULT_SELECTION : list[str]`
list of columns (as strings) used in fetching data from uniprot  
```
default = [ "go(biological process)",
            "go(cellular component)",
            "go(molecular function)"]
```


#### `HMMSEARCH_OPTIONS : str`
options to pass to the commandline call `>hmmsearch <options> hmm_file database`  

taken from the HMMER manual:  
`--tblout <f>` Save a simple tabular (space-delimited) file summarizing the
per-target output, with one data line per homologous target
sequence found.   
`--acc` Use accessions instead of names in the main output, where
available for profiles and/or sequences.  
`--noali` Omit the alignment section from the main output. This can greatly reduce the output volume.


```
default = " --tblout " + HMM_SEARCH_TAB_OUTPUT_FILENAME + " --acc --noali "
```
###### <sub>note:`HMM_SEARCH_TAB_OUTPUT_FILENAME` is a global string that holds filename hmmsearch output should be directed to  </sub>
