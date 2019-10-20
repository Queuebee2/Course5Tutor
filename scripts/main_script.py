from sys import argv
import subprocess
import os.path

from bioservices import UniProt
from DbConnector import DbConnector


def create_msa_mafft(fasta_filename, msa_destination_filename, verbose=False):
    """calls 'mafft' through the shell to create a
       multiple sequence alignment (msa_filename)

    ARGS:
        fasta_filename: string
            relative path (just a filename) of a file containing fasta
            sequences to be aligned

        msa_destination_filename: string
            relative path in which to save the multiple sequence alignment

    """

    # Check whether msa has already been made
    if os.path.isfile(msa_destination_filename):
        pass
    # Execute command if msa hasn't been made before
    else:
        cmd = "mafft " + fasta_filename + " > " + msa_destination_filename
        e = subprocess.check_call(cmd, shell=True)
        if verbose:  print(e)
    return


def create_hmm(msa_filename, hmm_destination_filename, verbose=False):
    """calls 'hmmbuild' through the shell to create a hmm profile
       from a multiple sequence alignment (msa_filename)

    ARGS:
        msa_filename: string
            relative path (just a filename) of
            a file containing a valid MSA

        hmm_destination_filename: string
            relative path in which to create
            a hmm profile using hmmer

    """

    # Check whether hmm has already been made
    if os.path.isfile(hmm_destination_filename):
        pass
    # Execute command if hmm hasn't been made before
    else:
        cmd = "hmmbuild " + hmm_destination_filename + " " + msa_filename
        e = subprocess.check_call(cmd, shell=True)
        if verbose:  print(e)
    return

def search_uniprot(uniprot_handle, uniprot_entry_id, columns, verbose=False):

    search_result = uniprot_handle.search(uniprot_entry_id, columns=columns)
    if verbose:
        print("searched", uniprot_entry_id)


#TODO parse search_result here (not really needed probably)
# could just do an insert with columns=columns, values=search_result.split

#TODO SQL insert here


def main():

    # create an object to handle communications with mySQL database
    our_database_handle = DbConnector()

    # create uniprot handle object
    # todo: find out if 'handle' is the right terminology here
    uniprot_handle = UniProt(verbose=False)


    # determine input file(s)
        # check validity
        # combine multiple fasta's into one for msa


# TODO replace this with if files > 0
    if 0 != 1:
        running = True

        
    # 'running' loop
    while running:
        
        # msa
        create_msa_mafft(fasta_filename, msa_destination_filename)

        # hmm
        create_hmm(msa_filename, hmm_destination_filename)

        # doBlast/search/jackhmmer/PSI/PHI ??????????
# TODO  find solution

        # will the format be
        blast_results = ['file','names']
        #or
        blast_results = 'filename_of_fasta_witha_all_results'

        # that determines how we loop over the sequences (to find their ID's)
        with open(blast_results, 'r') as file:

            # Assume fasta starts with >
            header = file.readline()
            # check if that assumption was true.
            assert header.startswith(">"), "file not properly Fasta Formatted"

            sequence = ''
            for l in file:
                line = l.strip("\n")
                if line.startswith(">"):
                    if header != '':
                        
                        
# TODO                  detect which database it comes from?        https://en.wikipedia.org/wiki/FASTA_format#NCBI_identifiers    
                        # SWISS-PROT 	    sp|accession|name       ''
                        # PDB 	            pdb|entry|chain         ''
                        # Refseq protein    >NP_id                  https://www.ncbi.nlm.nih.gov/books/NBK50679/
                        

                        # check if it already exists in our database (?? will this be costly?)

                        # Do we care about redundant sequences?
                        # Proposal: remove junction table and add 3 db-id columns to
                        # primary database table 
                        # https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5225397/
                        # http://weizhongli-lab.org/cd-hit/


                    # prep loop for next sequence
                    header = line
                    sequence = ''

                else:
                    sequence += line

        
        # find GO terms and other traits for each protein



if __name__ == "__main__":
    print('running from main')
    
    main()

