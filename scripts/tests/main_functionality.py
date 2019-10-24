import subprocess
from sys import argv
import os

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


if __name__ == '__main__':
    test_fasta_filename = "multiple_fasta_sequences.fasta"
    test_msa_filename = 'msa_file.msa'
    test_hmm_filename = 'hmm_file.hmm'

    print('trying to create msa...')
    create_msa_mafft(test_fasta_filename, test_msa_filename)

    print('trying to create hmm...')
    create_hmm(test_msa_filename, test_hmm_filename)

    print('done')


# TODO add assertions blabla
