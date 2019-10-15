import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main_script import create_msa_mafft, create_hmm

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
