

# deprecated because we're not using blast
def doBlast(filename=BLAST_OUTPUT , **kwargs):
    # take a sequence to exec5ute a blastn against the nt database
    # to do : add blasttype, db and matrix parameters

    # open output file
    blast_file = open(filename, 'w')

    # execute blast
    result_handle = NCBIWWW.qblast(**kwargs)

    # write results ( xml-string )
    blast_file.write(result_handle.read())
    

# deprecated because we shouldnt extract consensus patterns from hmm files
PROTEIN_SYMBOLS = 'ACDEFGHIKLMNPQRSTVWYadefghiklmnpqrstvwy'


def test_headers(l):
    """helper function for seq_from_hmm"""
    # when we find all these chars in a line, the matrix starts
    for char in "ACDEFGHIKLMNPQRSTVWY":
        if char not in l:
            return False
    return True

def seq_from_hmm(hmm_file=HMM_FILE):
    
    with open(hmm_file, 'r') as f:
        
        did_headers = False
        markov_word = ''
        
        for i, line in enumerate(f):
            if not did_headers:
                didHeaders = test_headers(line)
            else:
                try:
                    # the end of some lines look like      nnn x - - -
                    # with nn being numbers and x being a letter for a protein
                    # - being literally dashes, not sure what other possibilities
                    # are, yet.
                    # by splitting the whole line and taking the [-4]th element
                    # the character we obtain seems to be part of the consensus
                    # pattern
                    w = line.split()[-4]
                    if len(w) == 1 and w in PROTEIN_SYMBOLS:
                        markov_word += w
                except Exception as e:
                    print(e , "on row, ",i)
                
    return markov_word
